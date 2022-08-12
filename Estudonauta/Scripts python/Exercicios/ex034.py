salario = float(input('Digite o salario do funcionario: '))
if salario <= 1250.00:
    ajuste = (salario * 0.15) + salario
    print('O ajuste do salario foi para R${:.2f}'.format(ajuste))
else:
    ajuste = (salario * 0.10) + salario
    print('O ajuste do salrio foi para R${:.2f}'.format(ajuste))
