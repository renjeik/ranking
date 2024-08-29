const rankCompaniesUrlInput = document.getElementById("rankCompaniesUrlInput");
const rankCompaniesUrl = rankCompaniesUrlInput.value;

const rankCompaniesViewUrlInput = document.getElementById("rankCompaniesViewUrlInput");
const rankCompaniesViewUrl = rankCompaniesViewUrlInput.value;

// Function to handle the search action
function handleSearch() {
    // Get the value from the input field
    const searchTerm = document.getElementById('searchTerm').value;

    var formData = new FormData();
    formData.append('search_term', searchTerm);

    // Make the fetch request
    fetch(rankCompaniesUrl, {
        method: 'POST',
        body: formData,
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(json => {
        var form = document.createElement('form');
        form.setAttribute('method', 'post');
        form.setAttribute('action', rankCompaniesViewUrl);

        // Create hidden input fields and append them to the form
        var companiesInput = document.createElement('input');
        companiesInput.setAttribute('type', 'hidden');
        companiesInput.setAttribute('name', 'companies');
        companiesInput.setAttribute('value', JSON.stringify(json));
        form.appendChild(companiesInput);

        document.body.appendChild(form);
        form.submit();
    })
    .catch(error => {
        console.error('There was a problem with the fetch Rank Companies operation:', error);
    });
}

// Event listener for the button click
document.getElementById('searchButton').addEventListener('click', function() {
    handleSearch();
});

// Event listener for the Enter key press in the input field
document.getElementById('searchTerm').addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        event.preventDefault(); // Prevent the default form submission (if inside a form)
        handleSearch();
    }
});