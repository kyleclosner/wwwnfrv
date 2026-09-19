# Noble Forest RV Village — Site Architecture, Pages & Navigation

**Last updated: 2026-09-19 | Version 2.0 | PLATFORM: Static HTML / CSS**

---

## Visitor Roles

### Primary Visitor: Contractors, Traveling Professionals & Remote Workers

Individuals working on extended construction, utility, or commercial projects in the surrounding regional hubs: **\*\*Navasota, Waller, Tomball, Magnolia, Montgomery, and North Houston, TX\*\***.

 **Behavioral Traits:** They seek an immediate, hassle-free, highly secure residential base. They prioritize peace, strict rule enforcement, and a genuinely quiet environment to rest deeply after long off-site shifts.

**What this means for site structure:** Structural assets (All-Bills-Included, premium concrete pads, 40'x20' structural covers, onsite live-in manager, private walk-in showers, 24/7 laundry) must dominate the home view and structural landing layers.

\ ---

### Secondary Visitors: Campers, RV Travelers & Event Guests

Transient and seasonal visitors traveling for leisure, family events, or major regional attractions.

| Visitor Type | Goal | Priority Pages |

| :--- | :--- | :--- |

| **Texas RenFest Travelers & Vendors** | Demanding absolute geographical convenience, traffic avoidance, and full hookups near the festival gates. | \`/site-types/\`, \`/texas-renaissance-festival/\` |

| **Family & Regional Visitors** | Seeking proximity to Todd Mission, local areas, or events at Magnolia West High School while prioritizing night security and kid activities. | \`/amenities/\`, \`/rv-park-near-montgomery-texas/\` |

---

### Tertiary Visitors: Boat & RV Storage Seekers

Local property owners requiring secure, dedicated, accessible open or specialized storage alternatives.

---

## Site Map

text
├── / (Home)
├── /site-types
├── /amenities
├── /directions
├── /policies
├── /texas-renaissance-festival
└── /rv-park-near-montgomery-texas

(Derived from the visual tree structure applied to the updated URL matrix)

---

## File System & Server Directory Architecture

This section defines the physical repository layout and file-serving architecture, establishing strict separation of concerns between public production assets and internal documentation.

### 1. Directory Tree & Layout Blueprint

```text
nfrv-static-site/                         # Project Root
│
├── _docs/                                # Internal Documentation & Blueprint Rules (DO NOT DEPLOY)
│   ├── content-strategy.md               # Positioning, voice, tone, vocabulary & copy frameworks
│   ├── design-guidelines.md              # Technical interaction rules, accessibility targets & CSS standards
│   ├── implementation_plan.md            # Phase-by-phase migration & refactoring strategy
│   ├── policies.md                       # Canonical source copy for park rules and regulations
│   ├── privacy-policy.md                 # Authoritative source policy (including 10DLC mobile disclosures)
│   ├── Rates.md                          # Flat pricing metrics, all-inclusive terms & unit specs
│   ├── site-architecture.md              # UX, route hierarchy & physical file mapping (This document)
│   └── visual-style-guide.md             # Color tokens, typography roles & aesthetic thesis
│
├── assets/                               # Shared Static Deliverables
│   ├── fonts/                            # Locally hosted WOFF2 web fonts (zero external Google CDN lag)
│   │   ├── inter-v20-latin-*.woff2       # Inter weights (Regular, 500, 600, Italic)
│   │   └── montserrat-v31-latin-*.woff2  # Montserrat display weights (Regular, 600, 700)
│   └── images/                           # High-res photography, maps, logos, and vector iconography
│
├── CNAME                                 # Custom domain mapping configuration (e.g. nobleforestrv.com)
├── styles.css                            # Global CSS custom properties, base reset, and custom utilities
├── wip.txt                               # Temporary scratchpad / staging notes (ignored in production)
│
├── index.html                            # Homepage (Target: /)
├── site-types.html                       # RV Pad Types & Covered Specs (Target: /site-types/)
├── amenities.html                        # Utility & Recreation Facilities (Target: /amenities/)
├── rates.html                            # All-Bills-Included Pricing Grid (Target: /rates/)
├── directions.html                       # Navigation, Map & Regional Routing (Target: /directions/)
├── policies.html                         # Community Rules & Guest Conduct (Target: /policies/)
├── privacy-policy.html                   # Privacy Statement & Mobile Data Protections
├── texas-renaissance-festival.html       # Landing page for Texas RenFest visitors & vendors
└── rv-park-near-montgomery-texas.html    # SEO landing guide for workforce & regional contractors
```

### 2. Architectural Principles & File Rules

1. **Isolation of `_docs/`:**
   * The underscore prefix (`_`) signals that the directory contains metadata, design rules, and planning documents rather than runnable website code.
   * **Deployment Hygiene:** When deploying to production servers or static hosts, exclude the `_docs/` folder (via `.gitignore`, build exclusion, or publish directory settings) so internal strategies and private notes are never exposed via public URLs.

2. **Flat Root HTML Structure for Clean URL Routing:**
   * All primary landing pages live directly in the root directory.
   * Hosting platforms (GitHub Pages, Netlify, Cloudflare Pages, Vercel, or Apache/LiteSpeed via `.htaccess`) rewrite clean paths automatically:
     * `nobleforestrv.com/site-types.html` rewrites to `nobleforestrv.com/site-types`
     * `nobleforestrv.com/amenities.html` rewrites to `nobleforestrv.com/amenities`
   * Internal anchor links across the site should consistently point to clean paths or relative `.html` endpoints as configured by the server.

3. **Asset Referencing Standards:**
   * **Relative Paths:** Internal pages must reference shared assets using relative paths starting from the root or relative position:
     * Fonts: `assets/fonts/montserrat-v31-latin-700.woff2`
     * Images: `assets/images/logo-transparent.png`
     * Global Styles: `<link rel="stylesheet" href="styles.css">`
   * **Self-Contained Font Hosting:** The `assets/fonts/` directory contains self-hosted WOFF2 assets to eliminate third-party render-blocking requests, protect user privacy, and ensure maximum performance.

4. **CNAME & Root Configuration:**
   * The `CNAME` file must exist at the root level containing the primary production domain (`nobleforestrv.com`) for seamless DNS resolution on static hosts.

---

## **Navigation & Architecture Map**

### **Header Navigation Structure**
* **Logo** (Links back to / Home)
* **Site Types & Rates** (/site-types/)
* **Amenities** (/amenities/)
* **Directions & Local Area** (/directions/)
* **Park Policies** (/policies/)
* **\[CTA Button\]: Book Now** (External Link to Firefly Reservation engine)

### **Mobile Navigation**

Hamburger menu condensing the primary header links. The "BOOK NOW" and call buttons should remain persistent or highly visible at the top of the menu.

### **4-Column Footer Navigation Structure**

#### **Column 1: Logo & Bio**

* **Visual Asset:** Primary Brand Logo.  
* **Core Bio Text:** "Noble Forest RV Village is a premium, family-owned and operated gated RV community. We provide an ultra-safe, quiet, and deeply shaded sanctuary featuring all-bills-included pricing, level concrete pads, protective covered structures, and an onsite live-in manager."  
* 

#### **Column 2: Useful Links**

(Note for developer: Do not include a "Home" link in the footer grid. Ensure links utilize clean lowercase CSS targets).

* **Site Types & Rates** \-\> links to /site-types/  
* **Amenities** \-\> links to /amenities/  
* **Campground Site Map** \-\> links to /directions/  
* **Policies** \-\> links to /policies/  

#### **Column 3: Social & Areas We Serve**

* **Social Container:** Dynamic high-contrast icon links for Facebook, Instagram, and direct email connection.  
* **Areas We Serve Directory:**  
  * **Texas Renaissance Festival** \-\> links to /texas-renaissance-festival/  
  * **Montgomery, TX Guide** \-\> links to /rv-park-near-montgomery-texas/  

#### **Column 4: Address & Map**

* **Physical Location Details:** 22833 FM 1774, Plantersville, TX 77363  
* **Communication Anchor:** Phone/Text: (936) 894-2079  
* **Visual Element:** Clean, responsive Google Maps or high-contrast static orientation viewport mapping the entrance off FM 1774\.  

## **Page Purposes**

| Page Title | Target URL Slug | Component/Layout Strategy | Single-Sentence Purpose |
| :---- | :---- | :---- | :---- |
| **Home Page** | / | Hero section highlighting 40'x20' covered protection, predictable utility pricing, features block.  | Establish the core brand premium position and immediately address core weather and cost concerns.  |
| **Site Types** | /site-types/ | Structural cards showcasing Covered Sites, Deluxe Patio layouts, Standard pads, and Storage setups.  | Detail dimensions, concrete pad strength specifications, and flat all-inclusive rate grids.  |
| **Amenities** | /amenities/ | Dual-focus grid detailing utilities (1 GB Fiber, laundry) and recreation tracks (dog park, rec room).  | Provide physical proof of long-term convenience and short-term traveler comfort.  |
| **Directions** | /directions/ | Regional route descriptions, localized entry directions, and the main **Campground Site Map** graphic.  | Clear navigational boundaries; map landing anchor for Column 2 footer path.  |
| **Policies** | /policies/ | High-readability typographic breakdown of quiet hours, pet guidelines, and criminal background rules.  | Set mutual expectations for safety and clear community guidelines.\[cite: 6\]  |
| **Texas Renaissance Festival** | /texas-renaissance-festival/ | Specialty high-conversion layout highlighting 1-mile proximity, traffic bypass benefits, and full-hookup availability.\[cite: 6\]  | Target festival attendees, vendors, and seasonal performers looking for premium infrastructure close to the gates.\[cite: 6\]  |
| **RV Park near Montgomery** | /rv-park-near-montgomery-texas/ | Detailed regional guide connecting park features to nearby creature comforts, distances to local Walmarts, and historic centers.\[cite: 6\]  | Capture regional search authority for long-term accommodation seekers.\[cite: 6\]  |

(Derived from the URL Matrix\[cite: 6\] combined with the Page Purposes table structure)

## **Core Visitor Journeys**

### **Journey 1 — The Event Booking Journey**

User searches for premium accommodations near Todd Mission \-\> Lands directly on /texas-renaissance-festival/ \-\> Validates the 1-mile distance metric and private shower assets \-\> Clicks "Book Now".\[cite: 6\] **Success state:** Transfers smoothly to external Firefly execution container to finalize the reservation.

### **Journey 2 — The Logistics Placement Journey**

Contractor checks regional availability near Waller/Navasota \-\> Navigates to /rv-park-near-montgomery-texas/ \-\> Confirms exact mileage vectors to local Walmarts, supply hubs, and restaurants \-\> Validates All-Bills-Included security \-\> Selects site type layout.\[cite: 6\] **Success state:** The visitor contacts the office or books directly to secure a long-term monthly space.

## **Technical Targets, SEO & Meta Structure**

* **Platform Foundation:** Static HTML / CSS.  

| Page | Title Tag Pattern | Meta Description Pattern |
| :---- | :---- | :---- |
| Home | Noble Forest RV Village | Top rated RV Park  | Premium gated RV community in Plantersville, TX.\[cite: 6\] Featuring massive 40'x20' covered sites, clean concrete pads, all-bills-included rates, onsite live-in manager, and clean private showers less than 1 mile from the Texas Renaissance Festival.\[cite: 6\]  |
| Site Types | Rates & Availability | Noble Forest RV Village  | View our competitive nightly, weekly, and monthly rates for concrete pads, covered RV sites, and storage in Plantersville, TX.  |
| \[Page type\] | {Page Title} | Noble Forest RV Village  | \[Page specific summary highlighting structural assets, amenities, and location\] |