import os
import re

states = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", 
    "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", 
    "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", 
    "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", 
    "Uttarakhand", "West Bengal", "Delhi", "Jammu and Kashmir", "Ladakh", "Chandigarh", 
    "Puducherry"
]

def create_slug(text):
    return text.lower().replace(" ", "-")

def generate_pages():
    with open("index.php", "r", encoding="utf-8") as f:
        template = f.read()

    links_html = []
    
    for state in states:
        slug = create_slug(state)
        filename = f"best-orthopedic-hospital-in-{slug}.php"
        nav_text = f"Best Orthopedic Hospital in {state}"
        
        # Prepare content
        content = template
        
        # Replace Title
        content = re.sub(
            r'<title>.*?</title>', 
            f'<title>Best Orthopedic Hospital in {state} | Impact Ortho Centre</title>', 
            content
        )
        
        # Replace Meta Description
        content = re.sub(
            r'<meta name="description"\s+content=".*?" />',
            f'<meta name="description" content="Looking for the Best Orthopedic Hospital in {state}? Impact Ortho Centre in Hyderabad provides world-class robotic joint replacement for patients from {state}." />',
            content,
            flags=re.DOTALL
        )
        
        # Replace Keywords
        content = re.sub(
            r'<meta name="keywords"\s+content=".*?" />',
            f'<meta name="keywords" content="best orthopedic hospital in {state.lower()}, orthopedic surgeon for {state.lower()} patients, knee replacement {state.lower()}, hip replacement {state.lower()}" />',
            content,
            flags=re.DOTALL
        )
        
        # Replace H1 (Leading Orthopedic Hospital in India)
        # We look for "Leading Orthopedic Hospital in India"
        content = content.replace("Leading Orthopedic Hospital in India", f"Best Orthopedic Hospital in {state}")
        
        # Replace Hero Text
        # "recognized as one of the Best Orthopedic Hospitals in India"
        content = content.replace(
            "recognised as one of the Best Orthopedic Hospitals in India", 
            f"chosen by hundreds of patients from {state} as the Best Orthopedic Hospital"
        )

        # Write file
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
            
        print(f"Generated {filename}")
        
        links_html.append(f'<li class="mb-2"><a href="{filename}" class="text-gray-400 hover:text-white text-sm transition-colors text-left flex items-start"><i data-feather="map-pin" class="w-3 h-3 mt-1 mr-2 text-blue-500 flex-shrink-0"></i><span>Best Orthopedic Hospital in {state}</span></a></li>')

    # Generate location-links.php
    links_section = f"""
<section class="bg-gray-900 py-10 border-t border-gray-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex flex-col md:flex-row justify-between items-center mb-10 border-b border-gray-800 pb-6">
            <h3 class="text-white text-xl font-bold mb-4 md:mb-0 flex items-center">
                <i data-feather="globe" class="w-5 h-5 mr-2 text-blue-500"></i>
                Serving Patients Across India
            </h3>
            
            <button id="locationToggle" class="flex items-center space-x-2 bg-white/10 hover:bg-white/20 text-white px-6 py-2 rounded-full text-sm font-medium transition-all duration-300 backdrop-blur-sm border border-white/10">
                <span>Show Locations</span>
                <i data-feather="chevron-down" id="locationToggleIcon" class="w-4 h-4 transition-transform duration-300"></i>
            </button>
        </div>
        
        <div id="locationGrid" class="hidden transition-all duration-500 opacity-0 transform translate-y-4">
            <ul class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-x-8 gap-y-2">
                {''.join(links_html)}
            </ul>
        </div>
    </div>
    
    <script>
        document.addEventListener('DOMContentLoaded', function() {{
            const toggle = document.getElementById('locationToggle');
            const grid = document.getElementById('locationGrid');
            const icon = document.getElementById('locationToggleIcon');
            const buttonText = toggle.querySelector('span');
            
            toggle.addEventListener('click', () => {{
                grid.classList.toggle('hidden');
                
                // Small delay to allow display:block to apply before opacity transition
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
        }});
    </script>
</section>
"""
    
    output_dir = "components"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    with open(f"{output_dir}/location-links.php", "w", encoding="utf-8") as f:
        f.write(links_section)
    
    print("Generated location-links.php")

if __name__ == "__main__":
    generate_pages()
