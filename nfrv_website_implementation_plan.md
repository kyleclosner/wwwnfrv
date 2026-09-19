# Website Migration & Refactoring Implementation Plan
**Project:** Exact clone of current WordPress site into modern, static code architecture.
**Goal:** Pixel-perfect recreation utilizing clean HTML/CSS and established design tokens, stripping away all WordPress bloat.

---

## Phase 1: Foundation (Finalizing the Rulebooks)
*Before the AI can enforce your brand and architecture, we must define the rules. The provided markdown templates act as the "governing law" for this project, but they must be filled out with your specific data first.*

*   **Complete `template_visual_style_guide.md` & `template_design-guidelines.md`:** Fill in your exact hex codes, CSS custom property names (e.g., `--color-primary`), typography scale, font families, and interaction rules. This ensures the AI uses your actual CSS variables rather than guessing.
*   **Complete `template_content-strategy.md`:** Define your exact brand tone, required terminology, and messaging hierarchy. This ensures the AI doesn't accidentally change your brand voice while refactoring structural HTML.
*   **Complete `template_site-architecture.md`:** Map out exactly how the new file tree should look (e.g., `/about/index.html`) so the AI knows how to structure navigation links and folder directories.

## Phase 2: Source Extraction (The Blueprint)
*We cannot rely on an AI to guess the exact padding, margins, and flex behaviors of the current site. We must pull the raw materials directly from the live site.*

*   **Scrape the DOM:** Open the live WordPress site in your browser, inspect the page, and copy the raw HTML of the `<body>` element for each core page. Save these as raw text/html files.
*   **Extract Assets:** Download all images, SVGs, logos, and brand assets currently hosted in the `wp-content/uploads` folders.
*   **Capture Computed Styles:** Save the core CSS files from the live site, or use a browser extension to rip the computed CSS to reference exact spacing, grid, and layout math.

## Phase 3: Context Loading in the IDE
*Set up the workspace and load the AI context so it understands both the destination architecture and the brand standards.*

*   **Feed the Rulebooks:** Load your four **completed** markdown templates into the AI context window. This sets the strict parameters for naming conventions, semantic HTML guidelines, and vocabulary constraints.
*   **Define the Stack:** Instruct the AI that the target output is strictly modern HTML and CSS (or your chosen static site generator framework), completely decoupling the site from PHP, database queries, and WordPress dependencies.

## Phase 4: AI-Assisted Component Refactoring
*Instead of asking the AI to build the site from scratch, we use it as a high-speed refactoring engine.*

*   **Block-by-Block Processing:** Feed the AI the messy, div-heavy WordPress HTML sections one at a time (e.g., the Hero section first, then the features grid, then the Footer).
*   **Apply Design Guidelines:** Command the AI to rewrite the HTML block using semantic tags (like `<nav>`, `<main>`, `<section>`) and apply the exact CSS custom properties defined in your Design Guidelines document.
*   **Strip the Bloat:** Prompt the AI to strip out all `wp-` specific classes, plugin-generated inline styles, and unnecessary nested divs. The output must be a lean, modern HTML structure that maps perfectly to your new CSS variables while looking visually identical to the source.

## Phase 5: Asset & Route Mapping
*With the clean HTML and CSS generated, finalize the architecture and file structures.*

*   **Local Image Routing:** Update all `<img>` and `<picture>` tags to point to your new local asset directories (e.g., `/assets/images/`) rather than the old WordPress URLs.
*   **Page Structuring:** Organize the generated files according to the hierarchy mapped out in your Site Architecture document, ensuring all internal links are properly routed.

## Phase 6: Version Control & Deployment
*Finalize the code and push to a modern hosting environment.*

*   **Git Initialization:** Commit the clean, static files to your repository.
*   **Testing:** Verify responsiveness, accessibility scores, and console errors across all generated pages.
*   **Hosting:** Push the repository to a modern static hosting environment (e.g., GitHub Pages, Netlify, Vercel), ensuring rapid load times, zero database vulnerabilities, and a secure infrastructure.