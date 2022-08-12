contF = contM = tot18 = Fmenor20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        contM += 1
    else:
        contF += 1
    if idade < 20 and sexo == 'F':
        Fmenor20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total de pessoas maiores de 18 anos são {tot18}')
print(f'Foram cadastrados {contM} homens no total.')
print(f'Foram cadastradas {Fmenor20} mulheres com menos de 20 anos.')

print('Acabou!')

