// Select the element with the id 'red_header'
const redHeader = document.querySelector('#red_header');

// Add a click event listener
redHeader.addEventListener('click', function () {
  // Select the header element
  const header = document.querySelector('header');
  
  // Add the class 'red' to the header element
  header.classList.add('red');
});