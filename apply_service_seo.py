"""
Wire the SEO config into the India-level service pages.

Adds two includes to each configured page:
  * before </head>   -> components/service-schema.php   (JSON-LD @graph)
  * before </main>   -> components/international-patients-block.php

Idempotent: running it twice changes nothing. Both includes read the same
per-slug entry in components/seo-config.php, so all future content changes
happen in that one file rather than in the page files.

Usage:  python apply_service_seo.py [--dry-run]
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent

# Slugs configured in components/seo-config.php.
#
# Deliberately EXCLUDED: total-knee-replacement and hand-and-wrist-pain. Each is
# a near-duplicate of a stronger page (knee-replacement, hand-wrist-pain) with an
# identical <title>. Giving both twins the same block would make two pages
# identical rather than merely similar. Redirect the weaker one, then add its
# slug here only if you decide to keep it.
SLUGS = [
    "arthritis", "arthroscopy", "avascular-necrosis", "back-pain",
    "diagnostic-services", "elbow-pain", "foot-ankle-pain",
    "hand-wrist-pain", "knee-pain", "knee-replacement",
    "meniscus-tear", "neck-pain", "osteoporosis",
    "physiotherapy-rehabilitation", "robotic-knee-replacement",
    "rotator-cuff-tear", "shoulder-impingement", "shoulder-pain",
    "shoulder-replacement", "tennis-elbow", "total-hip-replacement",
    "trauma-surgery",
]

SCHEMA_MARK = "components/service-schema.php"
BLOCK_MARK = "components/international-patients-block.php"

dry = "--dry-run" in sys.argv
changed = skipped = missing = 0

for slug in SLUGS:
    path = ROOT / f"{slug}.php"
    if not path.exists():
        print(f"  MISSING  {slug}.php")
        missing += 1
        continue

    src = path.read_text(encoding="utf-8")

    if SCHEMA_MARK in src and BLOCK_MARK in src:
        print(f"  ok       {slug}.php (already wired)")
        skipped += 1
        continue

    out = src

    # 1. Schema include, immediately before </head>.
    if SCHEMA_MARK not in out:
        schema = (
            f'    <?php $page_slug = "{slug}"; '
            f'include "components/service-schema.php"; ?>\n'
        )
        if not re.search(r"</head>", out, re.I):
            print(f"  FAIL     {slug}.php has no </head>")
            continue
        out = re.sub(r"(?i)([ \t]*)</head>", schema + r"\1</head>", out, count=1)

    # 2. Visible block, immediately before </main>.
    if BLOCK_MARK not in out:
        block = (
            '        <?php include "components/'
            'international-patients-block.php"; ?>\n'
        )
        if not re.search(r"</main>", out, re.I):
            print(f"  FAIL     {slug}.php has no </main>")
            continue
        out = re.sub(r"(?i)([ \t]*)</main>", block + r"\1</main>", out, count=1)

    if out == src:
        skipped += 1
        continue

    if not dry:
        path.write_text(out, encoding="utf-8")
    print(f"  wired    {slug}.php")
    changed += 1

print(f"\n{changed} wired, {skipped} already done, {missing} missing"
      + ("  [DRY RUN, nothing written]" if dry else ""))
