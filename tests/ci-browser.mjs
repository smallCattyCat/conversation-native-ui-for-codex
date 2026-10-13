// Optional GitHub Actions browser verification. Requires 'npm install' and Playwright Chromium.
import { chromium } from "playwright";
import { spawn } from "node:child_process";
const port = 8799;
const origin = "http://127.0.0.1:" + port;
const server = spawn("python3", ["-m","http.server", String(port), "--bind", "127.0.0.1"], { stdio: "ignore" });
let browser;
async function waitForServer() {
  for (let i=0;i<80;i++) {
    try { const response=await fetch(origin+"/tests/browser-checks.html"); if (response.ok) return; } catch {}
    await new Promise(resolve=>setTimeout(resolve,100));
  }
  throw new Error("Local test server did not start");
}
try {
  await waitForServer();
  browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({ viewport: { width:1440, height:900 }, deviceScaleFactor:1 });
  await page.goto(origin+"/tests/browser-checks.html");
  await page.waitForFunction(() => {
    const text=document.querySelector("#report")?.textContent??"";
    return text.startsWith("PASS:") || text.startsWith("FAIL");
  }, undefined, { timeout:20000 });
  const report=await page.locator("#report").textContent();
  if (!/^PASS: \d+ assertions/.test(report)) throw new Error(report);
  console.log(report.split("\n")[0]);
  await page.goto(origin+"/examples/pattern-gallery/");
  await page.screenshot({ path:"pattern-gallery-ci.png", fullPage:true });
  const overflow=await page.evaluate(() => document.documentElement.scrollWidth>window.innerWidth);
  if (overflow) throw new Error("Gallery overflows desktop width");
  await page.setViewportSize({ width:390, height:844 });
  await page.screenshot({ path:"pattern-gallery-mobile-ci.png", fullPage:true });
  const mobileOverflow=await page.evaluate(() => document.documentElement.scrollWidth>window.innerWidth);
  if (mobileOverflow) throw new Error("Gallery overflows 390px");
  // Check the separately staged GitHub Pages artifact, not only the repository-source examples.
  await page.setViewportSize({ width:1440, height:900 });
  await page.goto(origin + "/site-dist/");
  if (!(await page.title()).includes("Conversation-Native UI")) throw new Error("Static site home is missing");
  await page.getByRole("link",{name:/Interaction pattern gallery/i}).click();
  if (!page.url().includes("/site-dist/examples/pattern-gallery/")) throw new Error("Staged gallery navigation failed");
  if (!(await page.locator("[data-cn-carousel]").isVisible())) throw new Error("Staged carousel failed to load");
  await page.goto(origin + "/site-dist/");
  await page.setViewportSize({ width:390, height:844 });
  await page.screenshot({ path:"site-home-mobile-ci.png", fullPage:true });
  if (await page.evaluate(() => document.documentElement.scrollWidth>window.innerWidth)) throw new Error("Static site home overflows 390px");
} catch (error) {
  console.error(error);
  process.exitCode=1;
} finally {
  await browser?.close();
  server.kill("SIGTERM");
}
