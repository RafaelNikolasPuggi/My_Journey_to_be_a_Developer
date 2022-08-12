while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    print('_' * 40)
    for c in range (1, 11):
        print(f'{n} x {c} = {n * c}')
        c += 1
    print('_' * 40)
print('Programa tabuada encerrado.')