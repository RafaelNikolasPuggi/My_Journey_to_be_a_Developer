let livros = [];
const endpointDaAPI = 'https://guilhermeonrails.github.io/casadocodigo/livros.json';
const elementoParaInserirLivros = document.getElementById('livros')
getBuscarLivrosDaAPI();

async function getBuscarLivrosDaAPI() {
    const res = await fetch(endpointDaAPI);
    livros = await res.json();
    console.log(livros);
    exibirLivrosNaTela(livros);
}

function exibirLivrosNaTela(listaDeLivros) {
    listaDeLivros.forEach(livro => {
        elementoParaInserirLivros.innerHTML += 
        `<div class="livro">
        <img class="livro__imagens" src="${livro.imagem}" alt="${livro.alt}
            ${livro.alt}" />
        <h2 class="livro__titulo">
          Vue.js
          Construa aplicações incríveis
        </h2>
        <p class="livro__descricao">Caio Incau</p>
        <p class="livro__preco" id="preco">R$29,90</p>
        <div class="tags">
          <span class="tag">Front-end</span>
          <span class="tag">Back-end</span>
        </div>
      </div>`
    })
}