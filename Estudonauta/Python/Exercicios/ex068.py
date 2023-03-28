from random import randint
jogador = computador = vitoria = 0
pi = ''
print('VAMOS JOGAR PAR OU IMPAR!')
print('==' * 20)
while True:
    while pi != 'P' and pi != 'I':
        pi = str(input('Par ou Ímpar? [P/I]> ')).strip().upper()
    if pi == 'P':
        pi = 'PAR'
    else:
        pi = 'IMPAR'
    jogador = int(input('Digite um valor de 1 a 10: '))
    computador = randint(0, 10)
    print(f'O PC escolheu {computador}.')
    total = jogador + computador
    if total % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'IMPAR'
    if pi == 'PAR' and total % 2 == 0:
        vitoria += 1
        print(f'O total foi {total}, deu {resultado}')
        print(f'Você ganhou!')
        print('==' * 20)
    elif pi == 'IMPAR' and total % 2 != 0:
        vitoria += 1
        print(f'O total foi {total}, deu {resultado}')
        print(f'Você ganhou!')
        print('==' * 20)
    else:
        print(f'O total foi {total}, deu {resultado}')
        print('Você perdeu!')
        break
print('==' * 20)
print(f'Você ganhou {vitoria} partidas seguidas.')