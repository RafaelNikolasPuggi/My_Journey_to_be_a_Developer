from time import sleep
n1 = int(input('Digite um valor: '))
n2 = int(input(('Digite outro valor: ')))
print('-*-' * 10)
opção = 0
soma = 0
mult = 0
maior = 0
while opção != 5:
    print('Os valores são \033[31m{}\033[m e \033[31m{}\033[m'.format(n1, n2))
    print('''*--------COMANDOS--------*
    [ 1 ] Somar
    [ 2 ] Mutiplicar
    [ 3 ] Maior
    [ 4 ] Novos numeros
    [ 5 ] SAIR''')
    opção = int(input('Escolha um comando: '))
    print('-*-' * 10)
    if opção == 1:
        soma = n1 + n2
        print('A soma dos valores \033[33m{}\033[m e \033[33m{}\033[m é igual a: \033[35m{}\033[m'.format(n1, n2, soma))
        print('-*-' * 10)
    elif opção == 2:
        mult = n1 * n2
        print('O resultado da multiplicação dos valores \033[33m{}\033[m e \033[33m{}\033[m é igual a: \033[35m{}\033[m'.format(n1, n2, mult))
        print('-*-' * 10)
    elif opção == 3:
        if n1 > n2:
            print('O \033[33m{}\033[m é maior que \033[33m{}\033[m'.format(n1, n2))
            print('-*-' * 10)
        elif n2 > n1:
            print('O \033[33m{}\033[m é maior que \033[33m{}\033[m'.format(n2, n1))
            print('-*-' * 10)
        else:
            print('Os dois são iguais!')
            print('-*-' * 10)
    elif opção == 4:
        n1 = int(input('Digite um novo valor: '))
        n2 = int(input('Digite outro valor novo: '))
        print('-*-' * 10)
    elif opção == 5:
        print('Finalizando programa...')
        sleep(2)
    else:
        print('Opção invalida, tente novamente.')
        print('-*-' * 10)
print('Programa finalizado!')



