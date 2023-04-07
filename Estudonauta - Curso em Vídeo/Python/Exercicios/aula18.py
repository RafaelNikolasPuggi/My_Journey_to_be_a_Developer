'''teste = list()
teste.append('Rafael')
teste.append(25)
galera = list()
galera.append(teste[:])
teste[0] = 'Marina'
teste[1] = 24
galera.append(teste[:])
print(galera)'''

'''galera = [['João', 23], ['Maria', 25], ['Joaquim', 33], ['Josefino', 42], ['Robersvaldo', 12]]
for p in galera:
    print(f'O {p[0]} tem {p[1]} anos de idade.')'''

galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f'O {p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'O {p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maior de idade e {totmen} menor de idade.')