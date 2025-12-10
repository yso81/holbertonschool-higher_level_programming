// Select the element with the id 'add_item'
const addItem = document.querySelector('#add_item');

// Add a click event listener
addItem.addEventListener('click', function () {
  // Select the <ul> element with the class 'my_list'
  const myList = document.querySelector('.my_list');

  // Create a new <li> element
  const newLi = document.createElement('li');

  // Set the text content of the new element
  newLi.textContent = 'Item';

  // Append the new <li> to the list
  myList.appendChild(newLi);
});
