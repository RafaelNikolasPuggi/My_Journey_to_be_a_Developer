const listaTeclas = document.querySelectorAll('input[type=button]');
const inputTelefone = document.querySelector('input[type=tel]');

for (indice = 0; indice < listaTeclas.length; indice++) {

    const tecla = listaTeclas[indice];
    tecla.onclick = function () {
        inputTelefone.value = inputTelefone.value + tecla.value;
    }

    tecla.onkeydown = function (evento) {
        if(evento.code === "Enter" || evento.code === "Space") {
            tecla.classList.add('ativa');
        }
    }

    tecla.onkeyup = function () {
        tecla.classList.remove('ativa');
    }
}