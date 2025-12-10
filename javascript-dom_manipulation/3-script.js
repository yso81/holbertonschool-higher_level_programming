// Select the element with the id 'toggle_header'
const toggleHeader = document.querySelector('#toggle_header');

// Add a click event listener
toggleHeader.addEventListener('click', function () {
  // Select the header element
  const header = document.querySelector('header');

  // Check if the header currently has the class 'red'
  if (header.classList.contains('red')) {
    // If red, remove 'red' and add 'green'
    header.classList.remove('red');
    header.classList.add('green');
  } else {
    // If not red (i.e., green or empty), remove 'green' and add 'red'
    header.classList.remove('green');
    header.classList.add('red');
  }
});
