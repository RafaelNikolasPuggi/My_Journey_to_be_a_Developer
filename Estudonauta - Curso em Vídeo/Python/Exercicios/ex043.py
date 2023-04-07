peso = float(input('Qual o seu peso? '))
altura = float(input('Qual sua altura? '))
imc = peso / (altura * altura)
print('O seu IMC é {:.1f}'.format(imc))
if imc < 18.5:
    print ('Você está abaixo do peso.')
elif imc < 25:
    print('Você está com o peso ideal.')
elif imc < 30:
    print('Você está com sobrepeso.')
elif imc < 40:
    print('Você está obeso.')
else:
    print('Você está com obesidade morbida.')

