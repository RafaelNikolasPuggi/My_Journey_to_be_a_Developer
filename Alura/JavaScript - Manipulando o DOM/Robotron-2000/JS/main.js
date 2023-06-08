// Obtém todos os elementos com o atributo data-controle e os armazena em uma lista
const controle = document.querySelectorAll('[data-controle]');

// Obtém todos os elementos com o atributo data-estatistica e os armazena em uma lista
const estatistica = document.querySelectorAll('[data-estatistica]');

// Obtém o elemento do botão com o ID botao-cor-robotron
const botaoCorRobotron = document.querySelector("#botao-cor-robotron");

// Obtém o elemento da imagem com o atributo imagemRobotron
const imagemRobotron = document.querySelector('[imagemRobotron]');

// Define um objeto com os dados das peças e seus valores correspondentes
const pecas = {
    "bracos": {
        "forca": 29,
        "poder": 35,
        "energia": -21,
        "velocidade": -5
    },
    "blindagem": {
        "forca": 41,
        "poder": 20,
        "energia": 0,
        "velocidade": -20
    },
    "nucleos": {
        "forca": 0,
        "poder": 7,
        "energia": 48,
        "velocidade": -24
    },
    "pernas": {
        "forca": 27,
        "poder": 21,
        "energia": -32,
        "velocidade": 42
    },
    "foguetes": {
        "forca": 0,
        "poder": 28,
        "energia": 0,
        "velocidade": -2
    }
};

// Define um array com as URLs das imagens do Robotron
const imagensRobotron = [
    'img/azul.png',
    'img/amarelo.png',
    'img/branco.png',
    'img/rosa.png',
    'img/preto.png',
    'img/vermelho.png'
];

// Adiciona um evento de clique a todos os elementos de controle
controle.forEach((elemento) => {
    elemento.addEventListener('click', (evento) => {
        manipulaDados(evento.target.dataset.controle, evento.target.parentNode);
        atualizaEstatistica(evento.target.dataset.peca, evento.target.dataset.controle);
    });
});

// Função para manipular os dados da peça (incrementar ou decrementar)
function manipulaDados(operacao, controle) {
    const peca = controle.querySelector('[data-contador]');
    if (operacao === "-") {
        peca.value = parseInt(peca.value) - 1;
    } else {
        peca.value = parseInt(peca.value) + 1;
    }
}

// Função para atualizar as estatísticas com base na peça e operação selecionadas
function atualizaEstatistica(peca, operacao) {
    estatistica.forEach((elemento) => {
        const valorEstatistica = parseInt(elemento.textContent);
        const valorPeca = pecas[peca][elemento.dataset.estatistica];

        if (operacao === "-") {
            elemento.textContent = valorEstatistica - valorPeca;
        } else {
            elemento.textContent = valorEstatistica + valorPeca;
        }
    });
}

// Variável para controlar o índice atual da imagem exibida
let indiceImagemAtual = 0;

// Adiciona um evento de clique ao botão para alterar a imagem do Robotron
botaoCorRobotron.addEventListener('click', () => {
    indiceImagemAtual = (indiceImagemAtual + 1) % imagensRobotron.length; // Incrementa o índice e volta ao início se ultrapassar o tamanho do array
    imagemRobotron.src = imagensRobotron[indiceImagemAtual];
});
