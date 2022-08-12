n = 0
r = ''
soma = 0
divisor = 0
media = 0
maior = 0
menor = 0
while r != 'N':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]: ')).upper().strip()
    while r != 'S' and r != 'N':
        r = str(input('Não entendi, quer continuar? [S/N] ')).upper().strip()
    soma += n
    divisor += 1
    if divisor == 1:
        maior = menor = n
    else:
        if maior < n:
            maior = n
        if menor > n:
            menor = n
media = soma / divisor
print('A média dos valores é igual a {}'.format(media))
print('O maior valor é {} e o menor valor é {}'.format(maior, menor))


