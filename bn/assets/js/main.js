// Main JavaScript file

document.addEventListener('DOMContentLoaded', () => {
  loadComponents().then(() => {
    initializeInteractions();
    initializeVideoPlayer();
  });
});

async function loadComponents() {
  try {
    // Load Header
    const headerPlaceholder = document.getElementById('header-placeholder');
    if (headerPlaceholder) {
      const headerResponse = await fetch('components/header.php');
      if (headerResponse.ok) {
        headerPlaceholder.innerHTML = await headerResponse.text();
        setActiveLink();
      }
    }

    // Load Footer
    const footerPlaceholder = document.getElementById('footer-placeholder');
    if (footerPlaceholder) {
      const footerResponse = await fetch('components/footer.php');
      if (footerResponse.ok) {
        footerPlaceholder.innerHTML = await footerResponse.text();
      }
    }
  } catch (error) {
    console.error('Error loading components:', error);
  }
}

function setActiveLink() {
  const currentPath = window.location.pathname.split('/').pop() || 'index.php';
  const navLinks = document.querySelectorAll('.nav-link');

  navLinks.forEach(link => {
    const linkPath = link.getAttribute('href');
    if (linkPath === currentPath) {
      link.classList.add('text-[#1E97D9]');
      link.classList.remove('text-gray-700');
    }
  });
}

function initializeInteractions() {
  // Initialize Feather Icons
  if (typeof feather !== 'undefined') {
    feather.replace();
  }

  // Mobile Menu Toggle
  const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
  const mobileMenu = document.querySelector('.mobile-menu');
  const closeMenuBtn = document.querySelector('.close-menu-btn');

  if (mobileMenuBtn && mobileMenu) {
    mobileMenuBtn.addEventListener('click', () => {
      mobileMenu.classList.remove('hidden');
      document.body.classList.add('overflow-hidden');
    });
  }

  if (closeMenuBtn && mobileMenu) {
    closeMenuBtn.addEventListener('click', () => {
      mobileMenu.classList.add('hidden');
      document.body.classList.remove('overflow-hidden');
    });
  }

  // Mobile Accordions
  const accordionBtns = document.querySelectorAll('.mobile-accordion-btn');
  accordionBtns.forEach(btn => {
    btn.addEventListener('click', function () {
      const content = this.nextElementSibling;
      const icon = this.querySelector('i');

      // Toggle current
      content.classList.toggle('hidden');
      if (icon) icon.classList.toggle('rotate-180');
    });
  });

  // Header Scroll Effect
  const header = document.querySelector('header');
  if (header) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 50) {
        header.classList.add('bg-white', 'shadow-md');
        header.classList.remove('bg-transparent');
      } else {
        header.classList.remove('bg-white', 'shadow-md');
        header.classList.add('bg-transparent');
      }
    });
  }

  // Services Dropdown (Desktop)
  const servicesDropdownBtn = document.querySelector('.services-dropdown-btn');
  const servicesDropdownMenu = document.querySelector('.services-dropdown-menu');
  let timeoutId;

  if (servicesDropdownBtn && servicesDropdownMenu) {
    const servicesWrapper = servicesDropdownBtn.closest('.group');

    servicesWrapper.addEventListener('mouseenter', () => {
      clearTimeout(timeoutId);
      servicesDropdownMenu.classList.remove('hidden');
      setTimeout(() => {
        servicesDropdownMenu.classList.remove('opacity-0', 'translate-y-2');
      }, 10);
    });

    servicesWrapper.addEventListener('mouseleave', () => {
      servicesDropdownMenu.classList.add('opacity-0', 'translate-y-2');
      timeoutId = setTimeout(() => {
        servicesDropdownMenu.classList.add('hidden');
      }, 200);
    });
  }

  // Patient Info Dropdown (Desktop)
  const patientInfoBtn = document.querySelector('.patient-info-btn');
  const patientInfoMenu = document.querySelector('.patient-info-menu');
  let patientTimeoutId;

  if (patientInfoBtn && patientInfoMenu) {
    const patientWrapper = patientInfoBtn.closest('.group');

    patientWrapper.addEventListener('mouseenter', () => {
      clearTimeout(patientTimeoutId);
      patientInfoMenu.classList.remove('hidden');
      setTimeout(() => {
        patientInfoMenu.classList.remove('opacity-0', 'translate-y-2');
      }, 10);
    });

    patientWrapper.addEventListener('mouseleave', () => {
      patientInfoMenu.classList.add('opacity-0', 'translate-y-2');
      patientTimeoutId = setTimeout(() => {
        patientInfoMenu.classList.add('hidden');
      }, 200);
    });
  }

  // FAQ Accordion (if present)
  document.querySelectorAll('.faq-question').forEach((question) => {
    question.addEventListener('click', function (e) {
      e.preventDefault();
      const faqItem = this.parentElement;
      const answer = faqItem.querySelector('.faq-answer');
      const icon = this.querySelector('i[data-feather="chevron-down"]');

      document.querySelectorAll('.faq-item').forEach((item) => {
        if (item !== faqItem) {
          const otherAnswer = item.querySelector('.faq-answer');
          const otherIcon = item.querySelector('i[data-feather="chevron-down"]');
          if (otherAnswer) otherAnswer.classList.add('hidden');
          if (otherIcon) otherIcon.classList.remove('rotate-180');
        }
      });

      if (answer) answer.classList.toggle('hidden');
      if (icon) icon.classList.toggle('rotate-180');
    });
  });

  // Animations initialization
  initAnimations();
}

function initAnimations() {
  const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -100px 0px'
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = '1';
        entry.target.style.transform = 'translateY(0)';
      }
    });
  }, observerOptions);

  document.querySelectorAll('.section-animate, .benefit-card, .type-card, .treatment-card, .before-after-card, .cause-card, .doctor-hero-animate, .doctor-card-animate, .cta-animate, .card-animate, .service-animate, .journey-step, .process-step, .hero-content, .hero-image').forEach((el) => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(30px)';
    el.style.transition = 'opacity 0.6s ease-out, transform 0.6s ease-out';
    observer.observe(el);
  });
}

function initializeVideoPlayer() {
  // Video Testimonials Logic
  const videos = [
    {
      id: 'tSaZvq7K5Gc',
      title: 'Robotic Knee Replacement',
      duration: '4:32',
      thumbnail: 'https://img.youtube.com/vi/tSaZvq7K5Gc/maxresdefault.jpg'
    },
    {
      id: 'iR9vwr0yuDU',
      title: 'Hip Replacement Surgery',
      duration: '3:45',
      thumbnail: 'https://img.youtube.com/vi/iR9vwr0yuDU/maxresdefault.jpg'
    },
    {
      id: 'BRkpeP4Sxlw',
      title: 'ACL Reconstruction',
      duration: '5:12',
      thumbnail: 'https://img.youtube.com/vi/BRkpeP4Sxlw/maxresdefault.jpg'
    },
    {
      id: 'X0hRQmi9imU',
      title: 'Shoulder Replacement',
      duration: '4:18',
      thumbnail: 'https://img.youtube.com/vi/X0hRQmi9imU/maxresdefault.jpg'
    }
  ];

  let currentVideoIndex = 0;

  // Make functions available globally for onclick events if needed, 
  // but better to attach listeners if possible. 
  // keeping global for compatibility with existing inline onclicks.
  window.playVideo = function () {
    const videoContainer = document.getElementById('main-video-container');
    const iframe = document.getElementById('video-iframe');
    const closeBtn = document.getElementById('close-video-btn');

    if (!iframe) return;

    // Set iframe src to autoplay
    iframe.src = `https://www.youtube.com/embed/${videos[currentVideoIndex].id}?autoplay=1`;

    // Show iframe and close button, hide thumbnail
    iframe.classList.remove('hidden');
    closeBtn.classList.remove('hidden');
  };

  window.closeVideo = function () {
    const iframe = document.getElementById('video-iframe');
    const closeBtn = document.getElementById('close-video-btn');

    if (!iframe) return;

    // Stop video
    iframe.src = '';

    // Hide iframe and close button
    iframe.classList.add('hidden');
    closeBtn.classList.add('hidden');
  };

  window.switchVideo = function (index) {
    if (index === currentVideoIndex) return;

    // Update current index
    currentVideoIndex = index;

    // Update main display
    const thumbnail = document.getElementById('current-video-thumbnail');
    const title = document.getElementById('current-video-title');
    const duration = document.getElementById('current-video-duration');
    const iframe = document.getElementById('video-iframe');
    const closeBtn = document.getElementById('close-video-btn');

    if (!thumbnail) return;

    // Reset player state
    if (iframe) {
      iframe.src = '';
      iframe.classList.add('hidden');
    }
    if (closeBtn) closeBtn.classList.add('hidden');

    // Update info
    thumbnail.src = videos[index].thumbnail;
    title.textContent = videos[index].title;
    duration.textContent = videos[index].duration;

    // Update active state in list
    document.querySelectorAll('#video-list > div').forEach((el, i) => {
      if (i === index) {
        el.className = 'group cursor-pointer rounded-xl p-4 transition-all duration-300 bg-blue-50 border-2 border-blue-200';
        el.querySelector('h4').className = 'font-semibold truncate text-blue-700';
      } else {
        el.className = 'group cursor-pointer rounded-xl p-4 transition-all duration-300 bg-gray-50 hover:bg-gray-100 border-2 border-transparent';
        el.querySelector('h4').className = 'font-semibold truncate text-gray-900';
      }
    });
  };
}

