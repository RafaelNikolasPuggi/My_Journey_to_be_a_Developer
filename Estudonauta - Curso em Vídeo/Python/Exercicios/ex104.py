def LeiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'\033[;31mERRO! DIGITE UM NÚMERO INTEIRO VÁLIDO.\033[m')
        if ok:
            break
    return valor


n = LeiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
