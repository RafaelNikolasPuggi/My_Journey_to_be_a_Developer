valorcasa = float(input('Qual o valor da casa que quer comprar? '))
salario = float(input('Quanto é o seu salario? '))
anos = int(input('Quantos anos pretende pagar? '))
prestação = valorcasa / (anos * 12)
mínimo = salario * 0.30
print('Para pagar uma casa de R${:.2f} em {} anos a prestação sera de R${:.2f}'.format(valorcasa, anos, prestação))
if prestação > mínimo:
    print('Não vai dar não')
else: print('Deu bom pra tu!')

