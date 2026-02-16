import xml.etree.ElementTree as ET
from datetime import date

# All Indian States and Union Territories
states = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", 
    "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", 
    "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", 
    "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", 
    "Uttarakhand", "West Bengal", "Delhi", "Jammu and Kashmir", "Ladakh", "Chandigarh", 
    "Puducherry", "Lakshadweep", "Andaman and Nicobar Islands", "Dadra and Nagar Haveli and Daman and Diu"
]

def create_slug(text):
    return text.lower().replace(" ", "-").replace("&", "and")

def update_sitemap():
    # Parse existing sitemap
    tree = ET.parse('sitemap.xml')
    root = tree.getroot()
    
    # Get namespace
    ns = {'sm': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    
    # Get today's date
    today = date.today().isoformat()
    
    # Check existing URLs to avoid duplicates
    existing_urls = set()
    for url_elem in root.findall('sm:url', ns):
        loc = url_elem.find('sm:loc', ns)
        if loc is not None:
            existing_urls.add(loc.text)
    
    # Add new robotic knee replacement pages
    added_count = 0
    for state in states:
        slug = create_slug(state)
        url = f"https://www.impactorthocenter.com/robotic-knee-replacement-in-{slug}.php"
        
        # Skip if already exists
        if url in existing_urls:
            print(f"Skipping (already exists): {url}")
            continue
        
        # Create new URL element
        url_elem = ET.SubElement(root, 'url')
        
        loc = ET.SubElement(url_elem, 'loc')
        loc.text = url
        
        lastmod = ET.SubElement(url_elem, 'lastmod')
        lastmod.text = today
        
        changefreq = ET.SubElement(url_elem, 'changefreq')
        changefreq.text = 'weekly'
        
        priority = ET.SubElement(url_elem, 'priority')
        priority.text = '0.8'
        
        added_count += 1
        print(f"✓ Added: {url}")
    
    # Write updated sitemap
    tree.write('sitemap.xml', encoding='UTF-8', xml_declaration=True)
    
    print(f"\n✅ Sitemap updated successfully!")
    print(f"Added {added_count} new robotic knee replacement pages")

if __name__ == "__main__":
    update_sitemap()
