/* global fetch */
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(function (response) {
    return response.json();
  })
  .then(function (data) {
    const listMovies = document.querySelector('#list_movies');
    for (const movie of data.results) {
      const li = document.createElement('li');
      li.textContent = movie.title;
      listMovies.appendChild(li);
    }
  });
