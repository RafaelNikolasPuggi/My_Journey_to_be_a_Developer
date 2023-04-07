import modulos

preço = float(input('Digite o preço: R$'))
taxa = float(input('Digite a taxa: %'))
print(f'A metade de {modulos.moeda(preço)} é {modulos.moeda(modulos.metade(preço))}')
print(f'O dobro de {modulos.moeda(preço)} é {modulos.moeda(modulos.dobro(preço))}')
print(f'O preço de {modulos.moeda(preço)} com o acrescimo de {taxa}% o valor fica {modulos.moeda(modulos.aumentar(preço, taxa))}')
print(f'O preço de {modulos.moeda(preço)} com o desconto de {taxa}% o valor fica {modulos.moeda(modulos.dimiuir(preço, taxa))}')