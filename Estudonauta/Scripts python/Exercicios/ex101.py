def voto():
    from datetime import datetime
    idade = datetime.today().year - nasc
    if idade < 16:
        return f'Com {idade} anos, seu voto é NEGADO!'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos, seu voto é OPCIONAL'
    else:
        return f'Com {idade} anos, seu voto é OBRIGATORIO'


nasc = int(input('Qual seu ano de nascimento? '))
print(voto())
