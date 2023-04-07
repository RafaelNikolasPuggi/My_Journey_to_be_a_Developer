time = []
dados = {}
partidas = []
while True:
    dados.clear()
    partidas.clear()
    dados['nome'] = str(input('Nome do jogador: ')).strip().capitalize()
    tot = int(input(f'Quantas partidas o jogador {dados["nome"]} jogou? '))
    for c in range(0, tot):
        partidas.append(int(input(f'    Quantos gols na {c + 1}º partida? ')))
    dados['gols'] = partidas[:]
    dados['soma'] = sum(partidas)
    time.append(dados.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Apenas S ou N.')
    if resp == 'N':
        break
print('=-' * 30)
print('cod', end=' ')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(time):
    print(f'{k:>4}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('=-' * 30)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com esse codigo {busca}!')
    else:
        print(f'--Levantamento do jogardor {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i + 1}º fez {g} gols.')
        print('=-' * 30)
print('Volte sempre.')