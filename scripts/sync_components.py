#!/usr/bin/env python3
"""
Noble Forest RV Village - Component Synchronizer
Zero-dependency script to synchronize master header and footer across all HTML pages.
Uses only Python standard library.
"""

import re
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
INCLUDES_DIR = ROOT_DIR / "_includes"
HEADER_TEMPLATE_PATH = INCLUDES_DIR / "header.html"
FOOTER_TEMPLATE_PATH = INCLUDES_DIR / "footer.html"

# Pattern to locate existing header block
HEADER_BLOCK_RE = re.compile(
    r"(<!-- START:HEADER -->.*?<!-- END:HEADER -->|<header\b[^>]*>.*?</header>)",
    re.DOTALL,
)

# Pattern to locate existing footer block (including mobile toggle script)
FOOTER_BLOCK_RE = re.compile(
    r"(<!-- START:FOOTER -->.*?<!-- END:FOOTER -->|<footer\b[^>]*>.*?</footer>(?:\s*<!-- Mobile Navigation Toggle Script -->\s*<script>.*?</script>)?)",
    re.DOTALL,
)


def generate_header(page_filename: str, template: str) -> str:
    """Returns the header with active page styling applied."""
    header = template

    # Desktop active state replacement
    desktop_search = f'class="hover:text-primary transition-colors" data-page="{page_filename}"'
    desktop_active = f'class="text-primary font-semibold transition-colors" aria-current="page" data-page="{page_filename}"'
    header = header.replace(desktop_search, desktop_active)

    # Mobile active state replacement
    mobile_search = f'class="block px-3 py-2 rounded-md font-medium text-gray-700 hover:bg-secondary hover:text-primary" data-page="{page_filename}"'
    mobile_active = f'class="block px-3 py-2 rounded-md font-semibold text-primary bg-secondary" aria-current="page" data-page="{page_filename}"'
    header = header.replace(mobile_search, mobile_active)

    return f"<!-- START:HEADER -->\n{header.strip()}\n<!-- END:HEADER -->"


def generate_footer(template: str) -> str:
    """Returns the footer wrapped in component markers."""
    return f"<!-- START:FOOTER -->\n{template.strip()}\n<!-- END:FOOTER -->"


def sync_file(file_path: Path, header_tmpl: str, footer_tmpl: str) -> bool:
    content = file_path.read_text(encoding="utf-8")
    page_filename = file_path.name

    new_header = generate_header(page_filename, header_tmpl)
    new_footer = generate_footer(footer_tmpl)

    # Replace or insert header
    if HEADER_BLOCK_RE.search(content):
        content, h_count = HEADER_BLOCK_RE.subn(new_header, content, count=1)
    else:
        print(f"  [WARN] No <header> found in {page_filename}")
        h_count = 0

    # Replace or insert footer
    if FOOTER_BLOCK_RE.search(content):
        content, f_count = FOOTER_BLOCK_RE.subn(new_footer, content, count=1)
    else:
        print(f"  [WARN] No <footer> found in {page_filename}")
        f_count = 0

    if h_count and f_count:
        file_path.write_text(content, encoding="utf-8")
        return True
    return False


def main():
    if not HEADER_TEMPLATE_PATH.exists() or not FOOTER_TEMPLATE_PATH.exists():
        print("Error: Component templates missing in _includes/")
        sys.exit(1)

    header_tmpl = HEADER_TEMPLATE_PATH.read_text(encoding="utf-8")
    footer_tmpl = FOOTER_TEMPLATE_PATH.read_text(encoding="utf-8")

    html_files = sorted(ROOT_DIR.glob("*.html"))
    synced_count = 0

    print("Synchronizing components across pages...")
    for f in html_files:
        if sync_file(f, header_tmpl, footer_tmpl):
            print(f"  ✓ Synced {f.name}")
            synced_count += 1
        else:
            print(f"  ✗ Failed to sync {f.name}")

    print(f"\nDone. Successfully synced {synced_count}/{len(html_files)} pages.")


if __name__ == "__main__":
    main()
