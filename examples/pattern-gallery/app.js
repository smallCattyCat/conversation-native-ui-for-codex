"use strict";
import { initCarousel, initWorkspace } from "../../.agents/skills/conversation-native-ui/assets/patterns.js";
const $ = id => document.getElementById(id);
const media = matchMedia("(prefers-color-scheme: dark)");
let themeMode = "light";
function setTheme(mode) {
  themeMode = mode;
  const resolved = mode === "system" ? (media.matches ? "dark" : "light") : mode;
  document.body.dataset.theme = resolved;
  document.documentElement.style.colorScheme = resolved;
  document.querySelector('meta[name="theme-color"]').content = resolved === "dark" ? "#141413" : "#FAF9F5";
  document.querySelectorAll("[data-gallery-theme]").forEach(button =>
    button.setAttribute("aria-pressed", String(button.dataset.galleryTheme === mode)));
}
document.querySelectorAll("[data-gallery-theme]").forEach(button =>
  button.addEventListener("click", () => setTheme(button.dataset.galleryTheme)));
media.addEventListener("change", () => { if (themeMode === "system") setTheme("system"); });
let cardView = "ready";
const cardActions = [$("card-inspect"), $("card-copy")];
function setCardView(view) {
  cardView = view;
  for (const name of ["ready", "loading", "empty", "error"]) $("card-" + name).hidden = name !== view;
  document.querySelectorAll("[data-card-view]").forEach(button =>
    button.setAttribute("aria-pressed", String(button.dataset.cardView === view)));
  cardActions.forEach(button => { button.disabled = view !== "ready"; });
  $("inline-card").classList.toggle("cn-card--error", view === "error");
  $("card-feedback").textContent = ({
    ready: "Ready to inspect. Demo data only.",
    loading: "Loading state preview only — no request is running.",
    empty: "No result available to inspect.",
    error: "Illustrative error state — no request failed."
  })[view];
}
document.querySelectorAll("[data-card-view]").forEach(button =>
  button.addEventListener("click", () => setCardView(button.dataset.cardView)));
const carousel = initCarousel($("patterns-carousel"), label => {
  $("selection-status").textContent = "Selected: " + label + ". This is a local UI choice only.";
});
const dialog = $("workspace-dialog");
initWorkspace(dialog, [...document.querySelectorAll("[data-open-workspace]"), $("card-inspect")], $("workspace-close"));
const text = $("workspace-text");
const status = $("workspace-status");
const save = $("workspace-save");
let saved = text.value, version = 1;
function updateDraft() {
  const dirty = saved !== text.value;
  save.disabled = !dirty;
  status.textContent = dirty ? "Unsaved changes · retained when closed" : "No unsaved edits · Version " + version;
}
text.addEventListener("input", updateDraft);
save.addEventListener("click", () => {
  if (!text.value.trim()) { status.textContent = "Add some text before applying."; text.focus(); return; }
  if (text.value === saved) { updateDraft(); return; }
  saved = text.value; version++;
  updateDraft();
  status.textContent = "Applied locally · Version " + version + ". No cloud save.";
});
$("card-copy").addEventListener("click", async () => {
  if (cardView !== "ready") return;
  try {
    if (!navigator.clipboard?.writeText) throw new Error("clipboard unavailable");
    await navigator.clipboard.writeText("Put the central claim first, then explain how each example supports it.");
    $("card-feedback").textContent = "Sample summary copied.";
  } catch {
    $("card-feedback").textContent = "Clipboard unavailable; select the summary to copy it.";
  }
});
setTheme("light");
setCardView("ready");
carousel.update();
