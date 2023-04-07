primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + 9 * razão #Décimo Termo
for c in range (primeiro, décimo + razão, razão):
    print('{}'.format(c), end=(' > '))
print('ACABOU!')
