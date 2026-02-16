#!/usr/bin/env python3
"""
Script to reorder footer components across all PHP pages.
Target Order:
1. Patient Services CTA (if present)
2. Location Links (if present)
3. Footer
"""

import os
import re

def reorder_components(filename):
    """Reorder CTA and Location Links components in the file"""
    
    if not os.path.exists(filename):
        return False
        
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        original_content = content
        
        # Regex patterns for the components
        # Correctly escaped <?php: r'<\?php'
        cta_pattern = r'<\?php\s+include\s+["\']components/patient-services-cta\.php["\'];\s*\?>'
        footer_pattern = r'<\?php\s+include\s+["\']components/footer\.php["\'];\s*\?>'
        
        # Location links can be variable (knee-pain-location-links.php, location-links.php, etc.)
        loc_links_pattern = r'<\?php\s+include\s+["\']components/.*location-links\.php["\'];\s*\?>'
        
        # Check if file has footer
        if not re.search(footer_pattern, content):
            return False
            
        # Find all occurrences
        ctas = list(re.finditer(cta_pattern, content))
        loc_links = list(re.finditer(loc_links_pattern, content))
        footer = list(re.finditer(footer_pattern, content))
        
        if not footer:
            return False
            
        # If no CTA and no Location Links, nothing to do
        if not ctas and not loc_links:
            return False
            
        new_content = content
        
        # Extract and remove CTA
        extracted_cta = ""
        if ctas:
            extracted_cta = ctas[0].group(0) # Assume one CTA
            new_content = re.sub(cta_pattern, '', new_content)
            
        # Extract and remove Location Links
        extracted_loc_link = ""
        if loc_links:
            # We need to capture the SPECIFIC string matched, because .* matches greedily?
            # cta_pattern is specific. loc_links_pattern has .*
            # If multiple location links exist, we might have issues.
            # But usually one.
            extracted_loc_link = loc_links[0].group(0) 
            new_content = re.sub(loc_links_pattern, '', new_content)
            
        # Clean up double newlines/spaces might be nice but let's be safe first.
        # Removing the tags might leave blank lines.
        # We can try to clean up blank lines later if needed.
        
        # Find footer again in new_content
        footer_match_new = re.search(footer_pattern, new_content)
        if not footer_match_new:
            # Just in case our sub removed it (unlikely)
            print(f"   ⚠️  Footer lost in {filename}?")
            return False
            
        footer_start = footer_match_new.start()
        
        # Construct insertion block
        insertion = ""
        if extracted_cta:
            insertion += extracted_cta + "\n\n    "
        if extracted_loc_link:
            insertion += extracted_loc_link + "\n\n    "
            
        # Insert
        final_content = new_content[:footer_start] + insertion + new_content[footer_start:]
        
        if final_content != original_content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(final_content)
            return True
            
        return False
            
    except Exception as e:
        print(f"   ⚠️  Error updating {filename}: {e}")
        return False

def main():
    print("=" * 80)
    print("REORDERING FOOTER COMPONENTS (Attempt 2)")
    print("Order: CTA -> Location Links -> Footer")
    print("=" * 80)
    
    # Get all PHP files
    all_files = [f for f in os.listdir('.') if f.endswith('.php')]
    
    print(f"\nScanning {len(all_files)} files...")
    
    updated_count = 0
    
    for filename in sorted(all_files):
        # Skip component files themselves
        if filename.startswith('components/'): 
            continue
            
        if reorder_components(filename):
            print(f"   ✓ Reordered {filename}")
            updated_count += 1
            
    print("\n" + "=" * 80)
    print(f"✅ REORDER COMPLETE!")
    print(f"   Updated Files: {updated_count}")
    print("=" * 80)

if __name__ == "__main__":
    main()
