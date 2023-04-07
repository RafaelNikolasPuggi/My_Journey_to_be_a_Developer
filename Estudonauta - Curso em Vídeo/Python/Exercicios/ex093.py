dados = {}
partidas = []
dados['nome'] = str(input('Nome do jogador: ')).strip().capitalize()
tot = int(input(f'Quantas partidas o jogador {dados["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'    Quantos gols na {c + 1}º partida? ')))
dados['gols'] = partidas[:]
dados['soma'] = sum(partidas)
print('=-' * 30)
print(dados)
print('=-' * 30)
for k, v in dados.items():
    print(f'O campo {k} tem valor {v}')
print('=-' * 30)
print(f'O jogador {dados["nome"]} jogou {len(dados["gols"])} partidas.')
for i, v in enumerate(dados['gols']):
    print(f'Na partida {i + 1}, fez {v} gols.')
print(f'Foi um total de {dados["soma"]} gols')