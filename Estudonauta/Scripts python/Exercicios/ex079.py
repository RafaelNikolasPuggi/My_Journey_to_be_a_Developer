valores = []
while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso!')
        print('-' * 30)
    else:
        print('Valor dublicado! Não irei adicionar.')
        print('-' * 30)
    sn = str(input('Quer continuar? ')).upper().strip()
    print('-' * 30)
    if sn == 'N':
        break
print(f'Você digitou os valores {sorted(valores)}')
