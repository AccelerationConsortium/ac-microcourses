document.addEventListener("DOMContentLoaded", function() {
    // Check if the current page is the one you want to modify
    if (window.location.href.endsWith('certificate-framework.html')) {
        var footer = document.querySelector('.footer');
        if (footer) {
            // Modify the footer here. For example:
            footer.style.backgroundColor = 'red';
        }
    }
});
