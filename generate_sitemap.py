import os
import datetime

base_url = "https://www.impactorthocenter.com/"
today = datetime.date.today().isoformat()

def generate_sitemap():
    # List all .php files in the current directory
    files = [f for f in os.listdir('.') if f.endswith('.php') and os.path.isfile(f)]
    
    # Files to exclude (if any)
    exclude = [] 
    
    sitemap_content = ['<?xml version="1.0" encoding="UTF-8"?>']
    sitemap_content.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
    
    for f in files:
        if f in exclude:
            continue
            
        url = base_url + f
        
        # Set priority based on file name
        priority = "0.8"
        if f == "index.php":
            priority = "1.0"
        elif "best-orthopedic-hospital" in f:
            priority = "0.9"
            
        sitemap_content.append('   <url>')
        sitemap_content.append(f'      <loc>{url}</loc>')
        sitemap_content.append(f'      <lastmod>{today}</lastmod>')
        sitemap_content.append('      <changefreq>weekly</changefreq>')
        sitemap_content.append(f'      <priority>{priority}</priority>')
        sitemap_content.append('   </url>')
        
    sitemap_content.append('</urlset>')
    
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write('\n'.join(sitemap_content))
    
    print(f"Generated sitemap.xml with {len(files)} URLs")

if __name__ == "__main__":
    generate_sitemap()
