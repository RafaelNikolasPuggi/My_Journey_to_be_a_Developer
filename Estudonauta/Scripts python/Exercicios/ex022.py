nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome!')
print('Seu nome em maiuscula fica: {}'.format(nome.upper()))
print('Seu nome em minuscula fica: {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras!'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras!'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e tem {} letras!'.format(separa[0], len(separa[0])))

