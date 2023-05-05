// Obtener el elemento HTML que contiene todas las columnas de imágenes
const portfolioItems = document.querySelectorAll(".portfolio-item");

// Iterar sobre cada columna y obtener la imagen correspondiente
portfolioItems.forEach((item, index) => {
  const artworkId = (index + 1) * 95; // Calcular el ID de la obra de arte
  const imgElement = item.querySelector("img"); // Obtener la etiqueta <img> dentro de la columna
  const titleElement = item.querySelector(".portfolio-caption-heading"); // Obtener el elemento HTML para el título de la obra de arte
  const descElement = item.querySelector(".portfolio-caption-subheading"); // Obtener el elemento HTML para la descripción de la obra de arte
  const apiUrl = `https://collectionapi.metmuseum.org/public/collection/v1/objects/${artworkId}`; // URL de la API con el ID de la obra de arte

  fetch(apiUrl)
    .then(response => response.json())
    .then(data => {
      const imageUrl = data.primaryImageSmall;
      const title = data.title;
      const description = data.objectDate;

      imgElement.src = imageUrl;
      titleElement.textContent = title;
      descElement.textContent = description;
    })
    .catch(error => {
      console.error(error);
    });


    
});


const comunaSelect = document.getElementById("comuna");

// Cargar el JSON desde el enlace
fetch('https://gist.githubusercontent.com/juanbrujo/0fd2f4d126b3ce5a95a7dd1f28b3d8dd/raw/b8575eb82dce974fd2647f46819a7568278396bd/comunas-regiones.json')
  .then(response => response.json())
  .then(data => {
    // Iterar sobre el objeto JSON y agregar cada comuna como una opción en el selector de menú
    data.regiones.forEach(function(region) {
      region.comunas.forEach(function(comuna) {
        const option = document.createElement('option');
        option.value = comuna;
        option.textContent = comuna;
        comunaSelect.appendChild(option);
      });
    });
  })
  .catch(error => {
    console.error('Error al cargar el JSON: ', error);
  });