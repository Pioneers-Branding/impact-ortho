import os
import sys

# Ensure the current directory is in the path to import data
sys.path.append(os.getcwd())

try:
    from data.districts import DISTRICTS
except ImportError:
    print("Error: Could not import DISTRICTS from data/districts.py")
    sys.exit(1)

def generate_district_pages():
    generated_total = 0
    
    # Iterate through each state in the data
    for state, districts in DISTRICTS.items():
        state_slug = state.lower().replace(" ", "-")
        state_filename = f"orthopedic-doctor-in-{state_slug}.php"
        
        # Check if state file exists
        if not os.path.exists(state_filename):
            print(f"Skipping {state}: {state_filename} not found.")
            continue
            
        print(f"Processing state: {state}...")
        
        with open(state_filename, 'r') as f:
            state_content = f.read()

        state_generated_files = []

        for district in districts:
            district_slug = district.lower().replace(" ", "-")
            district_filename = f"orthopedic-doctor-in-{district_slug}.php"
            
            # Create district content from state content
            # We replace "State" with "District, State" or just "District" where appropriate
            
            new_content = state_content
            
            # 1. Title Tag
            # Original: Best Orthopedic Doctor in Maharashtra | Top Orthopedic Surgeon Maharashtra - Dr. Ratnakar Rao
            # Target: Best Orthopedic Doctor in Pune, Maharashtra | Top Orthopedic Surgeon Pune - Dr. Ratnakar Rao
            
            # Helper to replace "State" with "District"
            # We need to be careful. The state file already has {location} = {State} hardcoded in many places.
            # So we are replacing "Maharashtra" with "Pune, Maharashtra" or just "Pune" depending on context.
            
            # Strategy: Replace the specific State Name string with the District Name
            # But we should ideally include state name for context, e.g. "Pune, Maharashtra"
            
            # Replace: "in Maharashtra" -> "in Pune, Maharashtra"
            new_content = new_content.replace(f"in {state}", f"in {district}, {state}")
            
            # Replace: "Surgeon Maharashtra" -> "Surgeon Pune"
            new_content = new_content.replace(f"Surgeon {state}", f"Surgeon {district}")
            
            # Replace: "specialist Maharashtra" -> "specialist Pune"
            new_content = new_content.replace(f"specialist {state}", f"specialist {district}")
            
            # Replace: "surgery Maharashtra" -> "surgery Pune"
            new_content = new_content.replace(f"surgery {state}", f"surgery {district}")
            
            # Replace: "cost Maharashtra" -> "cost Pune" (likely "cost of knee replacement in Maharashtra")
            new_content = new_content.replace(f"cost {state}", f"cost {district}")
            new_content = new_content.replace(f"replacement in {state}", f"replacement in {district}")
            
            # Replace: "hospital in Maharashtra" -> "hospital in Pune"
            new_content = new_content.replace(f"hospital in {state}", f"hospital in {district}")
            
            # Meta Tags & Open Graph
            # "Dr. Ratnakar Rao is a top orthopedic surgeon in Maharashtra" -> "... in Pune, Maharashtra"
            # This is covered by "in {state}" -> "in {district}, {state}" usually.
            
            # Canonical URL
            # href=".../orthopedic-doctor-in-maharashtra.php" -> ".../orthopedic-doctor-in-pune.php"
            new_content = new_content.replace(state_filename, district_filename)
            
            # Geo Tags (City Name Update)
            # <meta name="geo.placename" content="Hyderabad" /> -> This was hardcoded in India/State page template 
            # In generated state pages, it might still optionally be Hyderabad or the State capital if we didn't change it.
            # Let's update it to District name.
             # Note: In the state generation script, we didn't explicitly change geo.placename from "Hyderabad" except via broad replacement if it matched.
             # existing content has: <meta name="geo.placename" content="Hyderabad" />
            new_content = new_content.replace('content="Hyderabad"', f'content="{district}"')
            new_content = new_content.replace('content="India"', f'content="{district}, India"')
            
            # Schema
            # "addressRegion": "Telangana" -> Might remain state
            # "addressLocality": "Hyderabad" -> Change to District
            new_content = new_content.replace('"addressLocality": "Hyderabad"', f'"addressLocality": "{district}"')
            
            # H1: Best Orthopedic Doctor in Pune, Maharashtra | ...
            # Covered by "in {state}" replacement
            
            # Why Choose Maharashtra -> Why Choose Pune
            # Covered by "Choose {state}" -> "Choose {district}, {state}" replacement
            new_content = new_content.replace(f"Choose <span class=\"text-[#1E97D9]\">{state}</span>", f"Choose <span class=\"text-[#1E97D9]\">{district}</span>")
            
            # Fix any double state issues if "in {state}" pattern appeared inside previously replaced strings?
            # e.g. if we had "in Maharashtra" -> "in Pune, Maharashtra". 
            # If we had "Best Orthopedic Doctor in Maharashtra", it becomes "Best Orthopedic Doctor in Pune, Maharashtra". Correct.
            
            # Remove the State Links component from the bottom and replace with District Links for this state?
            # Or keep State links? The user said "link them with state page".
            # Usually district pages link back to State page or main page.
            # But here we want to generate district pages.
            
            # Remove the include line for "components/state-doctor-links.php" to avoid clutter?
            # Or keep it? The User didn't specify for district pages.
            # The User said: "link them with state page". This implies:
            # 1. State page links to District pages.
            # 2. District page might link back.
            
            # Let's replace the State Links component with a "Nearby Districts" or just keep it.
            # For now, let's keep the content focus on the district.
            
            with open(district_filename, 'w') as f:
                f.write(new_content)
            
            state_generated_files.append((district, district_filename))
            generated_total += 1
            
        # Create District Links Component for this State
        generate_district_links_component(state, state_generated_files)
        
        # Link this component in the State Page
        link_districts_in_state_page(state_filename, state_slug)

    print(f"Total district pages generated: {generated_total}")

def generate_district_links_component(state, files_list):
    state_slug = state.lower().replace(" ", "-")
    component_filename = f"components/districts-{state_slug}.php"
    
    component_content = f"""
<section class="bg-white py-10 border-t border-gray-200">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex flex-col md:flex-row justify-between items-center mb-6 border-b border-gray-100 pb-4">
            <h3 class="text-gray-800 text-lg font-bold mb-4 md:mb-0 flex items-center">
                <i data-feather="map" class="w-4 h-4 mr-2 text-blue-500"></i>
                Find Top Orthopedic Doctors in {state} Districts
            </h3>
            
            <button id="districtToggle-{state_slug}" class="flex items-center space-x-2 text-gray-600 hover:text-blue-600 px-4 py-2 rounded-lg text-sm font-medium transition-all duration-300 bg-gray-50 hover:bg-gray-100">
                <span>Show Districts</span>
                <i data-feather="chevron-down" id="districtToggleIcon-{state_slug}" class="w-4 h-4 transition-transform duration-300"></i>
            </button>
        </div>
        
        <div id="districtGrid-{state_slug}" class="hidden transition-all duration-500 opacity-0 transform translate-y-4">
            <ul class="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-5 gap-4">
"""
    
    files_list.sort(key=lambda x: x[0])

    for loc, fname in files_list:
        link_html = f'                <li class="mb-2"><a href="{fname}" class="text-gray-500 hover:text-blue-600 text-xs transition-colors flex items-center"><i data-feather="arrow-right" class="w-3 h-3 mr-1 text-gray-300"></i>Orthopedic Doctor in {loc}</a></li>\n'
        component_content += link_html

    component_content += f"""            </ul>
        </div>
    </div>
    
    <script>
        document.addEventListener('DOMContentLoaded', function() {{
            const toggle = document.getElementById('districtToggle-{state_slug}');
            const grid = document.getElementById('districtGrid-{state_slug}');
            const icon = document.getElementById('districtToggleIcon-{state_slug}');
            const buttonText = toggle.querySelector('span');
            
            if(toggle && grid && icon) {{
                toggle.addEventListener('click', () => {{
                    grid.classList.toggle('hidden');
                    
                    if (!grid.classList.contains('hidden')) {{
                        setTimeout(() => {{
                            grid.classList.remove('opacity-0', 'translate-y-4');
                        }}, 10);
                        buttonText.textContent = "Hide Districts";
                        icon.style.transform = "rotate(180deg)";
                    }} else {{
                        grid.classList.add('opacity-0', 'translate-y-4');
                        buttonText.textContent = "Show Districts";
                        icon.style.transform = "rotate(0deg)";
                    }}
                }});
            }}
        }});
    </script>
</section>
"""
    
    with open(component_filename, 'w') as f:
        f.write(component_content)
    print(f"Generated component: {component_filename}")

def link_districts_in_state_page(state_filename, state_slug):
    component_include = f'<?php include "components/districts-{state_slug}.php"; ?>'
    
    with open(state_filename, 'r') as f:
        content = f.read()
    
    # Avoid duplicate includes
    if component_include in content:
        return
        
    # Add before footer
    # We look for "<!-- Footer -->" or "<?php include \"components/footer.php\"; ?>"
    
    target_str = '<?php include "components/footer.php"; ?>'
    
    if target_str in content:
        new_content = content.replace(target_str, f"{component_include}\n\n    {target_str}")
        with open(state_filename, 'w') as f:
            f.write(new_content)
        print(f"Linked districts in {state_filename}")
    else:
        print(f"Warning: Could not link districts in {state_filename} - Footer not found.")

if __name__ == "__main__":
    generate_district_pages()
