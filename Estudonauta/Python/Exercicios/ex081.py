lista = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    res = str(input('Quer continuar? ')).upper().strip()
    if res == 'N':
        break
lista.sort(reverse=True)
print(f'Foram digitados {len(lista)} numeros.')
print(f'A ordem decrescente da lista fica {lista}')
if 5 in lista:
    print('O numero 5 está na lista.')
else:
    print('O numero 5 NÃO está na lista.')