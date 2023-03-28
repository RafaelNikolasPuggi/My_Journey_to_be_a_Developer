nome = str(input('Digite seu nome completo: ')).strip()
nomep = nome.split()
print('Seu primeiro nome é: {}'.format(nomep[0]))
print('Seu ultimo nome é: {}'.format(nomep[len(nomep)-1]))
