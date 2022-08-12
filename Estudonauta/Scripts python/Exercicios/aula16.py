lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
#Tuplas são imutaveis
for comida in lanche:
    print(f'Eu vou comer {comida}')
for comida in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[comida]}')
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('EU comi pra caramba!')