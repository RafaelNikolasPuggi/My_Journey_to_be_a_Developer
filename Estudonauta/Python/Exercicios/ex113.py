def LeiaInt(msg):
   while True:
       try:
           n = int(input(msg))
       except (ValueError, TypeError):
            print(f'\033[;31mERRO! DIGITE UM NÚMERO INTEIRO VÁLIDO.\033[m')
            continue
       except KeyboardInterrupt:
           print('Entrada de dados interrompida pelo usuário.')
           return 0
       else:
           return n


def LeiaFloat(msg):
    while True:
        try:
            f = float(input(msg))
        except (ValueError, TypeError):
            print(f'\033[;31mERRO! DIGITE UM NÚMERO INTEIRO VÁLIDO.\033[m')
            continue
        else:
            return f


n = LeiaInt('Digite um número inteiro: ')
f = LeiaFloat('Digite um numero real: ')
print(f'O número inteiro foi {n} e o número real foi {f}')