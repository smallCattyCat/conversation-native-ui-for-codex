/* Reusable browser behaviors for Claude-inspired demo surfaces.
 * These are standalone DOM helpers, NOT MCP host transport.
 */
export function initCarousel(root, onSelect = () => {}) {
  const track = root.querySelector("[data-carousel-track]");
  const previous = root.querySelector("[data-carousel-previous]");
  const next = root.querySelector("[data-carousel-next]");
  const cards = Array.from(root.querySelectorAll("[data-carousel-option]"));
  if (!track || !previous || !next || !cards.length) {
    throw new Error("Carousel requires a track, two navigation buttons, and option cards");
  }
  function update() {
    previous.disabled = track.scrollLeft <= 2;
    next.disabled = (track.scrollWidth - track.clientWidth - track.scrollLeft) <= 2;
  }
  function move(direction) {
    const cardWidth = cards[0].getBoundingClientRect().width;
    const gap = parseFloat(getComputedStyle(track).columnGap) || 0;
    track.scrollBy({ left: (cardWidth + gap) * direction,
      behavior: matchMedia("(prefers-reduced-motion: reduce)").matches ? "instant" : "smooth" });
  }
  previous.addEventListener("click", () => move(-1));
  next.addEventListener("click", () => move(1));
  track.addEventListener("scroll", update, { passive: true });
  const observer = typeof ResizeObserver !== "undefined" ? new ResizeObserver(update) : null;
  observer?.observe(track);
  for (const card of cards) {
    const action = card.querySelector("[data-select-option]");
    if (!action) throw new Error("Each option needs one visible action");
    action.addEventListener("click", () => {
      cards.forEach(item => {
        const selected = item === card;
        item.setAttribute("aria-current", String(selected));
        item.querySelector("[data-select-option]").setAttribute("aria-pressed", String(selected));
      });
      onSelect(card.dataset.carouselOption, card);
    });
  }
  update();
  return { update, destroy: () => observer?.disconnect() };
}

export function initWorkspace(dialog, buttons, closeButton) {
  let opener = null;
  function open(event) {
    opener = event.currentTarget;
    if (!dialog.open) dialog.showModal();
    closeButton.focus();
  }
  buttons.forEach(button => button.addEventListener("click", open));
  closeButton.addEventListener("click", () => dialog.close());
  dialog.addEventListener("close", () => {
    if (opener?.isConnected) opener.focus();
  });
  return { open, close: () => dialog.close() };
}
