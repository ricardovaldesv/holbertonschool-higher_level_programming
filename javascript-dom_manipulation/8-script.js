document.addEventListener('DOMContentLoaded', async function () {
  const title = document.getElementById('hello');

  try {
    const response = await fetch('https://hellosalut.stefanbohacek.dev/?lang=fr');

    if (!response.ok) {
      throw new Error('Error in obtaining data');
    }

    const data = await response.json();
    console.log(data);
    title.textContent = data.hello;

  } catch (error) {
    console.error('Error:', error.message);
    title.textContent = 'Error loading character';
  }
});
