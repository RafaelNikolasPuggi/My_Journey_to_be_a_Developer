#Função que calcula área

def área(l, c):
    a = l * c
    print(f'A área de um terreno é {l}x{c} é de {a:.1f}m²')

#Principal
print('Controle de terreno.')
print('=-' * 20)
l = float(input('Largura(m): '))
c = float(input('Comprimento(m): '))
área(l, c)
