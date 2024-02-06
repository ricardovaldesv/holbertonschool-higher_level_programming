document.addEventListener('DOMContentLoaded', function () {
  const redHeader = document.getElementById('red_header');

  redHeader.addEventListener('click', function () {
    const headerElement = document.querySelector('header');
    
    headerElement.classList.add('red');
  });
});
