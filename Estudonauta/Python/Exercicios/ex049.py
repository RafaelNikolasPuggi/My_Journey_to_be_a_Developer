num = int(input('Qual tabuada você quer ver? '))
for i in range (1, 11):
    print('{:2} x {:2} = {}'.format(i,num, i * num))
