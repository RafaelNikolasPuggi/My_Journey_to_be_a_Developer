from datetime import date
totalmaior = 0
totalmenor = 0
for pessoa in range (1, 8):
    ano = int(input('Ano de nascimento da {}ª pessoa: '.format(pessoa)))
    idade = date.today().year - ano
    print('A {}º pessoa tem {} anos'.format(pessoa, idade))
    if idade < 18:
        totalmenor += 1
    else:
        totalmaior += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totalmaior))
print('E ao todo tivemos {} pessoas menores de idade'.format(totalmenor))

