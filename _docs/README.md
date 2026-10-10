# Noble Forest RV Website Documentation

This folder contains the core architectural rulebooks, design specifications, and implementation guidelines for the Noble Forest RV Village website rebuild.

---

## 🚀 Quick Copy-Paste Developer & Content Workflow

Use these commands in order whenever making updates to the website:

### Step 1: If Updating Header or Footer Navigation
Edit [`_includes/header.html`](../_includes/header.html) or [`_includes/footer.html`](../_includes/footer.html), then run the sync script to automatically update all 10 site pages:
```bash
python3 scripts/sync_components.py
```
*(Note: Navigation components are synchronized at editing/build time. Individual HTML pages should never have their header or footer edited directly.)*

### Step 2: Preview the Site Locally
Launch a local web server to review your changes in the browser:
```bash
python3 -m http.server 8000
```
Open **[http://localhost:8000](http://localhost:8000)** in your browser. Press `Ctrl+C` in your terminal when done.

### Step 3: Check Git Status & Stage Changes
```bash
# 1. Review modified files
git status

# 2. Stage all updated files
git add .
```

### Step 4: Commit and Push to Deploy
```bash
# 3. Commit with a concise summary
git commit -m "Update navigation and header links"

# 4. Push to GitHub (triggers automated deployment to Bluehost)
git push origin main
```

> **Helpful Tip:** After running `git push origin main`, visit [https://staging.nobleforestrv.com](https://staging.nobleforestrv.com) (or your production URL) to see the live updates!

---

## 📚 Core Project Documentation Guide

Here is what each key markdown file in this folder governs:

### 1. [`content-strategy.md`](./content-strategy.md)
* **Purpose:** The brand voice, copy standards, and messaging rules for the park.
* **Key Content:**
  * Defines the brand tone: **"Protective, transparent, and hospitably Texan."**
  * Strict vocabulary rules (e.g., words to avoid like "trailer park" or "campsite" vs. preferred terms like "RV village", "guests", and "residents").
  * Rules for external booking links: all reservation buttons must link to the Firefly portal with `target="_blank"`.

---

### 2. [`design-guidelines.md`](./design-guidelines.md)
* **Purpose:** Structural and frontend code best practices.
* **Key Content:**
  * Semantic HTML requirements: Strict enforcement of `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, and `<footer>` tags (no meaningless Elementor `<div>` soup).
  * Accessibility (a11y) rules: Minimum 44x44px touch targets, visible focus rings (`focus-visible`), and logical heading hierarchies (`h1` through `h4`).
  * Mobile-first responsive layout patterns using clean Tailwind CSS flexbox and grid.

---

### 3. [`implementation_plan.md`](./implementation_plan.md)
* **Purpose:** The step-by-step master roadmap tracking the website migration.
* **Key Content:**
  * Tracks progress through all project phases:
    * **Phase 1:** Foundation & Rulebooks (Complete)
    * **Phase 2:** Source extraction from WordPress & clean HTML refactoring (Nearly complete)
    * **Phase 3:** Deploy to Staging (`staging.nobleforestrv.com`)
    * **Phase 4:** Stack definition & cross-page link synchronization
    * **Phase 5:** Verification, asset localization, and responsive testing
    * **Phase 6:** Production cutover (`nobleforestrv.com`)

---

### 4. [`site-architecture.md`](./site-architecture.md)
* **Purpose:** Site blueprint, page routing, and component hierarchy.
* **Key Content:**
  * Maps out all static page routes (`index.html`, `amenities.html`, `rates.html`, `directions.html`, `policies.html`, `privacy-policy.html`, `site-types.html`).
  * Defines reusable component structures: Global Header, Desktop/Mobile navigation dropdowns, and Global Footer.
  * Specifies folder hierarchy for local images and stylesheet assets.

---

### 5. [`visual-style-guide.md`](./visual-style-guide.md)
* **Purpose:** The design system token specifications and aesthetic standards.
* **Key Content:**
  * **Brand Color Palette:** Primary Forest Pine (`#48751F`), Secondary Soft White (`#F3F5F8`), Accent Gold (`#D2963E`), Dark Charcoal (`#1F2937`), and Neutral Slate (`#4B5563`).
  * **Typography:** Montserrat (headings) and Inter (body copy) via Google Fonts.

---

### Additional Content Reference Files in this Folder:
* [`Rates.md`](./Rates.md) — Source of truth for all current daily, weekly, monthly, and RenFest rates.
* [`policies.md`](./policies.md) — Source text for park rules, check-in/out times, and resident guidelines.
* [`privacy-policy.md`](./privacy-policy.md) — Complete privacy and SMS communication compliance policy text.
