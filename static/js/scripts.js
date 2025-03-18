// Frontend validation
document.getElementById('feedbackForm').addEventListener('submit', function(e) {
    let valid = true;
    
    // Name validation
    const nameInput = document.getElementById('name');
    if (nameInput.value.length < 2) {
        nameInput.classList.add('is-invalid');
        valid = false;
    } else {
        nameInput.classList.remove('is-invalid');
    }

    // Email validation
    const emailInput = document.getElementById('email');
    if (!/^\S+@\S+\.\S+$/.test(emailInput.value)) {
        emailInput.classList.add('is-invalid');
        valid = false;
    } else {
        emailInput.classList.remove('is-invalid');
    }

    if (!valid) e.preventDefault();
});

// Fetch internal projects API
fetch('/api/projects')
    .then(response => response.json())
    .then(projects => {
        console.log('Loaded projects:', projects);
    });