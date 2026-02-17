import os
import sys

# Ensure we can import from data directory if needed, but since data is a package (has __init__.py? maybe not), 
# or just a folder. The previous script didn't import districts, it defined locations list inline.
# I will import the districts dict from data/districts.py by adding current dir to path.
sys.path.append(os.getcwd())
from data.districts import DISTRICTS

# Source file
SOURCE_FILE = 'orthopedic-hospital-in-india.php'

# List of locations (States + UTs)
# derived from DISTRICTS keys
LOCATIONS = sorted(list(DISTRICTS.keys()))

def generate_pages():
    try:
        with open(SOURCE_FILE, 'r') as f:
            template_content = f.read()
    except FileNotFoundError:
        print(f"Error: {SOURCE_FILE} not found.")
        return

    generated_files = []

    for location in LOCATIONS:
        slug = location.lower().replace(" ", "-")
        filename = f"orthopedic-hospital-in-{slug}.php"
        
        new_content = template_content
        
        # 1. Title Tag
        new_content = new_content.replace(
            "<title>Best Orthopedic Hospital in India | Top Orthopedic Center - Impact Ortho Centre</title>",
            f"<title>Best Orthopedic Hospital in {location} | Top Orthopedic Center {location} - Impact Ortho Centre</title>"
        )
        
        # 2. Meta Description
        new_content = new_content.replace(
            'content="Looking for the best orthopedic hospital in India?',
            f'content="Looking for the best orthopedic hospital in {location}?'
        )
        
        # 3. Meta Keywords
        new_content = new_content.replace(
            'content="best orthopedic hospital in india, top orthopedic center india, bone hospital india, joint replacement hospital india, orthopedic surgery india, knee replacement cost india, sports injury hospital india, orthopedic hospital in india"',
            f'content="best orthopedic hospital in {location}, top orthopedic center {location}, bone hospital {location}, joint replacement hospital {location}, orthopedic surgery {location}, knee replacement cost {location}, sports injury hospital {location}, orthopedic hospital in {location}"'
        )
        
        # 4. Canonical URL
        new_content = new_content.replace(
            'href="https://www.impactorthocenter.com/orthopedic-hospital-in-india.php"',
            f'href="https://www.impactorthocenter.com/{filename}"'
        )
        
        # 5. OG tags
        new_content = new_content.replace(
            'content="Best Orthopedic Hospital in India | Impact Ortho Centre"',
            f'content="Best Orthopedic Hospital in {location} | Impact Ortho Centre"'
        )
        new_content = new_content.replace(
            'content="Expert orthopedic care at Impact Ortho Centre, one of the best orthopedic hospitals in India.',
            f'content="Expert orthopedic care at Impact Ortho Centre, one of the best orthopedic hospitals in {location}.'
        )
        new_content = new_content.replace(
            'content="https://www.impactorthocenter.com/orthopedic-hospital-in-india.php"',
            f'content="https://www.impactorthocenter.com/{filename}"'
        )

        
        # 6. Twitter Card
        
        # 7. H1 Heading
        new_content = new_content.replace(
            "Best Orthopedic Hospital in India |",
            f"Best Orthopedic Hospital in {location} |"
        )
        
        # 8. Body Content Replacements
        
        # "Seeking the best orthopedic hospital in India?"
        new_content = new_content.replace(
            "Seeking the <strong>best orthopedic hospital in India</strong>?",
            f"Seeking the <strong>best orthopedic hospital in {location}</strong>?"
        )
        
        # "top orthopedic hospitals in India"
        new_content = new_content.replace(
            "top orthopedic hospitals in\n                                    India</strong>",
             f"top orthopedic hospitals in\n                                    {location}</strong>"
        )
        new_content = new_content.replace( # in case of formatting diffs
            "top orthopedic hospitals in India",
            f"top orthopedic hospitals in {location}"
        )

        # "premier bone hospital in India"
        new_content = new_content.replace(
            "premier <strong>bone hospital in India</strong>",
            f"premier <strong>bone hospital in {location}</strong>"
        )
        
         # "best bone hospital in India" (Treatments section)
        new_content = new_content.replace(
            "best bone hospital in India.",
            f"best bone hospital in {location}."
        )

        # "Why Choose India" -> "Why Choose [Location]"? 
        new_content = new_content.replace(
            'Why Choose <span class="text-[#1E97D9]">India</span> for Orthopedic Surgery?',
            f'Why Choose <span class="text-[#1E97D9]">{location}</span> for Orthopedic Surgery?'
        )
        
        # FAQ Content
        # "Who is the best orthopedic hospital in India?"
        new_content = new_content.replace(
            "Who is the best orthopedic hospital in India?",
            f"Who is the best orthopedic hospital in {location}?"
        )
        new_content = new_content.replace(
            "best orthopedic hospitals in\n                            India", # in the answer
            f"best orthopedic hospitals in\n                            {location}"
        )
        new_content = new_content.replace(
             "best orthopedic hospitals in India",
             f"best orthopedic hospitals in {location}"
        )

        # "What is the cost of knee replacement surgery in India?"
        new_content = new_content.replace(
            "What is the cost of knee replacement surgery in\n                            India?",
            f"What is the cost of knee replacement surgery in\n                            {location}?"
        )
        new_content = new_content.replace(
             "cost of knee replacement surgery in India",
             f"cost of knee replacement surgery in {location}"
        )

        new_content = new_content.replace(
            "cost of knee replacement in India", # in the answer
            f"cost of knee replacement in {location}"
        )
        
        # CTA
        new_content = new_content.replace(
            "Best Bone Hospital in India?",
            f"Best Bone Hospital in {location}?"
        )
        
        # Schema ID / URL
        new_content = new_content.replace(
            '"@id": "https://www.impactorthocenter.com/orthopedic-hospital-in-india.php"',
            f'"@id": "https://www.impactorthocenter.com/{filename}"'
        )
        new_content = new_content.replace(
            '"url": "https://www.impactorthocenter.com/orthopedic-hospital-in-india.php"',
            f'"url": "https://www.impactorthocenter.com/{filename}"'
        )

        # Write file
        with open(filename, 'w') as f:
            f.write(new_content)
        
        print(f"Generated: {filename}")
        generated_files.append((location, filename))

    # Now generate the links component
    generate_links_component(generated_files)

def generate_links_component(files_list):
    # files_list is list of (location_name, filename)
    
    component_content = """
<section class="bg-gray-50 py-10 border-t border-gray-200">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex flex-col md:flex-row justify-between items-center mb-10 border-b border-gray-200 pb-6">
            <h3 class="text-gray-900 text-xl font-bold mb-4 md:mb-0 flex items-center">
                <i data-feather="map-pin" class="w-5 h-5 mr-2 text-blue-600"></i>
                Find Top Orthopedic Hospitals in India
            </h3>
            
            <button id="stateLocationToggle" class="flex items-center space-x-2 bg-white text-gray-700 hover:bg-gray-50 px-6 py-2 rounded-full text-sm font-medium transition-all duration-300 border border-gray-200 shadow-sm">
                <span>Show Locations</span>
                <i data-feather="chevron-down" id="stateLocationToggleIcon" class="w-4 h-4 transition-transform duration-300"></i>
            </button>
        </div>
        
        <div id="stateLocationGrid" class="hidden transition-all duration-500 opacity-0 transform translate-y-4">
            <ul class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-x-8 gap-y-2">
"""
    
    # Sort files_list by location name
    files_list.sort(key=lambda x: x[0])

    for loc, fname in files_list:
        link_html = f'                <li class="mb-2"><a href="{fname}" class="text-gray-500 hover:text-blue-600 text-sm transition-colors text-left flex items-start"><i data-feather="map-pin" class="w-3 h-3 mt-1 mr-2 text-blue-400 flex-shrink-0"></i><span>Orthopedic Hospital in {loc}</span></a></li>\n'
        component_content += link_html

    component_content += """            </ul>
        </div>
    </div>
    
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const toggle = document.getElementById('stateLocationToggle');
            const grid = document.getElementById('stateLocationGrid');
            const icon = document.getElementById('stateLocationToggleIcon');
            const buttonText = toggle.querySelector('span');
            
            if(toggle && grid && icon) {
                toggle.addEventListener('click', () => {
                    grid.classList.toggle('hidden');
                    
                    if (!grid.classList.contains('hidden')) {
                        setTimeout(() => {
                            grid.classList.remove('opacity-0', 'translate-y-4');
                        }, 10);
                        buttonText.textContent = "Hide Locations";
                        icon.style.transform = "rotate(180deg)";
                    } else {
                        grid.classList.add('opacity-0', 'translate-y-4');
                        buttonText.textContent = "Show Locations";
                        icon.style.transform = "rotate(0deg)";
                    }
                });
            }
        });
    </script>
</section>
"""
    
    with open('components/state-hospital-links.php', 'w') as f:
        f.write(component_content)
    print("Generated: components/state-hospital-links.php")

if __name__ == "__main__":
    generate_pages()
