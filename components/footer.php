<!-- ========== STICKY BOTTOM AD BANNER ========== -->
<div id="sticky-ad-banner" style="
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    width: 100%;
    height: 30vh;
    min-height: 120px;
    max-height: 300px;
    background: #fff;
    box-shadow: 0 -4px 24px rgba(0,0,0,0.18);
    z-index: 99999;
    display: flex;
    flex-direction: column;
    align-items: stretch;
    transform: translateY(100%);
    transition: transform 0.4s cubic-bezier(0.4,0,0.2,1);
    border-top: 2px solid #1E97D9;
">
    <!-- Close button -->
    <button
        id="sticky-ad-close-btn"
        onclick="closeStickyAd()"
        aria-label="Close advertisement"
        style="
            position: absolute;
            top: 6px;
            right: 10px;
            width: 32px;
            height: 32px;
            border-radius: 50%;
            background: rgba(30,151,217,0.12);
            border: 1.5px solid #1E97D9;
            color: #1E97D9;
            font-size: 18px;
            font-weight: bold;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 100000;
            line-height: 1;
            transition: background 0.2s, transform 0.2s;
        "
        onmouseover="this.style.background='#1E97D9';this.style.color='#fff';this.style.transform='scale(1.1)'"
        onmouseout="this.style.background='rgba(30,151,217,0.12)';this.style.color='#1E97D9';this.style.transform='scale(1)'"
    >&times;</button>
    <!-- Ad label -->
    <div style="text-align:center;font-size:10px;color:#aaa;letter-spacing:1px;padding-top:4px;flex-shrink:0;">ADVERTISEMENT</div>
    <!-- AdSense unit -->
    <div style="flex:1;overflow:hidden;display:flex;align-items:center;justify-content:center;padding:0 8px 4px;">
        <ins class="adsbygoogle"
             style="display:block;width:100%;height:100%;"
             data-ad-client="ca-pub-4910239000711715"
             data-ad-slot="5541132135"
             data-ad-format="auto"
             data-full-width-responsive="true"></ins>
    </div>
</div>

<script>
(function(){
    // Only show if not dismissed this session
    if (!sessionStorage.getItem('stickyAdClosed')) {
        // Slide in after short delay
        var banner = document.getElementById('sticky-ad-banner');
        if (banner) {
            setTimeout(function(){
                banner.style.transform = 'translateY(0)';
                // Push AdSense ad after visible
                try { (adsbygoogle = window.adsbygoogle || []).push({}); } catch(e){}
            }, 800);
        }
    } else {
        var banner = document.getElementById('sticky-ad-banner');
        if (banner) banner.style.display = 'none';
    }
})();

function closeStickyAd() {
    var banner = document.getElementById('sticky-ad-banner');
    if (banner) {
        banner.style.transform = 'translateY(100%)';
        setTimeout(function(){ banner.style.display = 'none'; }, 420);
    }
    sessionStorage.setItem('stickyAdClosed', '1');
}
</script>
<!-- ========== END STICKY BOTTOM AD BANNER ========== -->

<!-- Footer -->
<footer class="bg-gradient-to-br from-gray-900 via-blue-900 to-indigo-900 text-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-8">
            <!-- About Column -->
            <div class="lg:col-span-2 space-y-4">
                <div class="flex items-center space-x-3">
                    <img src="https://impactorthocenter.com/photos/impact-white-logo.png" alt="Impact Ortho Centre"
                        class="h-14 w-auto" />
                </div>
                <p class="text-gray-300 text-sm leading-relaxed">
                    World-class orthopedic care in India, trusted by international patients from 40+ countries.
                    Specializing in robotic surgery, joint replacement, and comprehensive medical tourism services
                    with international standards and personalized care.
                </p>
                <div class="flex space-x-4">
                    <a href="#" class="text-gray-400 hover:text-cyan-400 transition-colors">
                        <i data-feather="facebook" class="w-5 h-5"></i>
                    </a>
                    <a href="#" class="text-gray-400 hover:text-cyan-400 transition-colors">
                        <i data-feather="instagram" class="w-5 h-5"></i>
                    </a>
                    <a href="#" class="text-gray-400 hover:text-cyan-400 transition-colors">
                        <i data-feather="linkedin" class="w-5 h-5"></i>
                    </a>
                    <a href="#" class="text-gray-400 hover:text-cyan-400 transition-colors">
                        <i data-feather="youtube" class="w-5 h-5"></i>
                    </a>
                </div>
                <!-- Trust Badges -->
                <div class="flex flex-wrap gap-3 pt-4">
                    <div
                        class="flex items-center space-x-2 bg-white/10 backdrop-blur-sm rounded-full px-3 py-1 text-xs">
                        <i data-feather="shield" class="w-3 h-3 text-cyan-400"></i>
                        <span>ISO Certified</span>
                    </div>
                    <div
                        class="flex items-center space-x-2 bg-white/10 backdrop-blur-sm rounded-full px-3 py-1 text-xs">
                        <i data-feather="award" class="w-3 h-3 text-cyan-400"></i>
                        <span>NABH Accredited</span>
                    </div>
                    <div
                        class="flex items-center space-x-2 bg-white/10 backdrop-blur-sm rounded-full px-3 py-1 text-xs">
                        <i data-feather="globe" class="w-3 h-3 text-cyan-400"></i>
                        <span>Global Excellence</span>
                    </div>
                </div>
            </div>

            <!-- Quick Links -->
            <div>
                <h4 class="text-lg font-semibold mb-4 text-cyan-400">Quick Links</h4>
                <ul class="space-y-2">
                    <li><a href="index.php" class="text-gray-300 hover:text-cyan-400 transition-colors">Home</a>
                    </li>
                    <li><a href="about.php" class="text-gray-300 hover:text-cyan-400 transition-colors">About
                            Us</a></li>
                    <li><a href="doctors.php" class="text-gray-300 hover:text-cyan-400 transition-colors">Doctors</a>
                    </li>
                    <li><a href="https://impactorthocenter.com/blog/"
                            class="text-gray-300 hover:text-cyan-400 transition-colors">Blogs</a></li>
                    <li><a href="contact.php" class="text-gray-300 hover:text-cyan-400 transition-colors">Contact</a>
                    </li>
                    <li><a href="international-patients.php"
                            class="text-gray-300 hover:text-cyan-400 transition-colors">International Patients</a>
                    </li>
                    <li><a href="domestic-patients.php"
                            class="text-gray-300 hover:text-cyan-400 transition-colors">Domestic Patients</a></li>
                    <li><a href="video-testimonials.php"
                            class="text-gray-300 hover:text-cyan-400 transition-colors">Video Testimonials</a></li>
                </ul>
            </div>

            <!-- Medical Tourism -->
            <div>
                <h4 class="text-lg font-semibold mb-4 text-cyan-400">General Orthopedics</h4>
                <ul class="space-y-2">
                    <li><a href="arthritis.php"
                            class="text-gray-300 hover:text-cyan-400 transition-colors">Arthritis</a></li>
                    <li><a href="back-pain.php" class="text-gray-300 hover:text-cyan-400 transition-colors">Back
                            Pain</a></li>
                    <li><a href="elbow-pain.php" class="text-gray-300 hover:text-cyan-400 transition-colors">Elbow
                            Pain</a></li>
                    <li><a href="foot-ankle-pain.php" class="text-gray-300 hover:text-cyan-400 transition-colors">Foot
                            Ankle</a></li>
                    <li><a href="hand-wrist-pain.php" class="text-gray-300 hover:text-cyan-400 transition-colors">Hand
                            Wrist Pain</a></li>
                    <li><a href="knee-pain.php" class="text-gray-300 hover:text-cyan-400 transition-colors">Knee
                            Pain</a></li>
                    <li><a href="neck-pain.php" class="text-gray-300 hover:text-cyan-400 transition-colors">Neck
                            Pain</a></li>
                    <li><a href="osteoporosis.php"
                            class="text-gray-300 hover:text-cyan-400 transition-colors">Osteoporosis</a></li>
                    <li><a href="shoulder-pain.php" class="text-gray-300 hover:text-cyan-300 transition-colors">Shoulder
                            Pain</a></li>
                </ul>
            </div>

            <!-- Contact Info -->
            <div>
                <h4 class="text-lg font-semibold mb-4 text-cyan-400">Contact Info</h4>
                <div class="space-y-3">
                    <div class="flex items-start space-x-3">
                        <i data-feather="map-pin" class="w-5 h-5 text-cyan-400 mt-1 flex-shrink-0"></i>
                        <p class="text-gray-300 text-sm">
                            Apollo Hospitals, Rd Number 72,<br />
                            opposite Bharatiya Vidya Bhavan School,<br />
                            Film Nagar, Hyderabad, Telangana 500033
                        </p>
                    </div>
                    <div class="flex items-center space-x-3">
                        <i data-feather="phone" class="w-5 h-5 text-cyan-400"></i>
                        <a href="tel:+919494559848" class="text-gray-300 hover:text-cyan-400 transition-colors">
                            +91 9494559848
                        </a>
                    </div>
                    <div class="flex items-center space-x-3">
                        <i data-feather="mail" class="w-5 h-5 text-cyan-400"></i>
                        <a href="mailto:impactorthoc.dm@gmail.com"
                            class="text-gray-300 hover:text-cyan-400 transition-colors">
                            impactorthoc.dm@gmail.com
                        </a>
                    </div>
                    <div class="flex items-start space-x-3">
                        <i data-feather="clock" class="w-5 h-5 text-cyan-400 mt-1"></i>
                        <div class="text-gray-300 text-sm">
                            <p>Monday - Saturday: 10:00 AM - 4:00 PM</p>
                            <p>Sunday: Closed</p>
                            <p class="text-cyan-400 font-medium">Emergency: 24/7 Available</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- International Patient Hotline -->
        <div class="bg-gradient-to-r from-cyan-600 to-blue-600 rounded-2xl p-6 mt-8 mb-8">
            <div class="flex flex-col md:flex-row items-center justify-between">
                <div class="flex items-center space-x-4 mb-4 md:mb-0">
                    <div class="w-12 h-12 bg-white/20 backdrop-blur-sm rounded-full flex items-center justify-center">
                        <i data-feather="globe" class="w-6 h-6 text-white"></i>
                    </div>
                    <div>
                        <h4 class="text-xl font-bold text-white">International Patient Hotline</h4>
                        <p class="text-cyan-100">24/7 Support for Global Patients</p>
                    </div>
                </div>
                <div class="flex items-center space-x-4">
                    <a href="tel:+919494559848"
                        class="flex items-center space-x-2 bg-white text-blue-600 px-6 py-3 rounded-xl font-semibold hover:bg-blue-50 transition-colors">
                        <i data-feather="phone" class="w-5 h-5"></i>
                        <span>+91 9494559848</span>
                    </a>
                    <a href="contact.php"
                        class="flex items-center space-x-2 bg-white/20 backdrop-blur-sm text-white px-6 py-3 rounded-xl font-semibold hover:bg-white/30 transition-colors">
                        <i data-feather="plane" class="w-5 h-5"></i>
                        <span>Get Quote</span>
                    </a>
                </div>
            </div>
        </div>

        <!-- Bottom Bar -->
        <div class="border-t border-gray-700 pt-8 flex flex-col md:flex-row justify-between items-center">
            <p class="text-gray-400 text-sm">
                © 2024 Impact Orthopedic & Joint Replacement Center. All rights reserved.
            </p>
            <div class="flex space-x-6 mt-4 md:mt-0">
                <a href="#" class="text-gray-400 hover:text-cyan-400 text-sm transition-colors">Privacy Policy</a>
                <a href="#" class="text-gray-400 hover:text-cyan-400 text-sm transition-colors">Terms of Service</a>
                <a href="#" class="text-gray-400 hover:text-cyan-400 text-sm transition-colors">Sitemap</a>
            </div>
        </div>
    </div>
</footer>


<script src="assets/js/main.js"></script>


<script defer src="https://app.wacrs.com/install-widget/bundle.js?key=ba48163b-d301-4764-9bbe-08bc440922e2"></script>