const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

// Use the Fetch API to get the data
fetch(url)
  .then(function (response) {
    // Convert the response to JSON
    return response.json();
  })
  .then(function (data) {
    // Select the element with id 'character'
    const characterDiv = document.querySelector('#character');
    
    // Update the text content with the name from the fetched data
    characterDiv.textContent = data.name;
  });
