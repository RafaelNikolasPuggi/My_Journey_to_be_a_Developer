print('=-=' * 20)
def maior(* num):
    cont = maior = 0
    print(f'Analisando o valores passados:')
    for n in num:
        print(f'{n}', end=' ')
        if n == 0:
            maior = n
        else:
            if n > maior:
                maior = n
        cont += 1
    print()
    print(f'O maior valor é {maior} entre {cont} valores encontrados.')
    print('=-=' * 20)


maior(100, 2, 3, 4, 9, 5, 54, 16, 98)