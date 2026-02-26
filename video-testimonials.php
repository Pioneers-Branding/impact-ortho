<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="icon" type="image/svg+xml" href="https://www.impactorthocenter.com/photos/favicon.png" />
    <title>Patient Video Testimonials | Impact Ortho Centre Hyderabad</title>
    <meta name="description"



        content="Watch real patient success stories & video testimonials from Impact Ortho Centre. Hear about their recovery from knee replacement, hip surgery & trauma care." />









    
    <link rel="canonical" href="https://www.impactorthocenter.com/video-testimonials.php" />
    <?php include "components/header-link.php"; ?>
</head>

<body class="font-sans antialiased text-gray-900 bg-white">

    <!-- Header -->
    <!-- Header -->
    <?php include "components/header.php"; ?>

    <main class="pt-20">
        <!-- Hero Section -->
        <section class="relative bg-gradient-to-br from-blue-50 to-cyan-50 py-10">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="text-center hero-animate">
                    <div
                        class="inline-flex items-center px-4 py-2 bg-blue-100 text-blue-800 rounded-full text-sm font-medium mb-6">
                        <i data-feather="video" class="w-4 h-4 mr-2"></i>
                        Real Stories, Real People
                    </div>
                    <h1 class="text-4xl md:text-5xl font-bold text-gray-900 mb-6">
                        Patient <span
                            class="bg-gradient-to-r from-blue-600 to-cyan-600 bg-clip-text text-transparent">Video
                            Testimonials</span>
                    </h1>
                    <p class="text-xl text-gray-600 max-w-3xl mx-auto">
                        Hear directly from our patients about their experiences and journeys to recovery with Impact
                        Ortho Centre.
                    </p>
                </div>
            </div>
        </section>

        <!-- Videos Grid -->
        <section class="py-10 bg-white">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8" id="videos-grid">
                    <!-- Video cards will be dynamically generated -->
                </div>
            </div>
        </section>

        <!-- CTA Section -->
        <section class="py-10 bg-gradient-to-r from-blue-600 to-cyan-600 text-white">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
                <div class="cta-animate">
                    <h2 class="text-3xl font-bold mb-6">Start Your Own Recovery Journey</h2>
                    <p class="text-xl mb-8 text-blue-100 max-w-3xl mx-auto">
                        Join our growing family of happy, pain-free patients. Schedule your consultation today.
                    </p>
                    <a href="../contact.php"
                        class="inline-flex items-center px-8 py-4 bg-white text-blue-600 font-semibold rounded-xl hover:bg-blue-50 transition-all duration-300 transform hover:scale-105 shadow-xl">
                        <i data-feather="calendar" class="w-5 h-5 mr-2"></i>
                        Book Appointment
                    </a>
                </div>
            </div>
        </section>
    </main>

    <!-- Video Modal -->
    <div id="video-modal"
        class="fixed inset-0 z-50 hidden items-center justify-center p-4 bg-black/90 backdrop-blur-sm">
        <div
            class="modal-content relative w-full max-w-5xl aspect-video bg-black rounded-2xl overflow-hidden shadow-2xl">
            <button id="close-modal"
                class="absolute top-4 right-4 z-10 p-2 bg-white/10 hover:bg-white/20 rounded-full text-white transition-colors">
                <i data-feather="x" class="w-6 h-6"></i>
            </button>
            <div id="video-container" class="w-full h-full"></div>
        </div>
    </div>

    <!-- Footer -->
    <!-- Footer -->
    <?php include "components/footer.php"; ?>

    <!-- Scripts -->
    <script>
        // Video data
        const videos = [
            { id: 'PFNclB7NkCE', title: 'Patient Success Story', category: 'Knee Replacement' },
            { id: 'XKjqpMIKFT0', title: 'Recovery Journey', category: 'Joint Replacement' },
            { id: '26eSdQEygSk', title: 'Life After Surgery', category: 'Orthopedics' },
            { id: 'd13reLKlMbs', title: 'Patient Experience', category: 'Consultation' },
            { id: 'm9UHXw33tt4', title: 'Successful Recovery', category: 'Trauma Surgery' },
            { id: 'WUsyXT8-XMU', title: 'Back to Active Life', category: 'Sports Medicine' },
            { id: 'tSaZvq7K5Gc', title: 'Pain-Free Living', category: 'Joint Replacement' },
            { id: 'iR9vwr0yuDU', title: 'Patient Testimonial', category: 'General Orthopedics' },
            { id: 'BRkpeP4Sxlw', title: 'Treatment Satisfaction', category: 'Surgery' },
            { id: 'X0hRQmi9imU', title: 'Quality of Care', category: 'Patient Care' }
        ];

        // Wait for DOM to be fully loaded
        document.addEventListener('DOMContentLoaded', function () {
            // Generate video cards
            const videosGrid = document.getElementById('videos-grid');
            if (videosGrid) {
                videos.forEach((video, index) => {
                    const card = document.createElement('div');
                    card.className = 'bg-white rounded-xl overflow-hidden shadow-lg hover:shadow-xl transition-all duration-300 group cursor-pointer border border-gray-100 video-card';
                    card.style.animation = `fadeInUp 0.5s ease-out ${index * 0.1}s both`;
                    card.setAttribute('data-video-id', video.id);

                    card.innerHTML = `
                        <div class="relative aspect-video overflow-hidden">
                            <img src="https://img.youtube.com/vi/${video.id}/maxresdefault.jpg" 
                                alt="${video.title}"
                                class="w-full h-full object-cover transform group-hover:scale-105 transition-transform duration-500">
                            <div class="absolute inset-0 bg-black/30 group-hover:bg-black/20 transition-colors flex items-center justify-center">
                                <div class="w-16 h-16 bg-white/90 rounded-full flex items-center justify-center shadow-lg transform group-hover:scale-110 transition-transform">
                                    <i data-feather="play" class="w-6 h-6 text-blue-600 ml-1"></i>
                                </div>
                            </div>
                            <div class="absolute bottom-0 left-0 right-0 p-4 bg-gradient-to-t from-black/80 to-transparent">
                                <span class="text-white/90 text-sm font-medium px-2 py-1 bg-blue-600/80 rounded">
                                    ${video.category}
                                </span>
                            </div>
                        </div>
                        <div class="p-6">
                            <h3 class="text-lg font-bold text-gray-900 group-hover:text-blue-600 transition-colors">
                                ${video.title}
                            </h3>
                            <div class="mt-4 flex items-center text-sm text-blue-600 font-medium">
                                Watch Story <i data-feather="play" class="w-4 h-4 ml-2"></i>
                            </div>
                        </div>
                    `;
                    videosGrid.appendChild(card);
                });
            }

            // Re-initialize feather icons for dynamically added cards
            if (typeof feather !== 'undefined') {
                feather.replace();
            }

            // Video modal functionality
            const modal = document.getElementById('video-modal');
            const closeModalBtn = document.getElementById('close-modal');
            const videoContainer = document.getElementById('video-container');

            if (modal && closeModalBtn && videoContainer) {
                // Open video modal
                document.querySelectorAll('.video-card').forEach(card => {
                    card.addEventListener('click', function () {
                        const videoId = this.getAttribute('data-video-id');
                        openVideoModal(videoId);
                    });
                });

                // Close modal
                closeModalBtn.addEventListener('click', closeVideoModal);
                modal.addEventListener('click', function (e) {
                    if (e.target === modal) {
                        closeVideoModal();
                    }
                });

                // Close on Escape key
                document.addEventListener('keydown', function (e) {
                    if (e.key === 'Escape' && !modal.classList.contains('hidden')) {
                        closeVideoModal();
                    }
                });

                function openVideoModal(videoId) {
                    const iframe = document.createElement('iframe');
                    iframe.src = `https://www.youtube.com/embed/${videoId}?autoplay=1&rel=0`;
                    iframe.title = 'YouTube video player';
                    iframe.className = 'w-full h-full';
                    iframe.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture';
                    iframe.allowFullscreen = true;

                    videoContainer.innerHTML = '';
                    videoContainer.appendChild(iframe);

                    modal.classList.remove('hidden');
                    modal.classList.add('flex');
                    document.body.style.overflow = 'hidden';
                }

                function closeVideoModal() {
                    videoContainer.innerHTML = '';
                    modal.classList.add('hidden');
                    modal.classList.remove('flex');
                    document.body.style.overflow = '';
                }
            }
        });
    </script>
    

    <style>
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }

            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .hero-animate,
        .cta-animate {
            animation-fill-mode: both;
        }

        /* Modal animations */
        #video-modal {
            transition: opacity 0.3s ease-out;
        }

        #video-modal.hidden {
            opacity: 0;
            pointer-events: none;
        }

        .modal-content {
            transition: transform 0.3s ease-out, opacity 0.3s ease-out;
        }

        #video-modal.hidden .modal-content {
            transform: scale(0.9);
            opacity: 0;
        }

        /* Prevent body scroll when modal is open */
        body.modal-open {
            overflow: hidden;
        }
    </style>
</body>

</html>