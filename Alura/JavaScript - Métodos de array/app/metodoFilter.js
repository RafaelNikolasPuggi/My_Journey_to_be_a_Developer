const btnFiltrarLivrosDeFront = document.getElementById('btnFiltrarLivrosDeFront');

btnFiltrarLivrosDeFront.addEventListener('click', filtrarLivrosDeFront());

function filtrarLivrosDeFront() {
    let livrosFiltrados = livros.filter(livro => livro.categoria == 'front-end');
    console.table(livrosFiltrados);
}