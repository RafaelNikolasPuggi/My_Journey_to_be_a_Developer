import modulos

preço = float(input('Digite o preço: R$'))
taxa = float(input('Digite a taxa: %'))
print(f'A metade de {modulos.moeda(preço)} é {modulos.metade(preço, format(True))}')
print(f'O dobro de {modulos.moeda(preço)} é {modulos.dobro(preço, format(True))}')
print(f'O preço de {modulos.moeda(preço)} com o acrescimo de {taxa:.0f}% o valor fica {modulos.aumentar(preço, taxa, True)}')
print(f'O preço de {modulos.moeda(preço)} com o desconto de {taxa:.0f}% o valor fica {modulos.dimiuir(preço, taxa, True)}')