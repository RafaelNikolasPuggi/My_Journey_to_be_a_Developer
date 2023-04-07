km = float(input('Quantos KM de viagem? '))
pas = km * 0.50 if km <= 200 else km * 0.45
'''if km <= 200:
    pas = km * 0.50
else:
    pas = km * 0.45'''
print('O valor da passagem é R${:.2f}'.format(pas))