from datetime import date
anoatual = date.today().year
nasc = int(input('Qual ano você nasceu? '))
idade = anoatual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, anoatual))
if idade < 18:
    tempo = 18 - idade
    print('Ainda falta {} anos para o alistamento.'.format(tempo))
    alistar = anoatual + tempo
    print('Seu alistamento sera em {}'.format(alistar))
elif idade > 18:
    tempo = idade + 18
    print('Já passou {} anos para o alistamento.'.format(tempo))
    alistar = anoatual - tempo
    print('Seu alistamento foi em {}.'.format(alistar))
else:
    print('Você deve se alistar IMEDIATAMENTE!')
