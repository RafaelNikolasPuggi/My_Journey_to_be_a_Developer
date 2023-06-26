var logradouro = document.getElementById('endereco');
var bairro = document.getElementById('bairro');
var cidade = document.getElementById('cidade');
var estado = document.getElementById('estado');

async function buscaEndereco(cep) {
    var mensagemErro = document.getElementById('erro');
    mensagemErro.innerHTML = '';
    try {
        var consultaCEP = await fetch(`https://viacep.com.br/ws/${cep}/json/`);
        var consultaCEPconvertido = await consultaCEP.json();
        if (consultaCEPconvertido.erro) {
            throw Error;
        }

        logradouro.value = consultaCEPconvertido.logradouro;
        bairro.value = consultaCEPconvertido.bairro;
        cidade.value = consultaCEPconvertido.localidade;
        estado.value = consultaCEPconvertido.uf;

        //console.log(consultaCEPconvertido);
        return consultaCEPconvertido;
    } catch (erro) {
        if (cep.length !== 8) { // Verifica se o CEP tem 8 dígitos
            mensagemErro.innerHTML = `<p>O CEP deve ter exatamente 8 dígitos.</p>`;
        } else if (!/^[0-9]+$/.test(cep)) { // Verifica se o CEP contém apenas números
            mensagemErro.innerHTML = `<p>O CEP deve conter apenas números.</p>`;
        } else {
            // O CEP é válido
            mensagemErro.innerHTML = `CEP inexistente!`;
        }
    }

}

var cep = document.querySelector('#cep');
cep.addEventListener("focusout", () => limparCampos()); //Limpa os campos 
cep.addEventListener('focusout', () => buscaEndereco(cep.value));

function limparCampos() {
    cidade.value = "";
    logradouro.value = "";
    estado.value = "";
    bairro.value = "";
};