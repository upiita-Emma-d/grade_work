
const URL = 'https://sistema-calidad-del-agua.link/get_muestra_uv/';
 
fetch(URL)
  .then(res => res.json())
  .then(data => {
    console.log(data);
    const numbers = [];
    const min_voltage = data.map(obj => obj.min_voltage);
    const max_voltage = data.map(obj => obj.max_voltage);
    const voltaje_prom = data.map(obj => obj.voltaje_prom);
    console.log(max_voltage);

    const fechas = data.map(obj => moment(obj.created_at).format("DD-MM-YYYY HH:mm:ss"));
    // Obtener una referencia al elemento canvas del DOM
    const $grafica = document.querySelector("#grafica");
    // Las etiquetas son las que van en el eje X. 
    // Podemos tener varios conjuntos de datos. Comencemos con unog
    new Chart($grafica, {
        type: 'line',// Tipo de gráfica
        data: {
            labels: fechas,
            datasets: [{
                data: min_voltage,
                borderColor: "blue",
                fill: false,
                label: 'Voltaje minimo',
                },
                {
                data: max_voltage,
                borderColor: "red",
                fill: false,
                label: 'Voltaje máximo',
                },
                {
                data: voltaje_prom,
                borderColor: "black",
                fill: false,
                label: 'Voltaje promedio',
                },
            ]
        },
        options: {
            display: true,
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }],
            },
        }
    });
    })
  .catch(error => {
    console.error('Error:', error);
  });

 