document.addEventListener('DOMContentLoaded', function () {
  const addItem = document.getElementById('add_item');

  addItem.addEventListener('click', function () {
    const lissItem = document.querySelector('.my_list');

    const newLi = document.createElement('li');

    const content = document.createTextNode('Item');

    newLi.appendChild(content);

    lissItem.appendChild(newLi);
  });
});
