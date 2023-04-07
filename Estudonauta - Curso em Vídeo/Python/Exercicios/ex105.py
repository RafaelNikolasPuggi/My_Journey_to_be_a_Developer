def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de varios alunoas.
    :param n: Recebe uma ou mais notas a serem avaliadas.
    :param sit: Valor opcional. Define a Situação das notas.
    :return: Retorna o dicionario contendo as informações.
    """
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Media'] = sum(n)/len(n)
    if sit:
        if r['Media'] >= 7:
            r['Situação'] = 'BOA'
        elif r['Media'] >= 5:
            r['Situação'] = 'RAZOAVEL'
        else:
            r['Situação'] = 'RUIM'
    return r


# Programa principal
resp = notas(2, 5.3, 6, 9, sit=True)
print(resp)