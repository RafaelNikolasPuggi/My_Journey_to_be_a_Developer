import { conectaApi } from "./conectaAPI.js";
import constroiCard from "./mostrarVideos.js";

async function buscarVideo(evento) {
    evento.preventDefault();

    const dadosDePesquisa = document.querySelector('[data-pesquisa]').value;
    const busca = await conectaApi.buscaVideo(dadosDePesquisa);

    const lista = document.querySelector('[data-lista]');

    while (lista.lastChild){
        lista.removeChild(lista.lastChild);
    }

    busca.forEach(element => {
        lista.appendChild(constroiCard
            (element.titulo, element.descricao, element.url, element.imagem))
    });

    if (busca.length == 0) {
        lista.innerHTML = `<h2 class='mensagem__titulo'>Não existem videos com esses termos.</h2>`
    }
}

const botaoDePesquisa = document.querySelector('[data-botao-pesquisa]');
botaoDePesquisa.addEventListener('click', evento => buscarVideo(evento));