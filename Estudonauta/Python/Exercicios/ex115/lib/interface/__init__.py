def vermelho(msg=0):
    txt = str(f'\033[1;31m{msg}\033[0;0m')
    return txt


def azul(txt=0):
    txt = str(f'\033[1;34m{txt}\033[0;0m')
    return txt


def preto(txt=0):
    txt = str(f'\033[1;30m{txt}\033[0;0m')
    return txt


def amarelo(txt=0):
    txt = str(f'\033[1;33m{txt}\033[0;0m')
    return txt


def verde(txt=0):
    txt = str(f'\033[1;32m{txt}\033[0;0m')
    return txt


def branco(txt=0):
    txt = str(f'\033[1;97m{txt}\033[0;0m')
    return txt


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


def linha(tam = 42):
    return '_' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{amarelo(c)} - {azul(item)}')
        c += 1
    print(linha())
    opc = LeiaInt(verde('Digite uma opção: '))
    return opc