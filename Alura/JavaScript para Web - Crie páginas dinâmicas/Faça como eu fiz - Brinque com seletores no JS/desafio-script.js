const botoesTeclado = document.querySelectorAll('.botao-teclado');

botoesTeclado.forEach(botao => {
    botao.addEventListener('click', () => {
        const valorBotao = botao.value;
        document.getElementById('valor-selecionado').textContent = valorBotao;
    });
});
