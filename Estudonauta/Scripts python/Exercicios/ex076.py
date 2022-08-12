listagem = ('Lapis', 1.75,
            'Borracha', 0.50,
            'Caderno', 10,
            'Estojo', 5.70,
            'Mochila', 70,
            'Compaso', 8.20,
            'Caneta', 2,
            'Livro', 20)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end=' ')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-' * 40)