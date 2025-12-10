const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

// Fetch the data from the URL
fetch(url)
  .then(function (response) {
    // Convert the response to JSON
    return response.json();
  })
  .then(function (data) {
    // Select the <ul> element with id 'list_movies'
    const listMovies = document.querySelector('#list_movies');

    // Iterate through the results array provided by the API
    data.results.forEach(function (movie) {
      // Create a new <li> element
      const listItem = document.createElement('li');

      // Set the text content to the movie title
      listItem.textContent = movie.title;

      // Append the <li> to the <ul>
      listMovies.appendChild(listItem);
    });
  });
  