# Website Migration & Refactoring Implementation Plan
**Project:** Exact clone of current WordPress site into modern, static code architecture.
**Goal:** Pixel-perfect recreation utilizing clean Tailwind CSS and established design tokens, stripping away all WordPress bloat.

---

## Phase 1: Foundation (Finalizing the Rulebooks) — COMPLETE
*The project markdown files (moved to `_docs/`) act as the governing standards for this project.*

*   **COMPLETE `visual-style-guide.md` & `design-guidelines.md`:** Hex codes (`primary: '#48751F'`, `secondary: '#F3F5F8'`, `accent: '#D2963E'`), Google Fonts (Montserrat & Inter), focus-visible outlines, and semantic HTML tags (`<main>`, `<section>`, `<article>`).
*   **COMPLETE `content-strategy.md`:** Tone, vocabulary constraints, and Firefly booking links (`target="_blank"`).
*   **COMPLETE `site-architecture.md`:** Clean static HTML route mapping (`amenities.html`, `rates.html`, `directions.html`, `privacy-policy.html`, `policies.html`, `site-types.html`).

---

## Phase 2: Source Extraction & Page Refactoring — IN PROGRESS / NEARLY COMPLETE
*Extracting raw WordPress body HTML, stripping Elementor div-soup, and refactoring into clean, single-file static HTML documents styled with Tailwind CSS.*

*   **COMPLETE `index.html`:** Clean homepage static markup and navigation synced.
*   **COMPLETE `amenities.html`:** Refactored with 12 amenity cards and responsive Tailwind layout.
*   **COMPLETE `rates.html`:** Refactored with actual rates from `Rates.md` (Standard & RenFest tables, restrictions, cancellation rules).
*   **COMPLETE `directions.html`:** Refactored with Google Maps embed, distance cards, and location details.
*   **COMPLETE `privacy-policy.html`:** Refactored to match exact wording of `privacy-policy.md` (including SMS Communication opt-out text).
*   **COMPLETE `policies.html`:** Refactored to match exact text & section ordering of `policies.md` (Check-In, Check-Out, General Conduct, Noise, Vehicles, Site Setup, Site Appearance, Safety, Fires, Pets, Wifi, Payments, Electric Utility, Background Check, Right to Terminate, Cancellation Policy, and Terms 1–17).
*   **RESUME HERE `site-types.html`:** Needs raw WP HTML content review/refactoring into clean Tailwind static markup to complete the page refactoring phase.
*   ** RENFEST, any other pages :**.

---

## Phase 3: Deploy to Staging (`staging.nobleforestrv.com`) — COMPLETE
*Deploy the current static build to the live staging environment to review in a real browser context before final audits and production launch.*

*   **COMPLETE 1. Staging Domain & CNAME Configuration:** Verify `CNAME` is set to `staging.nobleforestrv.com` in project root.
*   **COMPLETE 2. Git Commit & Push:** Ensure all current static HTML files, CSS, assets, and documentation are committed and pushed to `origin/main` on GitHub (`https://github.com/kyleclosner/wwwnfrv`).
*   **COMPLETE 3. GitHub Pages / Staging Host Verification:** Confirm GitHub Pages deployment builds successfully from the repository and custom domain SSL certificate is active.
*   **COMPLETE 4. Live Staging Smoke Test:**
    *   Verify all page routes resolve live (`/`, `/amenities.html`, `/rates.html`, `/directions.html`, `/policies.html`, `/privacy-policy.html`, `/site-types.html`).
    *   Verify responsive navigation (mobile menu hamburger toggle & desktop nav).
    *   Verify external links (Firefly reservation portal opening with `target="_blank"`).
    *   Verify Google Maps embed and asset loading.

---

## Phase 4: Context Loading & Stack Definition — COMPLETE
*Using Tailwind CSS via `<script>` CDN config with custom theme extensions, Google Fonts, and standard HTML5 semantic architecture.*

*   **COMPLETE Stack Definition:** Single-file static HTML documents with no PHP, database, or WordPress dependencies.
*   **COMPLETE Cross-Page Link Synchronization:** All header nav dropdowns and footer links point directly to `.html` static paths (`amenities.html`, `rates.html`, `directions.html`, `privacy-policy.html`, `policies.html`, `site-types.html`).

---

## Phase 5: Verification, Asset Audit & Cleanup — NEXT STEPS
*Ensuring all assets, local image paths, and routing perform flawlessly.*

*   **1. Refactor `site-types.html` (If needed):** Finalize any remaining content or styling adjustments on `site-types.html`.
*   **2. Audit External Image Dependencies:** Replace any remaining remote WordPress image URLs (`https://nobleforestrv.com/wp-content/uploads/...`) with optimized local asset paths in `/assets/`.
*   **3. Local & Staging Cross-Browser Verification:** Test across desktop/mobile viewports to verify visual perfection.
*   **4. Final Code Review:** Ensure all HTML files validate cleanly and all navigation states (`aria-current="page"`) are correctly applied per page.

---

## Phase 6: Production Deployment & Cutover
*Prepare for final production release.*

*   **1. Final Production Sign-off:** Complete audit of staging site.
*   **2. Domain Cutover:** Point production domain (`nobleforestrv.com`) to hosting target / update DNS and CNAME records.
*   **3. Post-Launch Verification:** Verify SSL, booking funnel, and redirects from old WordPress URLs.