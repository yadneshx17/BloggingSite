// Handle tab switching for Login and Register
document.querySelectorAll('.tab').forEach((tab) => {
    tab.addEventListener('click', () => {
      document.querySelectorAll('.tab').forEach((btn) => btn.classList.remove('active'));
      tab.classList.add('active');
  
      const activeTab = tab.dataset.tab;
      document.querySelectorAll('.form').forEach((form) => {
        form.classList.remove('active');
      });
      document.querySelector(`#${activeTab}Form`).classList.add('active');
    });
  });
  
  // Handle Login Form Submission
  document.getElementById('loginForm').addEventListener('submit', async (event) => {
    event.preventDefault(); // Prevent form from refreshing the page
  
    const formData = new FormData(event.target); // Collect form data
  
    try {
      const response = await fetch('http://localhost:8000/login', {
        method: 'POST',
        body: formData, // Send the form-data
      });
  
      if (response.ok) {
        const data = await response.json();
        console.log('Login successful:', data);
        alert('Login successful!');
        // Handle success, e.g., redirect or save token
      } else {
        console.error('Login failed');
        alert('Login failed. Please check your credentials.');
      }
    } catch (error) {
      console.error('Error:', error);
      alert('An error occurred while logging in.');
    }
  });
  
// Handle Register Form Submission
document.getElementById('registerForm').addEventListener('submit', async (event) => {
  event.preventDefault(); // Prevent form refresh

  // Collect form data using FormData API
  const formData = new FormData(event.target);

  // Convert FormData to a plain object, then to JSON
  const formDataObject = Object.fromEntries(formData.entries());
  const jsonData = JSON.stringify(formDataObject);

  try {
    const response = await fetch('http://localhost:8000/register', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json', // Specify JSON content type
      },
      body: jsonData, // Send JSON data
    });

    if (response.ok) {
      const data = await response.json();
      console.log('Registration successful:', data);
      alert('Registration successful!');
      // Optionally redirect to login page
    } else {
      const errorData = await response.json();
      console.error('Registration failed:', errorData);
      alert(`Registration failed: ${errorData.detail}`);
    }
  } catch (error) {
    console.error('Error:', error);
    alert('An error occurred during registration.');
  }
});

  
  