const input_port = document.querySelector('#my-text-box');
const chart_general  = document.querySelector('#chart_div');
const API_LOCAL = 'http://localhost:8000';

function fillDataList(arrayOptions) {
  var container = document.getElementById('my-text-box'),
  dl = document.createElement('datalist');
  dl.id = 'puertos';

  arrayOptions.forEach(option => {
    var optionHTML = document.createElement('option');
    optionHTML.value = option;
    dl.appendChild(optionHTML);
  });
  container.appendChild(dl);
}

async function fetchData(urlApi){
  // fetch(urlApi)
  //   .then(response => response.json())
  //   .then(data => {
  //     console.log(data);
  //     return data
  //   })
  const response = await fetch(urlApi);
  const data = await response.json();
  console.log(data);
  fillDataList(data)
}

fetchData(`${API_LOCAL}/boards`);

// const obtain_boards_aviable = (urlApi) =>{
//   try {
//     const optionList = fetchData();
//     console.log(optionList);
//     return optionList.ports_aviable;
//   }catch (error){
//     console.log(error)
//     return ["Not boards avible"];
//   }

// }

// optionList = ["COM1", "COM2", "COM3", "COM4"];
// var optionList = obtain_boards_aviable(API_LOCAL);

input_port.addEventListener('change', updateValue);

function updateValue() {
  console.log(this.value)
}

