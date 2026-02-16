#!/usr/bin/env python3
"""
Script to add Patient Services CTA to main treatment pages
"""

import os

def add_patient_cta(filename):
    """Add patient services CTA before footer if not present"""
    
    if not os.path.exists(filename):
        return False
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if 'patient-services-cta.php' in content:
            return False
            
        # Look for footer include
        footer_tag = '<?php include "components/footer.php"; ?>'
        
        if footer_tag in content:
            # Insert CTA before footer
            cta_tag = '<?php include "components/patient-services-cta.php"; ?>'
            
            # We want to add it with some spacing
            replacement = f'{cta_tag}\n\n    {footer_tag}'
            
            new_content = content.replace(footer_tag, replacement)
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
        else:
            print(f"   ⚠️  Footer not found in {filename}")
            return False
            
    except Exception as e:
        print(f"   ⚠️  Error updating {filename}: {e}")
        return False

def main():
    print("=" * 80)
    print("ADDING PATIENT CTA TO MAIN TREATMENT PAGES")
    print("=" * 80)
    
    files_to_update = [
        "arthritis.php",
        "arthroscopy.php",
        "avascular-necrosis.php",
        "back-pain.php",
        "elbow-pain.php",
        "foot-ankle-pain.php",
        "hand-wrist-pain.php",
        "knee-pain.php",
        "knee-replacement.php",
        "meniscus-tear.php",
        "neck-pain.php",
        "osteoporosis.php",
        "physiotherapy-rehabilitation.php",
        "rotator-cuff-tear.php",
        "shoulder-impingement.php",
        "shoulder-pain.php",
        "shoulder-replacement.php",
        "tennis-elbow.php",
        "total-hip-replacement.php",
        "total-knee-replacement.php",
        "trauma-surgery.php"
    ]
    
    count = 0
    for filename in sorted(files_to_update):
        if add_patient_cta(filename):
            print(f"   ✓ Updated {filename}")
            count += 1
        else:
            print(f"   - Skipped {filename}")
            
    print("\n" + "=" * 80)
    print(f"✅ UPDATE COMPLETE!")
    print(f"   Updated Files: {count}")
    print("=" * 80)

if __name__ == "__main__":
    main()
