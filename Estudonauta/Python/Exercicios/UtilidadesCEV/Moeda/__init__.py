def aumentar(preço=0, taxa=0, format=False):
    res = preço + (preço * taxa / 100)
    return res if format is False else moeda(res)


def dimiuir(preço=0, taxa=0, format=False):
    res = preço - (preço * taxa / 100)
    return res if format is False else moeda(res)


def dobro(preço=0, format=False):
    res = preço * 2
    return res if format is False else moeda(res)


def metade(preço=0, format=False):
    res = preço / 2
    return res if format is False else moeda(res)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')


def resumo(preço=0, taxa=0):
    print('=-=' * 15)
    print(f'Analisando o preço R${preço:.2f} com taxa de {taxa:.0f}%'.center(30))
    print('=-=' * 15)
    print(f'A metade é {metade(preço, True)}\t')
    print(f'O dobro é {dobro(preço, True)}\t')
    print(f'Com acrescimo fica {aumentar(preço, taxa, True)}\t')
    print(f'Com desconto fica {dimiuir(preço, taxa, True)}\t')
    print('=-=' * 15)
    return True
