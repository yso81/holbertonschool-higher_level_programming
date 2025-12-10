const url = 'https://hellosalut.stefanbohacek.com/?lang=fr';

fetch(url)
  .then(function (response) {
    return response.json();
  })
  .then(function (data) {
    const helloElement = document.querySelector('#hello');
    helloElement.textContent = data.hello;
  });
  