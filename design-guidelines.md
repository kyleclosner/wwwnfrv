# Noble Forest RV Village — Design Guidelines

*Last updated: June 2026 | Version 1.1*
*Companion document to: Elementor Global Theme & Component Styles*

---

## Purpose of This Document

This document defines the implementation standards for developers and layout assistants building on top of the Noble Forest brand. It governs layout mechanics, accessibility, user interaction behaviors, and the design rules that keep the digital property matching the real-world experience.

---

## Interaction Principles

* **Booking Redirection Model:** Clicking any core "Check Availability" or "Book Now" CTA must open the Firefly Reservations interface (`https://app.fireflyreservations.com/reserve/property/NobleForestRV`) in a clean, new browser tab (`target="_blank"`).
* **Rate Layout Logic:** Site-type cards must cleanly toggle or clearly present the flat "All-Bills-Included" distinction side-by-side with covered dimensions (40'x20') so users don't look for utility dropdown maps or hidden calculators.

---

## Elementor Implementation & CSS Standards

* **Layout Engine:** Use Elementor Flexbox Containers exclusively. Avoid legacy section/column wrappers to minimize DOM depth.
* **Responsive Breakpoints:** * Desktop: 1025px and up.
    * Tablet: 768px to 1024px.
    * Mobile: 767px and below (optimized heavily for single-column mobile use by contractors on phones or travelers navigating on the road).

---

## Accessibility Audit Checklist

**Visual Layer:**
- [ ] All text elements meet minimum contrast targets (4.5:1 for standard body text; 3:1 for large display elements against off-white background tokens).
- [ ] Structural layout paths clearly call out the presence of nighttime security lighting grids and continuous onsite manager presence using descriptive text elements, not just visual icon indicators.

**Interaction Layer:**
- [ ] Mobile menus are fully toggleable and accessible without touch target overlapping.
- [ ] Minimum touch target size for touchscreens is set strictly to 44px x 44px for navigation links and booking indicators.

---

## Design Review Checklist

Use this checklist before finalizing any newly created Elementor template page:

- [ ] Clear prominence given to the primary pain-point callouts: *All-Bills-Included* and *40'x20' Covered Sites*.
- [ ] Regional workforce destination points (**Navasota, Waller, Tomball**) are visually mapped or listed cleanly on the Directions view.
- [ ] Event targets (**Texas Renaissance Festival, Todd Mission, Magnolia High School**) are visibly represented with clear typography on secondary tracks.
- [ ] Table or card variations detailing pricing blocks drop into clean, scannable vertical arrays on small mobile layouts.
