"use strict";
// Authored samples only. No network, model, persistence or external execution.
(() => {
  const fixtures = {
    writing: {
      prompt: "How can I make this argument easier to follow?",
      response: "Start with the point you want the reader to remember. Then use the evidence to make that point credible—not to delay it.",
      title: "A clearer argument",
      summary: "One central claim, one supporting example, and a clear explanation of why the example matters.",
      note: "Lead with the claim.\n\nShow one specific example.\n\nExplain how the example supports the claim, and state the condition under which the claim applies.\n\nEnd with what the reader can now understand or do."
    },
    comparison: {
      prompt: "Should this be a conversation, a dashboard, or a document?",
      response: "Choose the surface around what the person needs to do next. A conversation helps them frame the problem; a document helps them keep working on an answer.",
      title: "Choose the smallest useful surface",
      summary: "Conversation for exploration. A document for sustained editing. A dashboard only for repeated monitoring.",
      note: "Conversation\nUse when the question is still taking shape.\n\nDocument\nUse when the user needs to inspect, revise and retain an answer.\n\nDashboard\nUse when comparing repeated observations is the actual job—not merely to fill space."
    },
    research: {
      prompt: "Help me turn a broad idea into a question I can investigate.",
      response: "Name the decision that is difficult today. Then identify the smallest change you could observe that would explain why it is difficult.",
      title: "A more focused research question",
      summary: "A specific setting, an observable change, and a reason that the change matters.",
      note: "Setting\nWhere does the problem occur?\n\nObservable change\nWhat would count as a meaningful difference?\n\nExplanation\nWhat mechanism could account for that difference?\n\nEvidence\nWhat observation would distinguish your explanation from another?"
    }
  };
  const byId = id => document.getElementById(id);
  const state = { scenario: "writing", version: 1, note: fixtures.writing.note, dirty: false, mode: "light", pending: null };
  const media = window.matchMedia("(prefers-color-scheme: dark)");
  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
  const feedback = message => { byId("feedback").textContent = message; };

  function updateDraftState() {
    state.dirty = byId("note-content").value !== state.note;
    byId("edit-status").textContent = state.dirty ? "Unsaved changes · kept when closed" : "All edits applied in this tab";
    byId("save-note").disabled = !state.dirty;
  }
  function closeNote(restoreFocus = true) {
    byId("working-note").hidden = true;
    byId("workspace").classList.remove("is-open");
    byId("open-note").setAttribute("aria-expanded", "false");
    if (restoreFocus) byId("open-note").focus();
    // Deliberately do not reset the editor: unsaved drafts survive closing.
  }
  function renderScenario(key) {
    if (!Object.hasOwn(fixtures, key)) return;
    const item = fixtures[key];
    state.scenario = key; state.version = 1; state.note = item.note;
    byId("user-message").textContent = item.prompt;
    byId("response-text").textContent = item.response;
    byId("result-title").textContent = item.title;
    byId("result-summary").textContent = item.summary;
    byId("note-heading").textContent = item.title;
    byId("note-content").value = item.note;
    byId("version-label").textContent = "Version 1";
    byId("message").value = "";
    byId("send-message").disabled = true;
    byId("thread-history").replaceChildren();
    byId("conversation").classList.remove("has-activity");
    document.querySelectorAll("[data-scenario]").forEach(button =>
      button.setAttribute("aria-pressed", String(button.dataset.scenario === key)));
    updateDraftState();
    closeNote(false);
    feedback("All examples are authored samples. Nothing is sent to a server.");
  }
  function requestTransition(run, trigger) {
    if (!state.dirty) { run(); return; }
    state.pending = { run, trigger };
    byId("draft-dialog").showModal();
    byId("keep-draft").focus();
  }
  function dismissTransition() {
    const target = state.pending?.trigger;
    state.pending = null;
    byId("draft-dialog").close();
    if (target?.isConnected) target.focus();
  }
  function applyTheme(mode) {
    state.mode = mode;
    const resolved = mode === "system" ? (media.matches ? "dark" : "light") : mode;
    document.body.dataset.theme = resolved;
    document.documentElement.style.colorScheme = resolved;
    document.querySelector('meta[name="theme-color"]').content = resolved === "dark" ? "#141413" : "#FAF9F5";
    document.querySelectorAll("[data-mode]").forEach(button =>
      button.setAttribute("aria-pressed", String(button.dataset.mode === mode)));
  }
  function appendLocalTurn(message) {
    const user = document.createElement("p");
    user.className = "user-message";
    user.textContent = message;
    const assistant = document.createElement("p");
    assistant.className = "local-answer";
    assistant.textContent = "Local preview only: this text was added to the conversation. No AI model analyzed it.";
    byId("thread-history").append(user, assistant);
    byId("conversation").classList.add("has-activity");
    assistant.scrollIntoView({ block: "nearest", behavior: reducedMotion.matches ? "auto" : "smooth" });
  }

  document.querySelectorAll("[data-scenario]").forEach(button => button.addEventListener("click", () =>
    requestTransition(() => renderScenario(button.dataset.scenario), button)));
  document.querySelectorAll("[data-mode]").forEach(button =>
    button.addEventListener("click", () => applyTheme(button.dataset.mode)));
  media.addEventListener("change", () => { if (state.mode === "system") applyTheme("system"); });
  byId("new-chat").addEventListener("click", event =>
    requestTransition(() => { renderScenario(state.scenario); byId("message").focus(); }, event.currentTarget));
  byId("keep-draft").addEventListener("click", dismissTransition);
  byId("discard-draft").addEventListener("click", () => {
    const pending = state.pending;
    state.pending = null;
    byId("draft-dialog").close();
    pending?.run();
  });
  byId("draft-dialog").addEventListener("cancel", event => { event.preventDefault(); dismissTransition(); });
  byId("open-note").addEventListener("click", () => {
    if (byId("working-note").hidden) {
      byId("working-note").hidden = false;
      byId("workspace").classList.add("is-open");
      byId("open-note").setAttribute("aria-expanded", "true");
      // Content is initialized when scenarios change, never on open.
    }
    byId("note-content").focus({ preventScroll: true });
    if (window.innerWidth <= 1160) byId("working-note").scrollIntoView({
      behavior: reducedMotion.matches ? "auto" : "smooth", block: "start"
    });
  });
  byId("close-note").addEventListener("click", () => closeNote());
  byId("working-note").addEventListener("keydown", event => {
    if (event.key === "Escape") { event.preventDefault(); closeNote(); }
  });
  byId("note-content").addEventListener("input", updateDraftState);
  byId("save-note").addEventListener("click", () => {
    const edited = byId("note-content").value;
    if (!edited.trim()) {
      feedback("The note is empty. Add text before applying the edit.");
      byId("note-content").focus();
      return;
    }
    if (edited === state.note) { updateDraftState(); return; }
    state.note = edited;
    state.version++;
    byId("version-label").textContent = `Version ${state.version}`;
    const compact = edited.trim().replace(/\s+/g, " ");
    byId("result-summary").textContent = compact.length > 180 ? `${compact.slice(0, 177)}…` : compact;
    updateDraftState();
    feedback("Edit applied in this tab. No cloud save or publishing occurred.");
  });
  byId("copy-note").addEventListener("click", async () => {
    try {
      if (!navigator.clipboard?.writeText) throw new Error("Clipboard API unavailable");
      await navigator.clipboard.writeText(byId("result-summary").textContent);
      feedback("Summary copied to your clipboard.");
    } catch {
      feedback("Clipboard access is unavailable here. Open the working note to select and copy its text.");
    }
  });
  byId("message").addEventListener("input", () => {
    byId("send-message").disabled = !byId("message").value.trim();
  });
  // Browsers that permit it will warn before a dirty draft is discarded by reload/navigation.
  window.addEventListener("beforeunload", event => {
    if (!state.dirty) return;
    event.preventDefault();
    event.returnValue = "";
  });
  byId("composer").addEventListener("submit", event => {
    event.preventDefault();
    const message = byId("message").value.trim();
    if (!message) return;
    appendLocalTurn(message);
    byId("message").value = "";
    byId("send-message").disabled = true;
    feedback("Message added to local preview. Nothing was sent to a server.");
  });
  renderScenario("writing");
  applyTheme("light");
})();
