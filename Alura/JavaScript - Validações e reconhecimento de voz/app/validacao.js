function verificaSeChutePossuiValorValido(chute) {
    const numero = +chute;

    if (validaNumero(numero)) {
        elementoChute.innerHTML += '<div>Valor Invalido!</div>';
    }

    if (numeroMaiorOuMenor(numero)) {
        elementoChute.innerHTML += `<div>Valor Invalido! O número precisa estar entre o ${menorValor} e ${maiorValor}</div>`
    }

    if (numero === numeroSecreto) {
        document.body.innerHTML = `
            <h2>Você acertou!</h2>
            <h3>O Número Secreto era ${numeroSecreto}.</h3>    
        `
    }
}

function validaNumero(numero) {
    return Number.isNaN(numero)
}

function numeroMaiorOuMenor(numero){
    return numero > maiorValor || numero < menorValor
}