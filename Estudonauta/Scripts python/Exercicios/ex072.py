cont = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
        'Onze', 'Doze,', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
        n = int(input('Digite um numero entre 0 e 20: '))
        if 0 <= n <= 20:
                break
        print('Tente novamente!', end= ' ')
print(f'Você digitou o numero {cont[n]}')
