#!/usr/bin/env python3
"""
Script to update Dr. Ratnakar Rao's experience from 15+ to 24 years in all location pages
"""

import os
import re

def update_experience_in_file(filename):
    """Update experience from 15+ to 24 in a file"""
    
    if not os.path.exists(filename):
        return False
    
    try:
        # Read the file
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if file contains the experience section
        if '15+' not in content:
            return False
        
        # Replace 15+ with 24
        new_content = content.replace('15+', '24')
        
        # Also update "Years Experience" to "Years of Experience" for better grammar
        new_content = new_content.replace('Years Experience', 'Years of Experience')
        
        # Write back to file
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return True
    except Exception as e:
        print(f"   ⚠️  Error updating {filename}: {e}")
        return False

def main():
    print("=" * 80)
    print("UPDATING DR. RATNAKAR RAO'S EXPERIENCE TO 24 YEARS")
    print("=" * 80)
    
    # Get all PHP files in current directory
    all_files = [f for f in os.listdir('.') if f.endswith('.php')]
    
    # Filter for location pages (contain '-in-' in filename)
    location_pages = [f for f in all_files if '-in-' in f]
    
    print(f"\nFound {len(location_pages)} location pages to update")
    
    success_count = 0
    skip_count = 0
    
    for filename in sorted(location_pages):
        result = update_experience_in_file(filename)
        
        if result:
            success_count += 1
            if success_count % 50 == 0:
                print(f"   ✓ Updated {success_count} pages...")
        else:
            skip_count += 1
    
    print("\n" + "=" * 80)
    print(f"✅ UPDATE COMPLETE!")
    print(f"   Successfully Updated: {success_count}")
    print(f"   Skipped (no changes needed): {skip_count}")
    print(f"   Total Files Processed: {len(location_pages)}")
    print("=" * 80)

if __name__ == "__main__":
    main()
