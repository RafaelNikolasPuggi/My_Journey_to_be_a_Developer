'''num = [2, 4, 5, 6, 0, 10, 30, 8]
num[2] = 76
num.append(1)
num.sort(reverse=True)
num.insert(3, 53)
if 4 in num:
    num.remove(4)
else:
    print('Não achei o numero 4')
print(num)
print(f'Essa lista tem {len(num)} elementos.')'''

valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')
