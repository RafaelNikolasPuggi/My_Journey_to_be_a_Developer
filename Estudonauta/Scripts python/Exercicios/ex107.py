import modulos

preço = float(input('Digite o preço: R$'))
taxa = float(input('Digite a taxa: %'))
print(f'A metade de R${preço} é R${modulos.metade(preço)}')
print(f'O dobro de R${preço} é R${modulos.dobro(preço)}')
print(f'O preço de {preço} com o acrescimo de {taxa}% o valor fica {modulos.aumentar(preço, taxa)}')
print(f'O preço de {preço} com o desconto de {taxa}% o valor fica {modulos.dimiuir(preço, taxa)}')