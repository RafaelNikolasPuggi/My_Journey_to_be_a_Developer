pessoas = {}
lista = []
mulher = []
media_idade = soma_idade = 0
while True:
    pessoas['nome'] = str(input('Nome: ')).capitalize()
    pessoas['idade'] = int(input('Idade: '))
    soma_idade += pessoas['idade']
    pessoas['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()
    if pessoas['sexo'] == 'F':
        mulher.append(pessoas['nome'])
    while pessoas['sexo'] not in 'MF':
        pessoas['sexo'] = str(input('ERRO! Digite somente "M" ou "F": ')).upper().strip()
    lista.append(pessoas.copy())
    resp = str(input('Quer continuar [S/N]? ')).upper().strip()
    while resp not in 'SN':
        resp = str(input('ERRO! Digite somente "S" ou "N": ')).strip().upper()
    if resp == 'N':
        break
media_idade = soma_idade / len(lista)
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')
print(f'B) A media de idade é {media_idade:.0f} anos.')
print(f'C) As mulheres cadastradas foram: ', end='')
for i, m in enumerate(mulher):
    print(f'{m}; ', end='')
print()
print(f'D) Lista das pessoas que estão acima da media:')
for p in lista:
    if p['idade'] >= media_idade:
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('Encerrado!')
