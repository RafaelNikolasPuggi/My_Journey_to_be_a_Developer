lista = []
lista_par = []
lista_impar = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    resp = str(input('Quer continuar? ')).upper().strip()
    if resp == 'N':
        break
for c in lista:
    if c % 2 == 0:
        lista_par.append(c)
    else:
        lista_impar.append(c)
print(f'A lista principal ficou com os valores: {lista}')
if lista_par == []:
    print('Não tem nenhum valor atribuido a lista PAR.')
else:
    print(f'A lista PAR tem os seguintes valores atribuidos: {lista_par}')
if lista_impar == []:
    print('Não tem nenhum valor atribuido a lista IMPAR.')
else:
    print(f'A lista IMPAR tem os seguintes valores atribuidos: {lista_impar}')