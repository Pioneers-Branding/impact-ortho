#!/usr/bin/env python3
"""
Script to fix stray '<?' tags left by the previous update
"""

import os
import re

def fix_file(filename):
    """Remove stray <? tags before the patient services include"""
    
    if not os.path.exists(filename):
        return False
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Pattern: <? followed by whitespace/newline followed by <?php include "components/patient-services-cta.php"
        # We want to remove the <? and the whitespace
        
        # Look for literal <? followed by whitespace and then the include
        # using re.DOTALL to match across newlines
        pattern = r'<\?\s+(<\?php include "components/patient-services-cta\.php"; \?>)'
        
        if re.search(pattern, content):
            # Replace with just the include
            # We capture the correct include part in group 1
            new_content = re.sub(pattern, r'\1', content)
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            return True
        elif '<?' in content and 'patient-services-cta' in content:
             # Fallback check: look for specific string sequence if regex fails (e.g. indentation diff)
             # "<?\n    <?php"
             fixed = False
             if '<?\n    <?php include "components/patient-services-cta.php"; ?>' in content:
                 content = content.replace('<?\n    <?php include "components/patient-services-cta.php"; ?>', '<?php include "components/patient-services-cta.php"; ?>')
                 fixed = True
             elif '<?\n<?php include "components/patient-services-cta.php"; ?>' in content:
                 content = content.replace('<?\n<?php include "components/patient-services-cta.php"; ?>', '<?php include "components/patient-services-cta.php"; ?>')
                 fixed = True
                 
             if fixed:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(content)
                return True
                
        return False
            
    except Exception as e:
        print(f"   ⚠️  Error fixing {filename}: {e}")
        return False

def main():
    print("=" * 80)
    print("FIXING STRAY PHP TAGS")
    print("=" * 80)
    
    # Get all PHP files in current directory
    all_files = [f for f in os.listdir('.') if f.endswith('.php')]
    
    # Filter for location pages 
    location_pages = [f for f in all_files if '-in-' in f]
    
    print(f"\nScanning {len(location_pages)} location pages...")
    
    fixed_count = 0
    
    for filename in sorted(location_pages):
        if fix_file(filename):
            fixed_count += 1
            if fixed_count % 50 == 0:
                print(f"   ✓ Fixed {fixed_count} pages...")
    
    print("\n" + "=" * 80)
    print(f"✅ FIX COMPLETE!")
    print(f"   Fixed Files: {fixed_count}")
    print("=" * 80)

if __name__ == "__main__":
    main()
