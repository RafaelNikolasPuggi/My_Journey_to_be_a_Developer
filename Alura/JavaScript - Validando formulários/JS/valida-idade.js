const dataAtual = new Date();

export default function ehMaiorDeIdade(campo) {
    const dataNascimento = new Date(campo.value);
    if (!validaIdade(dataNascimento) || validaAnoNascimento(dataNascimento)) {
        campo.setCustomValidity('O usuário precisa ser maior de 18 anos de idade.')
    }
}

function validaIdade(data) {
    const dataMais18 = new Date(data.getUTCFullYear() + 18, data.getUTCMonth(), data.getUTCDate());

    return dataAtual >= dataMais18;
}
