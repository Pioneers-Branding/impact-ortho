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
        state_filename = f"orthopedic-hospital-in-{state_slug}.php"
        
        # Check if state file exists
        if not os.path.exists(state_filename):
            print(f"Skipping {state}: {state_filename} not found.")
            # Verify if maybe I need to create it? But I just ran state generation.
            # Maybe the state name in DISTRICTS differs from LOCATIONS in state gen script? 
            # They should be the same as state gen script used DISTRICTS keys.
            continue
            
        print(f"Processing state: {state}...")
        
        with open(state_filename, 'r') as f:
            state_content = f.read()

        state_generated_files = []

        for district in districts:
            district_slug = district.lower().replace(" ", "-")
            district_filename = f"orthopedic-hospital-in-{district_slug}.php"
            
            new_content = state_content
            
            # Replacements
            # "in Maharashtra" -> "in Pune, Maharashtra"
            new_content = new_content.replace(f"in {state}", f"in {district}, {state}")
            
            # "Center Maharashtra" -> "Center Pune"
            new_content = new_content.replace(f"Center {state}", f"Center {district}")
            
            # "Hospital Maharashtra" -> "Hospital Pune"
            new_content = new_content.replace(f"Hospital {state}", f"Hospital {district}")
            
            # "bone hospital Maharashtra" -> "bone hospital Pune"
            new_content = new_content.replace(f"bone hospital {state}", f"bone hospital {district}")

            # "specialist Maharashtra" -> "specialist Pune"
            new_content = new_content.replace(f"specialist {state}", f"specialist {district}")
            
             # "surgery Maharashtra" -> "surgery Pune"
            new_content = new_content.replace(f"surgery {state}", f"surgery {district}")
            
            # "cost Maharashtra" -> "cost Pune"
            new_content = new_content.replace(f"cost {state}", f"cost {district}")
            new_content = new_content.replace(f"replacement in {state}", f"replacement in {district}")
            
             # "hospital in Maharashtra" -> "hospital in Pune" (already covered by first replacement mostly, but good to be safe)
            new_content = new_content.replace(f"hospital in {state}", f"hospital in {district}")

            # Canonical URL
            new_content = new_content.replace(state_filename, district_filename)
            
            # Geo Tags / Address
            # In state pages, we might have had "Hyderabad" or updated to state.
            # Let's replace "Hyderabad" with District if it exists (from template carryover)
            new_content = new_content.replace('content="Hyderabad"', f'content="{district}"')
            new_content = new_content.replace('"addressLocality": "Hyderabad"', f'"addressLocality": "{district}"')
            
            # If state generation updated it to state name unique string?
            # State gen script: 
            # new_content = new_content.replace("Best Orthopedic Hospital in India", "Best ... in Maharashtra")
            # so the content has "Maharashtra".
            
            # Why Choose Maharashtra -> Why Choose Pune
            new_content = new_content.replace(f"Choose <span class=\"text-[#1E97D9]\">{state}</span>", f"Choose <span class=\"text-[#1E97D9]\">{district}</span>")
            
            # Add District Links Component explicitly to District Page
            component_include = f'<?php include "components/hospital-districts-{state_slug}.php"; ?>'
            
            # Start of State Link addition
            state_link_html = f'<div class="text-center mt-4"><a href="{state_filename}" class="text-blue-600 hover:text-blue-800 font-medium no-underline hover:underline transition-all">View All Hospitals in {state} &rarr;</a></div>'
            # End of State Link addition
            
            if component_include not in new_content:
                target_str = '<?php include "components/footer.php"; ?>'
                if target_str in new_content:
                    # Append state link after component include but before footer if needed, or inside component?
                    # Since component is separate file, better to append HTML or modify component generator.
                    # But component is shared across state. State page uses it too.
                    # If I put "Back to State" in component, state page will have "Back to State" link to itself?
                    # So better to add it only in District pages.
                    
                    # Inserting component AND the state link
                    new_content = new_content.replace(target_str, f"{component_include}\n{state_link_html}\n\n    {target_str}")
            else:
                # If component is already there (from previous run), we still want the link?
                # But previous run didn't add the link.
                # So we should force replace component include + link
                 new_content = new_content.replace(component_include, f"{component_include}\n{state_link_html}")

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
    component_filename = f"components/hospital-districts-{state_slug}.php"
    
    component_content = f"""
<section class="bg-white py-10 border-t border-gray-200">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex flex-col md:flex-row justify-between items-center mb-6 border-b border-gray-100 pb-4">
            <h3 class="text-gray-800 text-lg font-bold mb-4 md:mb-0 flex items-center">
                <i data-feather="map" class="w-4 h-4 mr-2 text-blue-500"></i>
                Find Top Orthopedic Hospitals in {state} Districts
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
        link_html = f'                <li class="mb-2"><a href="{fname}" class="text-gray-500 hover:text-blue-600 text-xs transition-colors flex items-center"><i data-feather="arrow-right" class="w-3 h-3 mr-1 text-gray-300"></i>Orthopedic Hospital in {loc}</a></li>\n'
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
    # print(f"Generated component: {component_filename}")

def link_districts_in_state_page(state_filename, state_slug):
    component_include = f'<?php include "components/hospital-districts-{state_slug}.php"; ?>'
    
    with open(state_filename, 'r') as f:
        content = f.read()
    
    # Avoid duplicate includes
    if component_include in content:
        return
        
    # Add before footer
    target_str = '<?php include "components/footer.php"; ?>'
    
    if target_str in content:
        new_content = content.replace(target_str, f"{component_include}\n\n    {target_str}")
        with open(state_filename, 'w') as f:
            f.write(new_content)
        # print(f"Linked districts in {state_filename}")
    else:
        print(f"Warning: Could not link districts in {state_filename} - Footer not found.")

if __name__ == "__main__":
    generate_district_pages()
