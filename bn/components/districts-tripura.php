
<section class="bg-white py-10 border-t border-gray-200">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex flex-col md:flex-row justify-between items-center mb-6 border-b border-gray-100 pb-4">
            <h3 class="text-gray-800 text-lg font-bold mb-4 md:mb-0 flex items-center">
                <i data-feather="map" class="w-4 h-4 mr-2 text-blue-500"></i>
                Find Top Orthopedic Doctors in Tripura Districts
            </h3>
            
            <button id="districtToggle-tripura" class="flex items-center space-x-2 text-gray-600 hover:text-blue-600 px-4 py-2 rounded-lg text-sm font-medium transition-all duration-300 bg-gray-50 hover:bg-gray-100">
                <span>Show Districts</span>
                <i data-feather="chevron-down" id="districtToggleIcon-tripura" class="w-4 h-4 transition-transform duration-300"></i>
            </button>
        </div>
        
        <div id="districtGrid-tripura" class="hidden transition-all duration-500 opacity-0 transform translate-y-4">
            <ul class="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-5 gap-4">
                <li class="mb-2"><a href="orthopedic-doctor-in-dhalai.php" class="text-gray-500 hover:text-blue-600 text-xs transition-colors flex items-center"><i data-feather="arrow-right" class="w-3 h-3 mr-1 text-gray-300"></i>Orthopedic Doctor in Dhalai</a></li>
                <li class="mb-2"><a href="orthopedic-doctor-in-gomati.php" class="text-gray-500 hover:text-blue-600 text-xs transition-colors flex items-center"><i data-feather="arrow-right" class="w-3 h-3 mr-1 text-gray-300"></i>Orthopedic Doctor in Gomati</a></li>
                <li class="mb-2"><a href="orthopedic-doctor-in-khowai.php" class="text-gray-500 hover:text-blue-600 text-xs transition-colors flex items-center"><i data-feather="arrow-right" class="w-3 h-3 mr-1 text-gray-300"></i>Orthopedic Doctor in Khowai</a></li>
                <li class="mb-2"><a href="orthopedic-doctor-in-north-tripura.php" class="text-gray-500 hover:text-blue-600 text-xs transition-colors flex items-center"><i data-feather="arrow-right" class="w-3 h-3 mr-1 text-gray-300"></i>Orthopedic Doctor in North Tripura</a></li>
                <li class="mb-2"><a href="orthopedic-doctor-in-sepahijala.php" class="text-gray-500 hover:text-blue-600 text-xs transition-colors flex items-center"><i data-feather="arrow-right" class="w-3 h-3 mr-1 text-gray-300"></i>Orthopedic Doctor in Sepahijala</a></li>
                <li class="mb-2"><a href="orthopedic-doctor-in-south-tripura.php" class="text-gray-500 hover:text-blue-600 text-xs transition-colors flex items-center"><i data-feather="arrow-right" class="w-3 h-3 mr-1 text-gray-300"></i>Orthopedic Doctor in South Tripura</a></li>
                <li class="mb-2"><a href="orthopedic-doctor-in-unakoti.php" class="text-gray-500 hover:text-blue-600 text-xs transition-colors flex items-center"><i data-feather="arrow-right" class="w-3 h-3 mr-1 text-gray-300"></i>Orthopedic Doctor in Unakoti</a></li>
                <li class="mb-2"><a href="orthopedic-doctor-in-west-tripura.php" class="text-gray-500 hover:text-blue-600 text-xs transition-colors flex items-center"><i data-feather="arrow-right" class="w-3 h-3 mr-1 text-gray-300"></i>Orthopedic Doctor in West Tripura</a></li>
            </ul>
        </div>
    </div>
    
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const toggle = document.getElementById('districtToggle-tripura');
            const grid = document.getElementById('districtGrid-tripura');
            const icon = document.getElementById('districtToggleIcon-tripura');
            const buttonText = toggle.querySelector('span');
            
            if(toggle && grid && icon) {
                toggle.addEventListener('click', () => {
                    grid.classList.toggle('hidden');
                    
                    if (!grid.classList.contains('hidden')) {
                        setTimeout(() => {
                            grid.classList.remove('opacity-0', 'translate-y-4');
                        }, 10);
                        buttonText.textContent = "Hide Districts";
                        icon.style.transform = "rotate(180deg)";
                    } else {
                        grid.classList.add('opacity-0', 'translate-y-4');
                        buttonText.textContent = "Show Districts";
                        icon.style.transform = "rotate(0deg)";
                    }
                });
            }
        });
    </script>
</section>
