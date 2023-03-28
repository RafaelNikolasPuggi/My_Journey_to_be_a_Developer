'''nome = str(input('Qual seu nome? '))
if nome == 'Rafael':
    print('Que nome lindo!')
else:
    print('Que nome simples!')
print('Bom dia, {}!'.format(nome))'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua media foi {:.2f}'.format(m))
print('Parabéns, sua media foi boa!' if m >= 6 else 'Sua media foi ruim, estude mais!')

