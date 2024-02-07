document.addEventListener('DOMContentLoaded', async function () {
  const character = document.getElementById('character');

  try {
    const response = await fetch('https://swapi-api.hbtn.io/api/people/5/?format=json');

    if (!response.ok) {
      throw new Error('Error in obtaining data');
    }

    const data = await response.json();
    console.log(data);
    character.textContent = data.name;
  } catch (error) {
    console.error('Error:', error.message);
    character.textContent = 'Error loading character';
  }
});
