from datetime import date
anoatual = date.today().year
nasc = int(input('Data de nascimento: '))
idade = anoatual - nasc
print('Você tem {} anos.'.format(idade))
if idade <= 9:
    print('Você é um atleta MIRIM!')
elif idade <= 14:
    print('Você é um atleta INFANTIL!')
elif idade <= 19:
    print('Você é um atleta JUNIOR!')
elif idade <=25:
    print('Você é um atleta SÊNIOR!')
else:
    print('Você é um atleta MASTER!')
