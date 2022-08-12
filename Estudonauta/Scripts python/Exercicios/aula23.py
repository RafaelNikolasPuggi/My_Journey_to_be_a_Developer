try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados.')
except ZeroDivisionError:
    print('Não é possível dividir por zero.')
else:
    print(f'O resultado é {r:.2f}')
finally:
    print('Volte sempre! Muito obrigado!')