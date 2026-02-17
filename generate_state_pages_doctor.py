import os

# Source file
SOURCE_FILE = 'orthopedic-doctor-in-india.php'

# List of locations (States + UTs + Major Cities if needed)
# Extracted from the user's previous location-links.php and standard Indian states
LOCATIONS = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", 
    "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", 
    "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", 
    "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", 
    "Uttarakhand", "West Bengal", "Delhi", "Jammu and Kashmir", "Ladakh", "Chandigarh", 
    "Puducherry", "Hyderabad"
]

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
        filename = f"orthopedic-doctor-in-{slug}.php"
        
        # Content replacements
        # We need to be careful to replace "India" with "Location" only where appropriate for the requested keywords
        # and context, while keeping the flow natural.
        
        new_content = template_content
        
        # 1. Title Tag
        new_content = new_content.replace(
            "<title>Best Orthopedic Doctor in India | Top Orthopedic Surgeon - Dr. Ratnakar Rao</title>",
            f"<title>Best Orthopedic Doctor in {location} | Top Orthopedic Surgeon {location} - Dr. Ratnakar Rao</title>"
        )
        
        # 2. Meta Description
        new_content = new_content.replace(
            'content="Looking for the best orthopedic doctor in India?',
            f'content="Looking for the best orthopedic doctor in {location}?'
        )
        
        # 3. Meta Keywords (LSI keywords adaptation)
        new_content = new_content.replace(
            'content="best orthopedic doctor in india, top orthopedic surgeon india, bone specialist india, joint replacement surgeon india, orthopedic surgery india, knee replacement cost india, sports injury specialist india, orthopedic hospital in india"',
            f'content="best orthopedic doctor in {location}, top orthopedic surgeon {location}, bone specialist {location}, joint replacement surgeon {location}, orthopedic surgery {location}, knee replacement cost {location}, sports injury specialist {location}, orthopedic hospital in {location}"'
        )
        
        # 4. Canonical URL
        new_content = new_content.replace(
            'href="https://www.impactorthocenter.com/orthopedic-doctor-in-india.php"',
            f'href="https://www.impactorthocenter.com/{filename}"'
        )
        
        # 5. OG tags
        new_content = new_content.replace(
            'content="Best Orthopedic Doctor in India | Dr. Ratnakar Rao"',
            f'content="Best Orthopedic Doctor in {location} | Dr. Ratnakar Rao"'
        )
         # Note: OG Description usually copies meta description or similar.
        new_content = new_content.replace(
             'content="Expert orthopedic care by Dr. Ratnakar Rao, one of the best orthopedic doctors in India.',
             f'content="Expert orthopedic care by Dr. Ratnakar Rao, one of the best orthopedic doctors in {location}.'
        )
        
        new_content = new_content.replace(
            'content="https://www.impactorthocenter.com/orthopedic-doctor-in-india.php"',
            f'content="https://www.impactorthocenter.com/{filename}"'
        )

        
        # 6. Twitter Card
        # Same title/description logic as above usually works if strings match exactly
        
        # 7. H1 Heading
        new_content = new_content.replace(
            "Best Orthopedic Doctor in India |",
            f"Best Orthopedic Doctor in {location} |"
        )
        
        # 8. Body Content Replacements
        # "Seeking the best orthopedic doctor in India?"
        new_content = new_content.replace(
            "Seeking the <strong>best orthopedic doctor in India</strong>?",
            f"Seeking the <strong>best orthopedic doctor in {location}</strong>?"
        )
        
        # "certified bone specialist in India"
        new_content = new_content.replace(
            "certified <strong>bone specialist in India</strong>",
            f"certified <strong>bone specialist in {location}</strong>"
        )
        
        # "best bone specialist in India" (Treatments section)
        new_content = new_content.replace(
            "best bone specialist in India.",
            f"best bone specialist in {location}."
        )

        # "Why Choose India" -> "Why Choose [Location]"? 
        # User asked for "orthopedic doctor + state name".
        # Context: "Why Choose India for Orthopedic Surgery?" -> "Why Choose {location} for Orthopedic Surgery?"
        # Logic: If I am looking for a doctor in Maharashtra, "Why Choose Maharashtra" makes sense.
        new_content = new_content.replace(
            'Why Choose <span class="text-[#1E97D9]">India</span> for Orthopedic Surgery?',
            f'Why Choose <span class="text-[#1E97D9]">{location}</span> for Orthopedic Surgery?'
        )
        
        # FAQ Content
        # "Who is the best orthopedic doctor in India?"
        new_content = new_content.replace(
            "Who is the best orthopedic doctor in India?",
            f"Who is the best orthopedic doctor in {location}?"
        )
        new_content = new_content.replace(
            "best orthopedic doctors in India", # in the answer
            f"best orthopedic doctors in {location}"
        )

        # "What is the cost of knee replacement surgery in India?"
        # Maybe keep India here if it's about cost? Or change to location?
        # User said "want same style". Localizing cost query is good for SEO.
        new_content = new_content.replace(
            "What is the cost of knee replacement surgery in India?",
            f"What is the cost of knee replacement surgery in {location}?"
        )
        new_content = new_content.replace(
            "cost of knee replacement in India", # in the answer
            f"cost of knee replacement in {location}"
        )
        
        # CTA
        new_content = new_content.replace(
            "Best Bone Specialist in India?",
            f"Best Bone Specialist in {location}?"
        )
        
        # Schema ID / URL
        new_content = new_content.replace(
            '"@id": "https://www.impactorthocenter.com/orthopedic-doctor-in-india.php"',
            f'"@id": "https://www.impactorthocenter.com/{filename}"'
        )
        new_content = new_content.replace(
            '"url": "https://www.impactorthocenter.com/orthopedic-doctor-in-india.php"',
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
                Find Top Orthopedic Doctors in India
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
        link_html = f'                <li class="mb-2"><a href="{fname}" class="text-gray-500 hover:text-blue-600 text-sm transition-colors text-left flex items-start"><i data-feather="map-pin" class="w-3 h-3 mt-1 mr-2 text-blue-400 flex-shrink-0"></i><span>Orthopedic Doctor in {loc}</span></a></li>\n'
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
    
    with open('components/state-doctor-links.php', 'w') as f:
        f.write(component_content)
    print("Generated: components/state-doctor-links.php")

if __name__ == "__main__":
    generate_pages()
