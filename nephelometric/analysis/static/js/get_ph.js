
//const URL = 'https://sistema-calidad-del-agua.link/get_muestra_ph/';
const URL = 'http://127.0.0.1:8000/get_muestra_ph/';
// http://127.0.0.1:8000/ph/
fetch(URL)
  .then(res => res.json())
  .then(data => {
    const voltaje_prom = data.map(obj => obj.voltaje_prom);
    const fechas = data.map(obj => moment(obj.created_at).format("DD-MM-YYYY HH:mm:ss"));
    // Obtener una referencia al elemento canvas del DOM
    const $grafica = document.querySelector("#grafica");
    // Las etiquetas son las que van en el eje X. 
    // Podemos tener varios conjuntos de datos. Comencemos con unog
    new Chart($grafica, {
        type: 'line',// Tipo de gráfica
        data: {
            labels: fechas,
            datasets: [
                {
                data: voltaje_prom,
                borderColor: "#F5E92C",
                fill: false,
                label: 'pH',
                },
            ]
        },
        // options: {
        //     display: true,
        //     scales: {
        //         yAxes: [{
        //             ticks: {
        //                 beginAtZero: true
        //             }
        //         }],
        //     },
        // }


        options: {
            responsive: true,
            plugins: {
              legend: {
                position: 'top',
              },
              title: {
                display: true,
                text: 'Chart.js Line Chart'
              }
            }
          }
    });
    })
  .catch(error => {
    console.error('Error:', error);
  });

 