from random import randint
from time import sleep
números = []

def sorteio():
    print('Sorteando 5 valores para a lista:', end=' ')
    for i in range(0, 5):
        sleep(0.3)
        n = randint(0, 10)
        números.append(n)
        print(f'{n}', end=' ')
    print('Pronto!')
    return True

def somar():
    somapar = 0
    for n in números:
        if n % 2 == 0:
            somapar += n
    print(f'O valor dos números pares somados é {somapar}')
    return True

sorteio()
print(somar())


