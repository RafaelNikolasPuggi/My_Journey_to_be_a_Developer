import random
from time import sleep
comp = random.randint(0, 5) #Faz o computador gerar aleatorio.
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5. Tente advinhar...')
print('-=-' *20)
print('Processando...')
sleep(3)
jog = int(input('Em qual numero eu pensei? '))
if jog == comp:
    print('Parabens, você ganhou!')
else:
    print('Haha! Ganhei! Escolhi o {} e não {}!'.format(comp, jog))

