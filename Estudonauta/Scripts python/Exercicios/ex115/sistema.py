from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)


while True:
    res = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if res == 1:
        lerArquivo(arq)
        sleep(2)
    elif res == 2:
        cabeçalho('Novo cadastro')
        nome = str(input('Nome: '))
        idade = LeiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif res == 3:
        cabeçalho('Saindo do sistema...')
        sleep(2)
        break
    else:
        print(vermelho('ERRO! DIGITE UMA OPÇÃO VÁLIDA!'))
        sleep(2)
