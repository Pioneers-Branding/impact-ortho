#!/usr/bin/env python3
"""
Script to add Patient Services CTA to all location pages before the footer
"""

import os
import re

def add_patient_cta_to_file(filename):
    """Add patient services CTA component to a file before the footer"""
    
    if not os.path.exists(filename):
        return False
    
    try:
        # Read the file
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Component to add
        cta_include = '<?php include "components/patient-services-cta.php"; ?>'
        
        # Check if already added
        if cta_include in content:
            return False
        
        # Find the footer include
        # We want to add it BEFORE the footer, but typically AFTER the location links
        # The location pages usually have:
        # include location-links
        # include footer
        
        # Let's look for the footer include
        footer_pattern = r'(\s*<?php include "components/footer\.php"; \?>)'
        
        if re.search(footer_pattern, content):
            # Check if there is a location links include right before footer
            # If so, we might want to put it before or after that?
            # User said "bfre footr", usually location links are also before footer.
            # Let's inspect a file to see where valid placement is.
            # Typically structure:
            # Main Content
            # Location Links
            # Footer
            #
            # If I insert before footer, it will be:
            # Main Content
            # Location Links
            # Patient CTA
            # Footer
            #
            # This seems correct for "before footer".
            
            replacement = f'\n    {cta_include}\n\n    <?php include "components/footer.php"; ?>'
            new_content = re.sub(footer_pattern, replacement, content)
            
            # Write back to file
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            return True
        else:
            print(f"   ⚠️  Could not find footer include in {filename}")
            return False
            
    except Exception as e:
        print(f"   ⚠️  Error updating {filename}: {e}")
        return False

def main():
    print("=" * 80)
    print("ADDING PATIENT SERVICES CTA TO LOCATION PAGES")
    print("=" * 80)
    
    # Get all PHP files in current directory
    all_files = [f for f in os.listdir('.') if f.endswith('.php')]
    
    # Filter for location pages (contain '-in-' in filename)
    # This covers both robotic-knee and all other treatments
    location_pages = [f for f in all_files if '-in-' in f]
    
    print(f"\nFound {len(location_pages)} location pages to update")
    
    success_count = 0
    skip_count = 0
    error_count = 0
    
    for filename in sorted(location_pages):
        result = add_patient_cta_to_file(filename)
        
        if result:
            success_count += 1
            if success_count % 50 == 0:
                print(f"   ✓ Updated {success_count} pages...")
        elif result is False and "Could not find" in str(result):
             error_count += 1
        else:
            skip_count += 1
    
    print("\n" + "=" * 80)
    print(f"✅ UPDATE COMPLETE!")
    print(f"   Successfully Updated: {success_count}")
    print(f"   Skipped (already present): {skip_count}")
    print(f"   Errors/Not found: {error_count}")
    print(f"   Total Files Processed: {len(location_pages)}")
    print("=" * 80)

if __name__ == "__main__":
    main()
