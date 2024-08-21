let companyName = document.getElementById("company-name");
let locationName = document.getElementById("location-name");
let description = document.getElementById("description");

const companiesViewUrlInput = document.getElementById("companiesViewUrlInput");
const companiesViewUrl = companiesViewUrlInput.value;

const addCompanyUrlInput = document.getElementById("addCompanyUrlInput");
const addCompanyUrl = addCompanyUrlInput.value;

function forError(element) {
    const isEmpty = element.value.trim() === '';
    element.style.border = `1px solid ${isEmpty ? 'hsl(0, 66%, 56%)' : 'hsl(186, 15%, 59%)'}`;
    element.nextElementSibling.style.visibility = isEmpty ? 'visible' : 'hidden';
    return !isEmpty;
}

let items = [companyName, locationName, description];

document.forms[0].addEventListener("submit", function (e) {
    e.preventDefault();
    let isValid = true;

    for(let i = 0; i < items.length; i++) {
        if (!forError(items[i])) {
            isValid = false;
        }
    }

    // if (!isValid) {
    //     e.preventDefault();
    // }

    if (isValid) {
        // If all fields are valid, proceed to call the API
        var formData = new FormData();
        formData.append('name', companyName.value.trim());
        formData.append('location', locationName.value.trim());
        formData.append('description', description.value.trim());

        fetch(addCompanyUrl, {
            method: 'POST',
            body: formData,
        })
        .then(response => {
            // If the status is not in the range 200-299
            if (!response.ok) {
                throw new Error('Failed to complete tool(s).');
            }
            return response.json();
        })
        .then(json => {
            var form = document.createElement('form');
            form.setAttribute('method', 'get');
            form.setAttribute('action', companiesViewUrl);

            document.getElementById('hiddenFormContainer').appendChild(form);
            form.submit();
        })
        .catch(error => {
            // Handle error
            console.error('There was a problem with the fetch Add Company operation:', error);
        });
        return;
    }
});