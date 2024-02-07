document.addEventListener('DOMContentLoaded', function () {
  const addItem = document.getElementById('update_header');

  addItem.addEventListener('click', function () {
    const header = document.querySelector('header');
    header.textContent = 'New Header!!!';
  });
});
