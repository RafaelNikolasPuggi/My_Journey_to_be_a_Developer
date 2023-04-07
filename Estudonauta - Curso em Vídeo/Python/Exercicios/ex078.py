valor = []
maior = 0
menor = 0
for cont in range(0, 5):
    valor.append(int(input(f'Digite um valor para a {cont + 1}ª possição: ')))
    if cont == 0:
        maior = menor = valor[cont]
    else:
        if valor[cont] > maior:
            maior = valor[cont]
        if valor[cont] < menor:
            menor = valor[cont]
print(f'Os valores digitados foram: {valor}')
print(f'O menor valor digitado foi {menor} na posição ', end='')
for i, v in enumerate(valor):
    if v == menor:
        print(f'{i + 1}...', end='')
print()
print(f'O maior valor digitado foi {maior} na posição ', end='')
for i, v in enumerate(valor):
    if v == maior:
        print(f'{i + 1}...', end='')
print()

