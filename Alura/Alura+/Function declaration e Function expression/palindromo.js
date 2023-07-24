let palavra = 'urU'

palindromo(palavra);

function palindromo(palavra) {
    let letrasDaPalavraSeparadas = palavra.split('');
    let palavraInvertida = letrasDaPalavraSeparadas.reverse();
    palavraInvertida = palavraInvertida.join('')

    let palavraPolindromo =  palavra.toLowerCase() == palavraInvertida.toLowerCase() ? 'Isso é um Polindromo!' : 'Isso não é um Polindromo!';

    console.log(palavraPolindromo)
}