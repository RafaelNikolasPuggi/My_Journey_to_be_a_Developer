function botoes () {
    document.querySelector(".teclado input[type=button]");
}

botoes.forEach(botao => {
    botao.addEventListener('click', () => {
        const valorBotao = botao.value;
    });
});

document.getElementById('telefone').value += valorBotao;

