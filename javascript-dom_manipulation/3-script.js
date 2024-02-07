document.addEventListener('DOMContentLoaded', function () {
  const headerElement = document.querySelector('header');

  const toggleHeader = document.getElementById('toggle_header');

  function toogleClass() {
    if (headerElement.classList.contains('red')) {
      headerElement.classList.remove('red');
      headerElement.classList.add('green');
    } else {
      headerElement.classList.remove('green');
      headerElement.classList.add('red');
    }
  }

  toggleHeader.addEventListener('click', toogleClass);
});
