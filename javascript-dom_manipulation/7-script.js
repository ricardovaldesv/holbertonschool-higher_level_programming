document.addEventListener('DOMContentLoaded', async function () {
  const title = document.getElementById('list_movies');

  try {
    const response = await fetch('https://swapi-api.hbtn.io/api/films/?format=json');

    if (!response.ok) {
      throw new Error('Error in obtaining data');
    }

    const data = await response.json();
    console.log(data.results);
    for (let i = 0; i < data.results.length; i += 1) {
      const titleMovie = data.results[i].title;
      console.log(titleMovie);
      const newLi = document.createElement('li');
      const content = document.createTextNode(titleMovie);
      newLi.appendChild(content);
      title.appendChild(newLi);
    }
  } catch (error) {
    console.error('Error:', error.message);
    title.textContent = 'Error loading character';
  }
});
