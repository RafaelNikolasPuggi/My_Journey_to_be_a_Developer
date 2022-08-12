num = int(input('Digite um numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o numero!')
print(' Unidade: {} \n Dezena: {} \n Centena: {} \n Milhar: {}'.format(u, d, c, m))
