from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('-=-' * 7)
print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
print('-=-' * 7)
jogador = int(input('Sua jogada: '))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=-' * 7)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
print('O computador escolheu {}'.format(itens[computador]))
if computador == 0:
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('VOCÊ GANHOU!')
    elif jogador == 2:
        print('VOCÊ PERDEU!')
    else:
        print('Jogada Invalida.')
if computador == 1:
    if jogador == 0:
        print('VOCÊ PERDEU!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('VOCÊ GANHOU!')
    else:
        print('Jogada Invalida.')
if computador == 2:
    if jogador == 0:
        print('VOCÊ GANHOU!')
    elif jogador == 1:
        print('VOCÊ PERDEU!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('Jogada Invalida.')

