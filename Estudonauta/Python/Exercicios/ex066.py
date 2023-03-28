cont = soma = 0
while True:
    print('999 para encerrar!')
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'O programa contou {cont} numeros inseridos e a soma deles é {soma}.')