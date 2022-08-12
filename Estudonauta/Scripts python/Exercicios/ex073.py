colocação = ('America-MG', 'Athletico-PR', 'Atletico-GO', 'Atletico-MG', 'Avai', 'Botafogo', 'Ceará SC', 'Conrinthians', 'Coritiba', 'Cuiabá',
             'Flamengo', 'Fluminense', 'Fortaleza', 'Goias', 'Internacional', 'Juventude', 'Palmeiras', 'Bragantino', 'Santos', 'São Paulo')
print(f'Os cinco primeiros colocados são: {colocação[:5]}')
print(f' Os quatro ultimos colocados são: {colocação[16:]}')
print(f'Em ordem alfabetica fica: {sorted(colocação)}')
print(f'O time do Atletico-MG está {colocação.index("Atletico-MG") + 1}ª posição do campeonato!')