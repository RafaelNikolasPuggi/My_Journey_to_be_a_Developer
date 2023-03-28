num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversão:
[1] Binario
[2] Octal
[3] Hexadecimal ''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('O numero {} convertido para Binario é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print ('O numero {} convertido para Octal é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print ('O numero {} convertido para Hexadecimal é igual a {}'. format(num, hex(num)[2:]))
else:
    print('Opção invalida, tente novamente!')