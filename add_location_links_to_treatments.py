#!/usr/bin/env python3
"""
Script to add location links components to all main treatment pages
"""

import os
import re

# Treatment files that need location links added
treatments = [
    "knee-replacement.php",
    "total-knee-replacement.php",
    "total-hip-replacement.php",
    "shoulder-replacement.php",
    "knee-pain.php",
    "back-pain.php",
    "shoulder-pain.php",
    "elbow-pain.php",
    "neck-pain.php",
    "foot-ankle-pain.php",
    "hand-wrist-pain.php",
    "arthritis.php",
    "osteoporosis.php",
    "avascular-necrosis.php",
    "meniscus-tear.php",
    "rotator-cuff-tear.php",
    "tennis-elbow.php",
    "shoulder-impingement.php",
    "arthroscopy.php",
    "trauma-surgery.php",
    "physiotherapy-rehabilitation.php",
]

def add_location_links_to_treatment(filename):
    """Add location links component to a treatment page before the footer"""
    
    if not os.path.exists(filename):
        print(f"   ⚠️  File not found: {filename}")
        return False
    
    # Read the file
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Get treatment slug (remove .php extension)
    treatment_slug = filename.replace('.php', '')
    component_include = f'<?php include "components/{treatment_slug}-location-links.php"; ?>'
    
    # Check if already added
    if component_include in content:
        print(f"   ℹ️  Location links already added to {filename}")
        return False
    
    # Find the footer include and add location links before it
    footer_pattern = r'(\s*<?php include "components/footer\.php"; \?>)'
    
    if re.search(footer_pattern, content):
        # Add location links before footer
        replacement = f'\n    {component_include}\n\n    <?php include "components/footer.php"; ?>'
        new_content = re.sub(footer_pattern, replacement, content)
        
        # Write back to file
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"   ✓ Added location links to {filename}")
        return True
    else:
        print(f"   ⚠️  Could not find footer include in {filename}")
        return False

def main():
    print("=" * 80)
    print("ADDING LOCATION LINKS TO MAIN TREATMENT PAGES")
    print("=" * 80)
    
    success_count = 0
    skip_count = 0
    error_count = 0
    
    for treatment_file in treatments:
        print(f"\n📄 Processing: {treatment_file}")
        result = add_location_links_to_treatment(treatment_file)
        
        if result:
            success_count += 1
        elif result is False and "already added" in str(result):
            skip_count += 1
        else:
            error_count += 1
    
    print("\n" + "=" * 80)
    print(f"✅ UPDATE COMPLETE!")
    print(f"   Successfully Updated: {success_count}")
    print(f"   Already Had Links: {skip_count}")
    print(f"   Errors: {error_count}")
    print("=" * 80)

if __name__ == "__main__":
    main()
