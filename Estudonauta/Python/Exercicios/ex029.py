vel = int(input('Qual a velocidade do veiculo? '))
if vel <= 80:
    print('Continue assim! Digira com segurança.')
else:
    print('ATENÇÂO! Você excedeu o limete de velocidade!')
    multa = (vel - 80) * 7
    print('Você terá que pagar uma multa de R${:.2f}...'.format(multa))