// Select the element with the id 'update_header'
const updateHeader = document.querySelector('#update_header');

// Add a click event listener
updateHeader.addEventListener('click', function () {
  // Select the header element
  const header = document.querySelector('header');

  // Update the text content of the header
  header.textContent = 'New Header!!!';
});
