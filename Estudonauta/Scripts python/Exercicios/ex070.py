totalgasto = pmm = menorpreço = cont = 0
pmb = ' '
while True:
    produto = str(input('Qual o nome do produtor? '))
    preço = float(input('Qual foi o preço? R$'))
    cont += 1
    totalgasto += preço
    if preço >= 1000:
        pmm += 1
    if cont == 1 or preço < menorpreço:
        menorpreço = preço
        pmb = produto
    sn = ' '
    while sn not in 'SN':
        sn = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if sn == 'N':
        break
print(f'A compra deu o total de R${totalgasto:.2f}')
print(f'A quantidade de produtos que custaram mais de R$1000.00 são {pmm}')
print(f'O nome do produto mais barato é {pmb} que custa {menorpreço}')
