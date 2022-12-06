const input_port = document.querySelector('#puerto');
const chart_general  = document.querySelector('#chart_div');

input_port.addEventListener('change', updateValue);

function updateValue() {
  console.log(this.value)
}

