# Noble Forest RV Village — Visual Style Guide

*Last updated: 2026-09-19 | Version 1.1*

## Emotional Thesis

The visual experience of Noble Forest RV Village must instantly communicate a grounded, safe, and deeply shaded sanctuary. Before reading a single word, the visitor should feel a sense of relief—like pulling off a busy highway into a peaceful, highly organized forest retreat. The visual system balances the organic, rustic charm of the East Texas outdoors with the ultra-clean, reliable functionality of a premium, modern RV resort. Every design decision must support this feeling of "clean, comfortable nature."

## The World This Product Lives In

The visual environment draws directly from the **East Texas Piney Woods, modern RV living, and the vibrant local culture of the Texas Renaissance Festival.**

This world contains:

* **Mature Shade Trees** — evokes comfort, protection, and a deep connection to nature.
* **Level Concrete Pads** — evokes cleanliness, premium infrastructure, and hassle-free setup.
* **Dappled Sunlight** — evokes warmth, safety, and a pleasant daytime atmosphere.
* **Tidy Utilities (Power pedestals, clean water lines)** — evokes reliability and modern convenience.
* **Families and Costumed RenFest Goers** — evokes a welcoming, fun, and inclusive community spirit.

The emotional register is **refreshing and secure**, not *rugged, messy, or chaotic*.

## Global Color System (Elementor Master Tokens)

The following hex codes are pulled directly from the source of truth (Elementor Global Settings) and must be strictly adhered to as CSS custom properties on `:root`.

### System Colors
| Token / Name | Hex Code | Role |
| :--- | :--- | :--- |
| `--color-primary` | `#48751F` | Deep forest green. Anchors the site; used for the header, structural blocks, and primary brand accents. |
| `--color-secondary` | `#F3F5F8` | Soft fog / off-white. Provides visual separation for alternating sections (like amenities or reviews) without darkening the page. |
| `--color-body-text` | `#B37822` | Golden earth tone. Used for specific sub-headings, contextual highlights, and warm text accents. |
| `--color-accent` | `#D2963E` | Warm oak / amber. Action-oriented; used for highly visible call-to-action buttons (e.g., "Book Online"). |

### Custom Colors
| Token / Name | Hex Code | Role |
| :--- | :--- | :--- |
| `--color-gold-accent` | `#F5C23F` | Bright gold accent. Used for secondary highlights or star ratings in review blocks. |
| `--color-green-text` | `#024600` | Dark pine text. High-contrast typography for green text on light backgrounds. |
| `--color-grey-accent` | `#F3F3F3` | Light neutral grey for subtle UI borders or inactive states. |
| `--color-grey-bg` | `#E9E9E9` | Mid-grey background for structure or shaded card components. |
| `--color-bg-kit` (White Element) | `#FFFFFF` | Pure white. Used for crisp backgrounds, premium card surfaces, and absolute cleanliness. |
| `--color-overlay-bg` | `#000000CC` | 80% opacity black. Used for dimming backgrounds behind modals or enhancing text legibility over hero images. |

## Lighting

**Primary light:** High-contrast daytime natural light, specifically filtered through heavy tree canopies (dappled sunlight). Photography should feel like a bright, clear afternoon.

**Secondary light:** Warm, inviting evening campfires or glowing RV porch lights to communicate safety and coziness at night.

**Avoid:**
* Overcast, gloomy, or heavily shadowed photography that feels unsafe or cold.
* Artificial, blown-out studio lighting.
* High-saturation HDR filters that make the environment look fake or overly processed.

**In practice:**
* Backgrounds utilize crisp whites (`#FFFFFF`) and soft fog (`#F3F5F8`) to reflect the brightness of the outdoor lighting.
* The amber accent color (`#D2963E`) directly mimics the warmth of a campfire or sunset, contrasting against the natural greens.

## Photography Direction

### What to show
* **Subject matter:** Real RVs parked on actual concrete pads, showcasing the massive shade trees. Real guests (like the RenFest family photo) enjoying the space.
* **Photographic style:** Candid, authentic, and well-lit. Shot from human-eye level or slight elevation.
* **Lighting quality:** Bright, sunny, outdoor natural light.
* **Representation:** Families, couples, solo travelers, and pets. A mix of large Fifth Wheels, motorhomes, and tents to show capacity.

### What to avoid
* **Stock photography:** Absolutely no generic stock photos of RVs in the mountains or fake models.
* **Empty dirt lots:** Avoid showing unfinished or messy areas of the park.
* **Overcrowding:** Do not use photos that make the park look cramped or chaotic.

### Technical specs
* **Hero Images:** 16:9 landscape, high-resolution. Must use `--color-overlay-bg` (or a lighter transparency variant) if necessary to allow white hero text to remain legible.
* **Cards/Grids:** 4:3 or 1:1 aspect ratio, consistent rounded corners (`border-radius: 12px`).

## Illustration & Iconography Direction

**Style reference:** Clean, modern, flat-vector iconography.

**Characteristics:**
* **Line and shape quality:** Solid fills or thick, uniform stroke weights. Friendly, slightly rounded terminals.
* **Color approach:** Monochromatic. Icons should be drawn in `--color-primary` (`#48751F`) or `--color-accent` (`#D2963E`).
* **Complexity level:** Highly simplified silhouettes (e.g., a simple Wi-Fi symbol, a basic tent shape, a clear pet silhouette).

## Typography in Context

### Display Font — The Welcoming Authority
*(Based on global font system visually matching geometric sans-serifs like Montserrat/Poppins)*

**Feels like:** Clean, modern, and highly legible, much like premium national park signage.
**Used for:** Hero headlines, major section headers (H1, H2).
**Rules:**
* Minimum size: 32px (Desktop), 24px (Mobile).
* Weight: Bold (700) or Semi-Bold (600).
* High contrast only (White on photos, Dark Green/Charcoal on light backgrounds).

### Body Font — The Workhorse
*(Highly readable sans-serif like Inter, Roboto, or Open Sans)*

**Feels like:** Straightforward, transparent, and easy to read.
**Used for:** Paragraphs, rate grids, policy lists, reviews.
**Rules:**
* Primary body size: 16px to 18px for maximum legibility by older demographics.
* Minimum size: 14px (fine print only).
* Weight: Regular (400) and Medium (500).

## UI Surface Materials

**Primary Cards (Site Types, Reviews):**
Clean white cardstock (`#FFFFFF`). Substantial but friendly. Features a subtle, diffuse drop shadow (`rgba(0,0,0,0.08)`) and rounded corners (`12px`). Hovering feels like sliding the card slightly toward the user.

**Section Dividers (The Organic Wave):**
Rather than harsh, straight horizontal lines separating sections, use the soft, organic SVG wave borders. This mimics rolling hills, alternating between `--color-bg-kit` (`#FFFFFF`) and `--color-secondary` (`#F3F5F8`), reinforcing the "nature/forest" aesthetic while remaining modern.

**Data Tables (Rates):**
High-contrast, alternating row colors (zebra striping using `#F3F3F3` or `#E9E9E9`) for extreme readability. The header row acts as a solid, structural green beam (`#48751F`) holding the data together.

## What This Product Is Not

**Not a rugged, primitive campground.**
*Visually:* We never show muddy sites, chaotic fire pits, or unkempt grounds. We emphasize concrete, clean hookups, and neat landscaping.

**Not a sterile parking lot.**
*Visually:* We never show vast expanses of uninterrupted concrete. Every visual must include the canopy of our mature shade trees or green grass.

**Not a noisy party spot.**
*Visually:* The layout and spacing must feel breathable and quiet. Generous padding and margins between UI elements reflect the physical space between the RV sites.