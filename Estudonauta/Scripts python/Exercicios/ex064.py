n = 0
ndig = 0
soma = 0
while n != 999:
    n = int(input('Digite um numero inteiro [999 para parar]: '))
    ndig += 1
    soma += n
ndig -= 1
soma -= 999
print('Foram {} numeros registrados e a soma entre eles é igual a {}'.format(ndig, soma))