document.addEventListener('DOMContentLoaded', () => {
    // Add smooth scrolling for all anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });

    // Add active class to current nav item
    const navLinks = document.querySelectorAll('.nav-links a');
    navLinks.forEach(link => {
        link.addEventListener('click', function() {
            navLinks.forEach(l => l.classList.remove('active'));
            this.classList.add('active');
        });
    });
});

// This will be called when the page loads or when you want to refresh the posts
function fetchPosts() {
    fetch('http://localhost:8000/blogs/', {
      method: 'GET',
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token')}`, // Assuming JWT token is saved in localStorage
      },
    })
      .then(response => response.json())
      .then(data => {
        displayPosts(data); // Call the function to display posts
      })
      .catch(error => console.error('Error fetching posts:', error));
  }
  

