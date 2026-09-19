# Noble Forest RV Village — Design Guidelines

*Last updated: 2026-09-19 | Version 2.0*
*Companion document to: Noble Forest RV Visual Style Guide & Content Strategy*

---

## Purpose of This Document

The Visual Style Guide covers **what** to build and **how** it should feel (e.g., earthy, protective, premium). 

This document covers **why** and **how to implement it logically**—the rationale behind decisions, the interaction principles, developer implementation standards, and the guidelines that inform judgment calls when building the static HTML/CSS structure.

Read both. When they conflict, raise it — don't guess.

---

## Typography System

### Font Roles

| Role | Font | Weights Used |
|---|---|---|
| Display / Hero | **Montserrat** | Bold (700) |
| Section Headers | **Montserrat** | Bold (700), Semi-Bold (600) |
| Body / UI | **Inter** (or Open Sans) | Regular (400), Medium (500) |
| Tags / Labels / Chips | **Inter** | Medium (500) |

### Loading Fonts

Google Fonts should be loaded in the document `<head>` using `font-display: swap` to ensure text remains visible during webfont loading.

---

## Color System & CSS Custom Properties

Define all color and spacing tokens as CSS custom properties on `:root`. Do not hard-code hex values in component styles.

css
:root {
  /* System Colors */
  --color-primary: #48751F;
  --color-secondary: #F3F5F8;
  --color-body-text: #B37822;
  --color-accent: #D2963E;

  /* Custom Colors */
  --color-gold-accent: #F5C23F;
  --color-green-text: #024600;
  --color-grey-accent: #F3F3F3;
  --color-grey-bg: #E9E9E9;
  --color-bg-kit: #FFFFFF;
  --color-white-element: #FFFFFF;
  --color-overlay-bg: #000000CC;
  
  /* Utilities */
  --color-focus-ring: #D2963E;
}


---

## Interaction Principles

### 1. Booking Redirection Model
Clicking any core "Check Availability" or "Book Now" CTA must open the Firefly Reservations interface (`https://app.fireflyreservations.com/reserve/property/NobleForestRV`) in a clean, new browser tab (`target="_blank"`). Never attempt to embed the booking engine via iframe, as it compromises mobile usability.

### 2. Rate Layout Logic
Site-type cards must cleanly toggle or clearly present the flat "All-Bills-Included" distinction side-by-side with covered dimensions (40'x20') so users don't look for utility dropdown maps or hidden calculators. Predictability is the core value proposition.

### 3. Every action needs visible feedback within 100ms
Ensure native CSS hover and active states are applied to all interactive elements. Button presses should have an immediate visual response (e.g., a slight background color darken or transform scale).

---

## Developer Implementation Notes

### Responsive Breakpoints

* **Desktop:** 1025px and up.
* **Tablet:** 768px to 1024px.
* **Mobile:** 767px and below (optimized heavily for single-column mobile use by contractors on phones or travelers navigating on the road).

### Semantic HTML

Use semantic HTML elements strictly. Do not use `<div>` for interactive elements.

* **Navigation:** `<nav>`
* **Main content:** `<main>`
* **Sections:** `<section>` with `aria-labelledby` linking to the section's H2.
* **All buttons:** `<button>` — never a styled `<div>` or `<span>`.
* **External booking links:** `<a>` with `href` and `target="_blank"`.

### Focus Management

Focus states must be explicitly visible on all interactive elements. Do not suppress focus outlines with `outline: none` without providing a visible replacement.

css
:focus-visible {
  outline: 2px solid var(--color-focus-ring);
  outline-offset: 2px;
}

### Skip Navigation

The first focusable element on every page should be a skip-to-content link, visible only on focus.

html
<a href="#main-content" class="skip-link">Skip to main content</a>

---

## Accessibility Audit Checklist

Use at design review and before release.

**Visual Layer:**
- [ ] All text elements meet minimum contrast targets (4.5:1 for standard body text; 3:1 for large display elements against off-white background tokens).
- [ ] Structural layout paths clearly call out the presence of nighttime security lighting grids and continuous onsite manager presence using descriptive text elements, not just visual icon indicators (e.g., screen readers must be able to read "Onsite live-in manager").
- [ ] Logical heading hierarchy (one H1 per page, H2s for sections, H3s for sub-sections).
- [ ] All images have appropriate alt text (e.g., `alt="Family standing outside their RV under mature shade trees"`).

**Interaction Layer:**
- [ ] Mobile menus are fully toggleable and accessible without touch target overlapping.
- [ ] Minimum touch target size for touchscreens is set strictly to 44px x 44px for navigation links, form inputs, and booking indicators.
- [ ] All interactive elements are reachable and operable via keyboard.
- [ ] Focus order follows visual reading order.