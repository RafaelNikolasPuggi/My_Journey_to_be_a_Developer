const form = (document.querySelector('#novoItem'));
const lista = document.querySelector('.lista');


form.addEventListener('submit', (event) => {
    event.preventDefault();

    criaElemento(event.target.elements['nome'].value, event.target.elements['quantidade'].value)
})

function criaElemento(nome, quantidade) {

    const novoItem = document.createElement('li');
    novoItem.classList.add('item');

    const numeroItem = document.createElement('strong');
    numeroItem.innerHTML = quantidade;

    novoItem.appendChild(numeroItem);
    novoItem.innerHTML += nome;

    const lista = document.querySelector('.lista');
    lista.appendChild(novoItem);
}