const API_LOCAL = 'http://localhost:8000';

function CreateGrafic(arrayOptions) {
    // Obtener una referencia al elemento canvas del DOM
    const $grafica = document.querySelector("#grafica");
    // Las etiquetas son las que van en el eje X. 
    const etiquetas = arrayOptions.tiempos
    // Podemos tener varios conjuntos de datos. Comencemos con uno

    const DatosArduino = {
        label: "Datos Graficados",
        data: arrayOptions.data, // La data es un arreglo que debe tener la misma cantidad de valores que la cantidad de etiquetas
        backgroundColor: 'rgba(54, 162, 235, 0.2)', // Color de fondo
        borderColor: 'rgba(54, 162, 235, 1)', // Color del borde
        borderWidth: 1,// Ancho del borde
    };
    new Chart($grafica, {
        type: 'line',// Tipo de gráfica
        data: {
            labels: etiquetas,
            datasets: [
                DatosArduino,
                // Aquí más datos...
            ]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }],
            },
        }
});

}

async function fetchData(urlApi){
  const response = await fetch(urlApi, {mode: 'no-cors',method: 'POST'});
  const data = await response.json();
  console.log(data);
  CreateGrafic(data)
}

fetchData(`${API_LOCAL}/sensors/1`);






