function verificaSeChutePossuiValorValido(chute) {
    const numero = parseInt(chute);

    if (isNaN(numero)) {
        elementoChute.innerHTML += '<div>Valor Invalido!</div>';
    }

    if (numero > maiorValor || numero < menorValor) {
        elementoChute.innerHTML += `<div>Valor Invalido! O número precisa estar entre o ${menorValor} e ${maiorValor}</div>`
    }

    if (numero === numeroSecreto) {
        document.body.innerHTML = `
            <h2>Você acertou!</h2>
            <h3>O Número Secreto era ${numeroSecreto}.</h3>
            
            <button id="jogar-novamente" class="btn-jogar">Jogar Novamente </button>
        `
    }else if (numero > numeroSecreto) {
        elementoChute.innerHTML += `<div>O número secreto  é menor <i class="fa-solid fa-down-long"></div>`
    }else {
        elementoChute.innerHTML += `<div>O número secreto  é maior <i class="fa-solid fa-up-long"></div>`
    }
}

document.body.addEventListener('click', (event) => {
    if (event.target.id =='jogar-novamente') {
        window.location.reload();
    }
})
