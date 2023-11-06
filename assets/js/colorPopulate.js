
function fetchColorPalette(route) {
  fetch(route)
    .then(response => response.json())
    .then(data => {
      // Itera pelas divs com a classe 'corX' e aplica as cores e valores HEX correspondentes
      for (let i = 1; i <= 5; i++) {
        const corDiv = document.querySelector(`.cor${i}`);
        const cor = data.paleta[`cor${i}`];
        
        // Define o background-color e o texto da div
        corDiv.style.backgroundColor = cor;
        corDiv.textContent = cor;
      }
    })
    .catch(error => console.error('Erro ao buscar a paleta de cores:', error));
}

fetchColorPalette('http://192.168.0.54:5000/mono'); 