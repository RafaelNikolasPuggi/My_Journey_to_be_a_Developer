frase = str(input('Digite um frase: ')).upper().strip()
print('Quantos vezes a letra A aparece? {} '.format((frase.count('A'))))
print('Em que posição ela aparece pela primeira vez? {}'.format(frase.find('A')))
print('Em que posição ela aparece pela ultima vez? {}'.format(frase.rfind('A')))