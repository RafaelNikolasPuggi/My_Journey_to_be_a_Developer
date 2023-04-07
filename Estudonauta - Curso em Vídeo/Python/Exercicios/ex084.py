pessoa = list()
galera = list()
maior = menor = 0
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    if len(galera) == 0:
        maior = menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        if pessoa[1] < menor:
            menor = pessoa[1]
    galera.append(pessoa[:])
    pessoa.clear()
    res = str(input('Quer continuar? [S/N] ')).strip().upper()
    if res == 'N':
        break
print(f'Foram cadastradas o total de {len(galera)} pessoas.')
print(f'O maior peso foi de {maior:.3f}Kg', end=' ')
for p in galera:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {menor:.3f}Kg', end=' ')
for p in galera:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')
print()

