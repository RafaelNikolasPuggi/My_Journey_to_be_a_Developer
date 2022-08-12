import random
from time import sleep
comp = random.randint(0, 10) #Faz o computador gerar aleatorio.
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 10. Tente advinhar...')
print('-=-' *20)
print('Hm...')
sleep(3)
jog = int(input('Em qual numero eu pensei? '))
erro = 1
while jog != comp:
    erro += 1
    if jog > comp:
        jog = int(input('Haha! Errou! Tenta pra menos: '))
    elif jog < comp:
        jog = int(input('Haha! Errou! Tenta pra mais: '))
print('Parabens, você ganhou na {}ª tentativa.'.format(erro))

