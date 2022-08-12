def escreva(nome):
    tam = len(nome) + 4
    print('=' * tam)
    print(f'  {nome}')
    print('=' * tam)


n = str(input('Nome: ')).strip()
escreva(n)