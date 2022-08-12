valor = float(input('Valor do produto: '))
pagamento = str(input('Como vai pagar? '))
parcela = int(input('Vai pagar de quantas vezes? '))
if pagamento == 'dinheiro' or pagamento == 'cheque' and parcela == 0:
    novovalor = valor - (valor * 0.10)
elif pagamento == 'cartao' and parcela == 0:
    novovalor = valor - (valor * 0.05)
elif pagamento == 'cartao' and parcela == 1 or parcela == 2:
    novovalor = valor
elif pagamento == 'cartao' and parcela >= 3:
    novovalor = valor + (valor * 0.20)
print('O valor do pagamento com {} fica no total de {:.2f}'.format(pagamento, novovalor))
