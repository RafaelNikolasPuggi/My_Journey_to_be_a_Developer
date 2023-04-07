from UtilidadesCEV.Moeda import resumo
from UtilidadesCEV.Dados import leiaDinheiro

p = leiaDinheiro('Digite o preço: R$')
t = float(input('Digite a taxa: %'))
resumo(p, t)
