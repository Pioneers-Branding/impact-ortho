
<section class="bg-white py-10 border-t border-gray-200">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex flex-col md:flex-row justify-between items-center mb-6 border-b border-gray-100 pb-4">
            <h3 class="text-gray-800 text-lg font-bold mb-4 md:mb-0 flex items-center">
                <i data-feather="map" class="w-4 h-4 mr-2 text-blue-500"></i>
                Find Top Orthopedic Doctors in Delhi Districts
            </h3>
            
            <button id="districtToggle-delhi" class="flex items-center space-x-2 text-gray-600 hover:text-blue-600 px-4 py-2 rounded-lg text-sm font-medium transition-all duration-300 bg-gray-50 hover:bg-gray-100">
                <span>Show Districts</span>
                <i data-feather="chevron-down" id="districtToggleIcon-delhi" class="w-4 h-4 transition-transform duration-300"></i>
            </button>
        </div>
        
        <div id="districtGrid-delhi" class="hidden transition-all duration-500 opacity-0 transform translate-y-4">
            <ul class="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-5 gap-4">
                <li class="mb-2"><a href="orthopedic-doctor-in-central-delhi.php" class="text-gray-500 hover:text-blue-600 text-xs transition-colors flex items-center"><i data-feather="arrow-right" class="w-3 h-3 mr-1 text-gray-300"></i>Orthopedic Doctor in Central Delhi</a></li>
                <li class="mb-2"><a href="orthopedic-doctor-in-east-delhi.php" class="text-gray-500 hover:text-blue-600 text-xs transition-colors flex items-center"><i data-feather="arrow-right" class="w-3 h-3 mr-1 text-gray-300"></i>Orthopedic Doctor in East Delhi</a></li>
                <li class="mb-2"><a href="orthopedic-doctor-in-new-delhi.php" class="text-gray-500 hover:text-blue-600 text-xs transition-colors flex items-center"><i data-feather="arrow-right" class="w-3 h-3 mr-1 text-gray-300"></i>Orthopedic Doctor in New Delhi</a></li>
                <li class="mb-2"><a href="orthopedic-doctor-in-north-delhi.php" class="text-gray-500 hover:text-blue-600 text-xs transition-colors flex items-center"><i data-feather="arrow-right" class="w-3 h-3 mr-1 text-gray-300"></i>Orthopedic Doctor in North Delhi</a></li>
                <li class="mb-2"><a href="orthopedic-doctor-in-north-east-delhi.php" class="text-gray-500 hover:text-blue-600 text-xs transition-colors flex items-center"><i data-feather="arrow-right" class="w-3 h-3 mr-1 text-gray-300"></i>Orthopedic Doctor in North East Delhi</a></li>
                <li class="mb-2"><a href="orthopedic-doctor-in-north-west-delhi.php" class="text-gray-500 hover:text-blue-600 text-xs transition-colors flex items-center"><i data-feather="arrow-right" class="w-3 h-3 mr-1 text-gray-300"></i>Orthopedic Doctor in North West Delhi</a></li>
                <li class="mb-2"><a href="orthopedic-doctor-in-shahdara.php" class="text-gray-500 hover:text-blue-600 text-xs transition-colors flex items-center"><i data-feather="arrow-right" class="w-3 h-3 mr-1 text-gray-300"></i>Orthopedic Doctor in Shahdara</a></li>
                <li class="mb-2"><a href="orthopedic-doctor-in-south-delhi.php" class="text-gray-500 hover:text-blue-600 text-xs transition-colors flex items-center"><i data-feather="arrow-right" class="w-3 h-3 mr-1 text-gray-300"></i>Orthopedic Doctor in South Delhi</a></li>
                <li class="mb-2"><a href="orthopedic-doctor-in-south-east-delhi.php" class="text-gray-500 hover:text-blue-600 text-xs transition-colors flex items-center"><i data-feather="arrow-right" class="w-3 h-3 mr-1 text-gray-300"></i>Orthopedic Doctor in South East Delhi</a></li>
                <li class="mb-2"><a href="orthopedic-doctor-in-south-west-delhi.php" class="text-gray-500 hover:text-blue-600 text-xs transition-colors flex items-center"><i data-feather="arrow-right" class="w-3 h-3 mr-1 text-gray-300"></i>Orthopedic Doctor in South West Delhi</a></li>
                <li class="mb-2"><a href="orthopedic-doctor-in-west-delhi.php" class="text-gray-500 hover:text-blue-600 text-xs transition-colors flex items-center"><i data-feather="arrow-right" class="w-3 h-3 mr-1 text-gray-300"></i>Orthopedic Doctor in West Delhi</a></li>
            </ul>
        </div>
    </div>
    
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const toggle = document.getElementById('districtToggle-delhi');
            const grid = document.getElementById('districtGrid-delhi');
            const icon = document.getElementById('districtToggleIcon-delhi');
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
