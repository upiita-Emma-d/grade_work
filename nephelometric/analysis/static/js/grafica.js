const input_port = document.querySelector('#my-text-box');
const chart_general  = document.querySelector('#chart_div');
const API_LOCAL = 'http://localhost:8000';

function fetchData(urlApi){
  fetch(urlApi)
    .then(response => response.json())
    .then(data => {
      console.log(data);
      return data
    })
  // const response = await fetch(urlApi);
  // const data = await response.json();
  // return data
}
console.log(fetchData(`${API_LOCAL}/boards`));

const obtain_boards_aviable = (urlApi) =>{
  try {
    const optionList = fetchData(`${urlApi}/boards`);
    console.log(optionList);
    return optionList.ports_aviable;
  }catch (error){
    console.log(error)
    return ["Not boards avible"];
  }

}

// optionList = ["COM1", "COM2", "COM3", "COM4"];
var optionList = obtain_boards_aviable(API_LOCAL);
console.log("Option list");
console.table(optionList);

function fillDataList() {
    var container = document.getElementById('my-text-box'),
    i = 0,
    len = optionList.length,
    dl = document.createElement('datalist');

    dl.id = 'puertos';
    
    optionList.forEach(option => {
      var optionhtml = document.createElement('option');
      optionhtml.value = option;
      dl.appendChild(optionhtml);
      
    });
    container.appendChild(dl);
}
fillDataList();

input_port.addEventListener('change', updateValue);

function updateValue() {
  console.log(this.value)
}

