pessoas = {'nome': 'Rafael', 'idade': 25, 'sexo': 'M'}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos e é do sexo {pessoas["sexo"]}')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print('=-=' * 30)
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('=-=' * 30)
del pessoas['sexo']
pessoas['nome'] = 'Gustavo'
pessoas['peso'] = 89.3
print(pessoas)
print('=-=' * 30)
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[1]['sigla'])
print('=-=' * 30)
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')