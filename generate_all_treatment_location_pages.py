import os
import json
from datetime import date

base_url = "https://www.impactorthocenter.com/"

# All Indian States and Union Territories
states = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", 
    "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", 
    "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", 
    "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", 
    "Uttarakhand", "West Bengal", "Delhi", "Jammu and Kashmir", "Ladakh", "Chandigarh", 
    "Puducherry", "Lakshadweep", "Andaman and Nicobar Islands", "Dadra and Nagar Haveli and Daman and Diu"
]

# Treatment definitions with metadata
treatments = [
    # Joint Replacements
    {"file": "knee-replacement.php", "name": "Knee Replacement", "type": "MedicalProcedure", "procedure_type": "Surgical", "body_part": "Knee"},
    {"file": "total-knee-replacement.php", "name": "Total Knee Replacement", "type": "MedicalProcedure", "procedure_type": "Surgical", "body_part": "Knee"},
    {"file": "total-hip-replacement.php", "name": "Total Hip Replacement", "type": "MedicalProcedure", "procedure_type": "Surgical", "body_part": "Hip"},
    {"file": "shoulder-replacement.php", "name": "Shoulder Replacement", "type": "MedicalProcedure", "procedure_type": "Surgical", "body_part": "Shoulder"},
    
    # Pain Treatments
    {"file": "knee-pain.php", "name": "Knee Pain Treatment", "type": "MedicalTherapy", "procedure_type": "Pain Management", "body_part": "Knee"},
    {"file": "back-pain.php", "name": "Back Pain Treatment", "type": "MedicalTherapy", "procedure_type": "Pain Management", "body_part": "Back"},
    {"file": "shoulder-pain.php", "name": "Shoulder Pain Treatment", "type": "MedicalTherapy", "procedure_type": "Pain Management", "body_part": "Shoulder"},
    {"file": "elbow-pain.php", "name": "Elbow Pain Treatment", "type": "MedicalTherapy", "procedure_type": "Pain Management", "body_part": "Elbow"},
    {"file": "neck-pain.php", "name": "Neck Pain Treatment", "type": "MedicalTherapy", "procedure_type": "Pain Management", "body_part": "Neck"},
    {"file": "foot-ankle-pain.php", "name": "Foot & Ankle Pain Treatment", "type": "MedicalTherapy", "procedure_type": "Pain Management", "body_part": "Foot and Ankle"},
    {"file": "hand-wrist-pain.php", "name": "Hand & Wrist Pain Treatment", "type": "MedicalTherapy", "procedure_type": "Pain Management", "body_part": "Hand and Wrist"},
    
    # Specific Conditions
    {"file": "arthritis.php", "name": "Arthritis Treatment", "type": "MedicalTherapy", "procedure_type": "Disease Management", "body_part": "Joints"},
    {"file": "osteoporosis.php", "name": "Osteoporosis Treatment", "type": "MedicalTherapy", "procedure_type": "Disease Management", "body_part": "Bones"},
    {"file": "avascular-necrosis.php", "name": "Avascular Necrosis Treatment", "type": "MedicalProcedure", "procedure_type": "Surgical", "body_part": "Hip"},
    {"file": "meniscus-tear.php", "name": "Meniscus Tear Treatment", "type": "MedicalProcedure", "procedure_type": "Surgical", "body_part": "Knee"},
    {"file": "rotator-cuff-tear.php", "name": "Rotator Cuff Tear Treatment", "type": "MedicalProcedure", "procedure_type": "Surgical", "body_part": "Shoulder"},
    {"file": "tennis-elbow.php", "name": "Tennis Elbow Treatment", "type": "MedicalTherapy", "procedure_type": "Sports Medicine", "body_part": "Elbow"},
    {"file": "shoulder-impingement.php", "name": "Shoulder Impingement Treatment", "type": "MedicalTherapy", "procedure_type": "Sports Medicine", "body_part": "Shoulder"},
    {"file": "arthroscopy.php", "name": "Arthroscopy", "type": "MedicalProcedure", "procedure_type": "Surgical", "body_part": "Joints"},
    
    # Other Services
    {"file": "trauma-surgery.php", "name": "Trauma Surgery", "type": "MedicalProcedure", "procedure_type": "Surgical", "body_part": "Multiple"},
    {"file": "physiotherapy-rehabilitation.php", "name": "Physiotherapy & Rehabilitation", "type": "MedicalTherapy", "procedure_type": "Physical Therapy", "body_part": "Multiple"},
]

def create_slug(text):
    return text.lower().replace(" ", "-").replace("&", "and")

def get_treatment_slug(treatment_file):
    """Extract treatment slug from filename"""
    return treatment_file.replace(".php", "")

def get_page_content(treatment, state_name):
    """Generate complete page content for a treatment in a specific state"""
    treatment_name = treatment["name"]
    treatment_slug = get_treatment_slug(treatment["file"])
    state_slug = create_slug(state_name)
    
    # Create URL
    page_slug = f"{treatment_slug}-in-{state_slug}"
    canonical_url = f"{base_url}{page_slug}"
    
    # SEO Meta Tags
    title = f"{treatment_name} in {state_name} | Impact Ortho"
    description = f"Expert {treatment_name} in {state_name}. Impact Ortho Centre offers advanced orthopedic care with experienced surgeons. Book consultation today!"
    keywords = f"{treatment_name.lower()} in {state_name.lower()}, best {treatment_name.lower()} {state_name.lower()}, orthopedic specialist {state_name.lower()}"
    
    # Ensure title length < 60 chars
    if len(title) > 60:
        title = f"{treatment_name} in {state_name} | Impact"
    
    # Ensure description length < 155 chars
    if len(description) > 155:
        description = f"Expert {treatment_name} in {state_name}. Advanced orthopedic care at Impact Ortho Centre. Book consultation!"
    
    # Schema Markup
    schema = {
        "@context": "https://schema.org",
        "@type": treatment["type"],
        "name": f"{treatment_name} in {state_name}",
        "description": f"Advanced {treatment_name.lower()} for patients in {state_name} at Impact Ortho Centre, Hyderabad.",
    }
    
    # Add procedure-specific fields
    if treatment["type"] == "MedicalProcedure":
        schema["procedureType"] = treatment["procedure_type"]
    elif treatment["type"] == "MedicalTherapy":
        schema["therapyType"] = treatment["procedure_type"]
    
    # Add body location
    if treatment["body_part"] != "Multiple":
        schema["bodyLocation"] = {
            "@type": "BodyPart",
            "name": treatment["body_part"]
        }
    
    # Add provider information
    schema["provider"] = {
        "@type": "Hospital",
        "name": "Impact Ortho Centre",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "Apollo Hospitals, Rd Number 72, opposite Bharatiya Vidya Bhavan School, Film Nagar",
            "addressLocality": "Hyderabad",
            "addressRegion": "Telangana",
            "postalCode": "500033",
            "addressCountry": "IN"
        },
        "geo": {
            "@type": "GeoCoordinates",
            "latitude": 17.415639,
            "longitude": 78.413217
        },
        "telephone": "+919494559848",
        "areaServed": {
            "@type": "State",
            "name": state_name
        }
    }
    
    if treatment["type"] == "MedicalProcedure":
        schema["medicalSpecialty"] = "Orthopedic Surgery"
    
    schema_json = json.dumps(schema, indent=4)
    
    # Determine appropriate image
    image_name = treatment_slug.replace("-", "-").title().replace(" ", "-")
    image_url = f"https://impactorthocenter.com/photos/{image_name}.webp"
    
    # Full Page Content
    content = f"""<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="icon" type="image/svg+xml" href="https://www.impactorthocenter.com/photos/favicon.png" />
    <title>{title}</title>
    <meta name="description" content="{description}" />
    <meta name="keywords" content="{keywords}" />
    <link rel="canonical" href="{canonical_url}" />
    <meta name="robots" content="index, follow" />

    <!-- Open Graph -->
    <meta property="og:title" content="{title}" />
    <meta property="og:description" content="{description}" />
    <meta property="og:url" content="{canonical_url}" />
    <meta property="og:type" content="website" />
    <meta property="og:image" content="https://impactorthocenter.com/photos/logo-1-impact.webp" />
    <meta property="og:site_name" content="Impact Ortho Centre" />
    <meta property="og:locale" content="en_IN" />

    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:title" content="{title}" />
    <meta name="twitter:description" content="{description}" />
    <meta name="twitter:image" content="https://impactorthocenter.com/photos/logo-1-impact.webp" />

    <!-- Geo Tags -->
    <meta name="geo.region" content="IN-TG" />
    <meta name="geo.placename" content="Hyderabad" />
    <meta name="geo.position" content="17.415639;78.413217" />
    <meta name="ICBM" content="17.415639, 78.413217" />

    <!-- Schema.org -->
    <script type="application/ld+json">
    {schema_json}
    </script>
    
    <?php include "components/header-link.php"; ?>
</head>

<body class="font-sans antialiased text-gray-900 bg-white">
    <?php include "components/header.php"; ?>

    <main class="pt-20">
        <section class="relative bg-gradient-to-br from-blue-50 to-cyan-50 py-10">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
                    <div class="hero-content">
                        <div class="inline-flex items-center px-4 py-2 bg-blue-100 text-blue-800 rounded-full text-sm font-medium mb-6">
                            <i data-feather="activity" class="w-4 h-4 mr-2"></i>
                            Expert Orthopedic Care
                        </div>
                        <h1 class="text-4xl md:text-5xl font-bold text-gray-900 mb-6">
                            {treatment_name} <span class="bg-gradient-to-r from-blue-600 to-cyan-600 bg-clip-text text-transparent">in {state_name}</span>
                        </h1>
                        <p class="text-xl text-gray-700 mb-8 leading-relaxed">
                            Experience world-class orthopedic care at Impact Ortho Centre in Hyderabad. We serve patients from {state_name} with advanced {treatment_name.lower()} solutions, expert surgeons, and comprehensive rehabilitation programs for optimal recovery.
                        </p>
                        <div class="flex flex-col sm:flex-row gap-4">
                            <a href="contact.php" class="inline-flex items-center justify-center px-8 py-4 bg-gradient-to-r from-blue-600 to-cyan-600 text-white font-semibold rounded-xl hover:from-blue-700 hover:to-cyan-700 transition-all duration-300 transform hover:scale-105 shadow-lg">
                                <i data-feather="calendar" class="w-5 h-5 mr-2"></i>
                                Book Free Consultation
                            </a>
                            <button onclick="window.location.href='tel:+919494559848'" class="inline-flex items-center justify-center px-8 py-4 border-2 border-blue-600 text-blue-600 font-semibold rounded-xl hover:bg-blue-600 hover:text-white transition-all duration-300">
                                <i data-feather="phone" class="w-5 h-5 mr-2"></i>
                                Call Now
                            </button>
                        </div>
                    </div>
                    <div class="hero-image relative">
                        <div class="relative rounded-2xl overflow-hidden shadow-2xl">
                            <img src="https://impactorthocenter.com/photos/logo-1-impact.webp" alt="{treatment_name} in {state_name}" class="w-full h-auto object-cover" />
                            <div class="absolute inset-0 bg-gradient-to-t from-black/30 to-transparent"></div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <section class="py-10 bg-white">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="text-center mb-16">
                    <h2 class="text-4xl font-bold text-gray-900 mb-4">Why Choose Impact Ortho Centre for {treatment_name}?</h2>
                    <p class="text-xl text-gray-600 max-w-3xl mx-auto">Serving patients from {state_name} with excellence in orthopedic care</p>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
                    <div class="bg-gradient-to-br from-blue-50 to-cyan-50 rounded-xl p-6 text-center border border-blue-100">
                        <div class="w-16 h-16 bg-gradient-to-r from-blue-500 to-cyan-500 rounded-full flex items-center justify-center mx-auto mb-4">
                            <i data-feather="award" class="w-8 h-8 text-white"></i>
                        </div>
                        <div class="text-3xl font-bold text-blue-600 mb-2">15+</div>
                        <div class="text-gray-700 font-medium">Years Experience</div>
                    </div>
                    <div class="bg-gradient-to-br from-blue-50 to-cyan-50 rounded-xl p-6 text-center border border-blue-100">
                        <div class="w-16 h-16 bg-gradient-to-r from-blue-500 to-cyan-500 rounded-full flex items-center justify-center mx-auto mb-4">
                            <i data-feather="users" class="w-8 h-8 text-white"></i>
                        </div>
                        <div class="text-3xl font-bold text-blue-600 mb-2">10,000+</div>
                        <div class="text-gray-700 font-medium">Successful Treatments</div>
                    </div>
                    <div class="bg-gradient-to-br from-blue-50 to-cyan-50 rounded-xl p-6 text-center border border-blue-100">
                        <div class="w-16 h-16 bg-gradient-to-r from-blue-500 to-cyan-500 rounded-full flex items-center justify-center mx-auto mb-4">
                            <i data-feather="star" class="w-8 h-8 text-white"></i>
                        </div>
                        <div class="text-3xl font-bold text-blue-600 mb-2">98%</div>
                        <div class="text-gray-700 font-medium">Patient Satisfaction</div>
                    </div>
                    <div class="bg-gradient-to-br from-blue-50 to-cyan-50 rounded-xl p-6 text-center border border-blue-100">
                        <div class="w-16 h-16 bg-gradient-to-r from-blue-500 to-cyan-500 rounded-full flex items-center justify-center mx-auto mb-4">
                            <i data-feather="shield" class="w-8 h-8 text-white"></i>
                        </div>
                        <div class="text-3xl font-bold text-blue-600 mb-2">100%</div>
                        <div class="text-gray-700 font-medium">Safety Standards</div>
                    </div>
                </div>
            </div>
        </section>

        <section class="py-10 bg-gradient-to-r from-blue-600 to-cyan-600 text-white">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
                <h2 class="text-4xl font-bold mb-6">Ready to Start Your Treatment Journey?</h2>
                <p class="text-xl mb-8 text-blue-100 max-w-3xl mx-auto">Experience world-class orthopedic care with our internationally trained surgeons. Serving patients from {state_name}.</p>
                <div class="flex flex-col sm:flex-row gap-4 justify-center">
                    <a href="contact.php" class="inline-flex items-center px-8 py-4 bg-white text-blue-600 font-semibold rounded-xl hover:bg-blue-50 transition-all duration-300 transform hover:scale-105 shadow-xl">
                        <i data-feather="calendar" class="w-5 h-5 mr-2"></i>
                        Schedule Consultation
                    </a>
                    <button onclick="window.location.href='tel:+919494559848'" class="inline-flex items-center px-8 py-4 border-2 border-white text-white font-semibold rounded-xl hover:bg-white hover:text-blue-600 transition-all duration-300">
                        <i data-feather="phone" class="w-5 h-5 mr-2"></i>
                        Call Now
                    </button>
                </div>
            </div>
        </section>
    </main>

    <?php include "components/footer.php"; ?>

</body>

</html>"""
    
    return content

def generate_location_links_component(treatment):
    """Generate location links component for a treatment"""
    treatment_name = treatment["name"]
    treatment_slug = get_treatment_slug(treatment["file"])
    component_id = treatment_slug.replace("-", "")
    
    # Generate links HTML
    links_html = []
    for state in states:
        state_slug = create_slug(state)
        page_slug = f"{treatment_slug}-in-{state_slug}.php"
        link_text = f"{treatment_name} in {state}"
        links_html.append(f'<li class="mb-2"><a href="{page_slug}" class="text-gray-400 hover:text-white text-sm transition-colors text-left flex items-start"><i data-feather="map-pin" class="w-3 h-3 mt-1 mr-2 text-blue-500 flex-shrink-0"></i><span>{link_text}</span></a></li>')
    
    component_content = f"""
<section class="bg-gray-900 py-10 border-t border-gray-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex flex-col md:flex-row justify-between items-center mb-10 border-b border-gray-800 pb-6">
            <h3 class="text-white text-xl font-bold mb-4 md:mb-0 flex items-center">
                <i data-feather="map-pin" class="w-5 h-5 mr-2 text-blue-500"></i>
                {treatment_name} Across India
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
    
    return component_content

def generate_all_pages():
    """Generate all location pages for all treatments"""
    total_pages = 0
    total_components = 0
    
    print("=" * 80)
    print("GENERATING LOCATION PAGES FOR ALL TREATMENTS")
    print("=" * 80)
    
    for treatment in treatments:
        treatment_name = treatment["name"]
        treatment_slug = get_treatment_slug(treatment["file"])
        
        print(f"\n📄 Processing: {treatment_name}")
        print(f"   File: {treatment['file']}")
        print(f"   Type: {treatment['type']} ({treatment['procedure_type']})")
        
        # Generate location pages for this treatment
        pages_generated = 0
        for state in states:
            state_slug = create_slug(state)
            filename = f"{treatment_slug}-in-{state_slug}.php"
            content = get_page_content(treatment, state)
            
            with open(filename, "w", encoding="utf-8") as f:
                f.write(content)
            
            pages_generated += 1
        
        print(f"   ✓ Generated {pages_generated} location pages")
        total_pages += pages_generated
        
        # Generate location links component
        component_filename = f"components/{treatment_slug}-location-links.php"
        component_content = generate_location_links_component(treatment)
        
        with open(component_filename, "w", encoding="utf-8") as f:
            f.write(component_content)
        
        print(f"   ✓ Created component: {component_filename}")
        total_components += 1
    
    print("\n" + "=" * 80)
    print(f"✅ GENERATION COMPLETE!")
    print(f"   Total Pages Generated: {total_pages}")
    print(f"   Total Components Created: {total_components}")
    print(f"   Treatments Processed: {len(treatments)}")
    print("=" * 80)
    print("\nNext steps:")
    print("1. Add location links components to main treatment pages")
    print("2. Update sitemap.xml with all new pages")
    print("3. Test sample pages on localhost")

if __name__ == "__main__":
    generate_all_pages()
