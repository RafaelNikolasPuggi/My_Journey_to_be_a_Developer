altura = float(input('Qual a altura da parede? '))
largura = float(input('Qual a largura da parede? '))
area = largura * altura
print('A sua parede tem uma dimenssão de {}x{} e sua área é de {}m².'.format(altura, largura, area))
tinta = area / 2
print('A quantidade de tinta necessaria será : {}L'.format(tinta))
