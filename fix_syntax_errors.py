#!/usr/bin/env python3
"""
Script to fix syntax errors (stray <? tags) in main treatment pages
"""

import os
import re

def fix_syntax_error(filename):
    """Remove stray <? line before the location links include"""
    
    if not os.path.exists(filename):
        return False
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        new_lines = []
        fixed = False
        
        for i, line in enumerate(lines):
            # Check for stray <? line
            # It seems to be just "    <?" or "    <?\n"
            if line.strip() == '<?':
                # Check if next line is a valid php include
                if i + 1 < len(lines) and '<?php include' in lines[i+1]:
                    # Skip this line (remove it)
                    fixed = True
                    continue
            
            new_lines.append(line)
            
        if fixed:
            with open(filename, 'w', encoding='utf-8') as f:
                f.writelines(new_lines)
            return True
        
        return False
            
    except Exception as e:
        print(f"   ⚠️  Error fixing {filename}: {e}")
        return False

def main():
    print("=" * 80)
    print("FIXING SYNTAX ERRORS IN TREATMENT PAGES")
    print("=" * 80)
    
    # List of files reported with errors
    files_to_fix = [
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
    
    print(f"\nChecking {len(files_to_fix)} files...")
    
    fixed_count = 0
    
    for filename in sorted(files_to_fix):
        if fix_syntax_error(filename):
            print(f"   ✓ Fixed {filename}")
            fixed_count += 1
        else:
            print(f"   - No fix needed/applied for {filename}")
    
    print("\n" + "=" * 80)
    print(f"✅ FIX COMPLETE!")
    print(f"   Fixed Files: {fixed_count}")
    print("=" * 80)

if __name__ == "__main__":
    main()
