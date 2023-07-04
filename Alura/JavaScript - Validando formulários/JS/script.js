import ehUmCpf from "./valida-cpf";

const camposDoFormulario = document.querySelectorAll('[required]');

camposDoFormulario.forEach((campo) => {
    campo.addEventListener('blur', () => verificarCampo(campo));
})

function verificarCampo(campo){
    if (campo.name == 'cpf' && campo.value.lenght >= 11){
        ehUmCpf(campo);
    }
}