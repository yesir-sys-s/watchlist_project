document.addEventListener('DOMContentLoaded', function() {
    // Add loading animation when forms are submitted
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function() {
            const submitBtn = this.querySelector('button[type="submit"]');
            if (submitBtn) {
                submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Processing...';
                submitBtn.disabled = true;
            }
        });
    });

    // Add hover effects to movie items
    const movieItems = document.querySelectorAll('.list-group-item');
    movieItems.forEach(item => {
        item.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-4px)';
        });
        
        item.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });

    // Fade in elements on page load
    const content = document.querySelector('.container');
    if (content) {
        content.style.opacity = '0';
        content.style.transition = 'opacity 0.5s ease-in';
        setTimeout(() => {
            content.style.opacity = '1';
        }, 100);
    }

    // Smooth scroll animation
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Parallax effect for hero section
    const hero = document.querySelector('.home-hero');
    if (hero) {
        window.addEventListener('scroll', () => {
            const scrolled = window.pageYOffset;
            hero.style.transform = `translateY(${scrolled * 0.4}px)`;
            hero.style.opacity = 1 - (scrolled * 0.003);
        });
    }

    // Animate elements on scroll
    const animateOnScroll = () => {
        const elements = document.querySelectorAll('.list-group-item, .card, .btn');
        elements.forEach(element => {
            const elementTop = element.getBoundingClientRect().top;
            if (elementTop < window.innerHeight - 100) {
                element.style.opacity = '1';
                element.style.transform = 'translateY(0)';
            }
        });
    };

    // Initialize animation states
    document.querySelectorAll('.list-group-item, .card, .btn').forEach(element => {
        element.style.opacity = '0';
        element.style.transform = 'translateY(20px)';
        element.style.transition = 'all 0.6s cubic-bezier(0.4, 0, 0.2, 1)';
    });

    window.addEventListener('scroll', animateOnScroll);
    animateOnScroll();
});
