import os
import re

states = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", 
    "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", 
    "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", 
    "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", 
    "Uttarakhand", "West Bengal", "Delhi", "Jammu and Kashmir", "Ladakh", "Chandigarh", 
    "Puducherry", "Hyderabad"
]

hyderabad_areas = [
    "Banjara Hills", "Jubilee Hills", "Gachibowli", "HITECH City", "Madhapur", 
    "Kondapur", "Manikonda", "Kukatpally", "Miyapur", "Ameerpet", "Begumpet", 
    "Dilsukhnagar", "LB Nagar", "Uppal", "Secunderabad", "Attapur", "Tolichowki", 
    "Nizampet", "ECIL", "Kompally"
]

def create_slug(text):
    return text.lower().replace(" ", "-")

def prepare_content(template, location_name, is_hyderabad_context=False):
    content = template
    
    # Replace Title
    content = re.sub(
        r'<title>.*?</title>', 
        f'<title>Best Orthopedic Hospital in {location_name} | Impact Ortho Centre</title>', 
        content
    )
    
    # Replace Meta Description
    content = re.sub(
        r'<meta name="description"\s+content=".*?" />',
        f'<meta name="description" content="Looking for the Best Orthopedic Hospital in {location_name}? Impact Ortho Centre in Hyderabad provides world-class robotic joint replacement for patients from {location_name}." />',
        content,
        flags=re.DOTALL
    )
    
    # Replace Keywords
    content = re.sub(
        r'<meta name="keywords"\s+content=".*?" />',
        f'<meta name="keywords" content="best orthopedic hospital in {location_name.lower()}, orthopedic surgeon for {location_name.lower()} patients, knee replacement {location_name.lower()}, hip replacement {location_name.lower()}" />',
        content,
        flags=re.DOTALL
    )
    
    # Replace H1
    content = content.replace("Leading Orthopedic Hospital in India", f"Best Orthopedic Hospital in {location_name}")
    
    # Replace Hero Text
    content = content.replace(
        "recognised as one of the Best Orthopedic Hospitals in India", 
        f"chosen by hundreds of patients from {location_name} as the Best Orthopedic Hospital"
    )
    
    if is_hyderabad_context:
        # Add Hyderabad links before Location Links
        content = content.replace(
            '<?php include "components/location-links.php"; ?>', 
            '<?php include "components/hyderabad-links.php"; ?>\n    <?php include "components/location-links.php"; ?>'
        )
        
    return content

def generate_links_component(links_html, filename, title_text, component_id):
    links_section = f"""
<section class="bg-gray-900 py-10 border-t border-gray-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex flex-col md:flex-row justify-between items-center mb-10 border-b border-gray-800 pb-6">
            <h3 class="text-white text-xl font-bold mb-4 md:mb-0 flex items-center">
                <i data-feather="map-pin" class="w-5 h-5 mr-2 text-blue-500"></i>
                {title_text}
            </h3>
            
            <button id="{component_id}Toggle" class="flex items-center space-x-2 bg-white/10 hover:bg-white/20 text-white px-6 py-2 rounded-full text-sm font-medium transition-all duration-300 backdrop-blur-sm border border-white/10">
                <span>Show Locations</span>
                <i data-feather="chevron-down" id="{component_id}ToggleIcon" class="w-4 h-4 transition-transform duration-300"></i>
            </button>
        </div>
        
        <div id="{component_id}Grid" class="hidden transition-all duration-500 opacity-0 transform translate-y-4">
            <ul class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-x-8 gap-y-2">
                {''.join(links_html)}
            </ul>
        </div>
    </div>
    
    <script>
        document.addEventListener('DOMContentLoaded', function() {{
            const toggle = document.getElementById('{component_id}Toggle');
            const grid = document.getElementById('{component_id}Grid');
            const icon = document.getElementById('{component_id}ToggleIcon');
            const buttonText = toggle.querySelector('span');
            
            if(toggle && grid && icon) {{
                toggle.addEventListener('click', () => {{
                    grid.classList.toggle('hidden');
                    
                    if (!grid.classList.contains('hidden')) {{
                        setTimeout(() => {{
                            grid.classList.remove('opacity-0', 'translate-y-4');
                        }}, 10);
                        buttonText.textContent = "Hide Locations";
                        icon.style.transform = "rotate(180deg)";
                    }} else {{
                        grid.classList.add('opacity-0', 'translate-y-4');
                        buttonText.textContent = "Show Locations";
                        icon.style.transform = "rotate(0deg)";
                    }}
                }});
            }}
        }});
    </script>
</section>
"""
    output_dir = "components"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    with open(f"{output_dir}/{filename}", "w", encoding="utf-8") as f:
        f.write(links_section)
    print(f"Generated {filename}")

def generate_pages():
    with open("index.php", "r", encoding="utf-8") as f:
        template = f.read()

    # 1. Generate State Pages
    state_links_html = []
    for state in states:
        slug = create_slug(state)
        filename = f"best-orthopedic-hospital-in-{slug}.php"
        
        # Check if this is Hyderabad page
        is_hyd = (state == "Hyderabad")
        content = prepare_content(template, state, is_hyderabad_context=is_hyd)
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Generated {filename}")
        
        state_links_html.append(f'<li class="mb-2"><a href="{filename}" class="text-gray-400 hover:text-white text-sm transition-colors text-left flex items-start"><i data-feather="map-pin" class="w-3 h-3 mt-1 mr-2 text-blue-500 flex-shrink-0"></i><span>Best Orthopedic Hospital in {state}</span></a></li>')

    # 2. Generate Hyderabad Area Pages
    hyd_links_html = []
    for area in hyderabad_areas:
        slug = create_slug(area)
        filename = f"best-orthopedic-hospital-in-{slug}.php"
        
        content = prepare_content(template, area, is_hyderabad_context=True)
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Generated {filename}")
        
        hyd_links_html.append(f'<li class="mb-2"><a href="{filename}" class="text-gray-400 hover:text-white text-sm transition-colors text-left flex items-start"><i data-feather="map-pin" class="w-3 h-3 mt-1 mr-2 text-blue-500 flex-shrink-0"></i><span>Best Orthopedic Hospital in {area}</span></a></li>')

    # 3. Generate Link Components
    generate_links_component(
        state_links_html, 
        "location-links.php", 
        "Serving Patients Across India", 
        "location"
    )
    
    generate_links_component(
        hyd_links_html, 
        "hyderabad-links.php", 
        "Serving Patients in Hyderabad", 
        "hydLocation"
    )

if __name__ == "__main__":
    generate_pages()
