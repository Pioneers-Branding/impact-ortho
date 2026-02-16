#!/usr/bin/env python3
"""
Script to update doctor experience to 24 years across all pages
Handles variations like "20+", "20 Years", "24+", etc.
"""

import os
import re

def update_experience(filename):
    """Update experience strings in the file"""
    
    if not os.path.exists(filename):
        return False
        
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        original_content = content
        
        # 1. Update "20+" in stats numbers to "24"
        # <div class="text-5xl font-bold text-blue-500">20+</div>
        content = re.sub(r'>20\s*\+</div>', '>24</div>', content)
        
        # 2. Update "20+" or "20" years text
        content = content.replace('20+ Years', '24 Years')
        content = content.replace('20 Years', '24 Years')
        
        # 3. Update "24+" to "24" (if user specifically wants "24 years")
        # <span class="font-semibold">24+ Years Experience</span>
        content = content.replace('24+ Years Experience', '24 Years Experience')
        
        # 4. Update "20+" in other contexts
        content = content.replace('20+ Years of Excellence', '24 Years of Excellence')
        
        if content != original_content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
            
        return False
            
    except Exception as e:
        print(f"   ⚠️  Error updating {filename}: {e}")
        return False

def main():
    print("=" * 80)
    print("UPDATING DOCTOR EXPERIENCE TO 24 YEARS")
    print("=" * 80)
    
    # Get all PHP files
    all_files = [f for f in os.listdir('.') if f.endswith('.php')]
    
    print(f"\nScanning {len(all_files)} files...")
    
    updated_count = 0
    
    for filename in sorted(all_files):
        if update_experience(filename):
            print(f"   ✓ Updated {filename}")
            updated_count += 1
            
    print("\n" + "=" * 80)
    print(f"✅ UPDATE COMPLETE!")
    print(f"   Updated Files: {updated_count}")
    print("=" * 80)

if __name__ == "__main__":
    main()
