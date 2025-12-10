// Select the element with the id 'red_header'
const redHeader = document.querySelector('#red_header');

// Add a 'click' event listener to it
redHeader.addEventListener('click', function () {
  // Select the <header> element
  const header = document.querySelector('header');
  
  // Update the text color to red
  header.style.color = '#FF0000';
});
