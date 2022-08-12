Algoritmo "Definição de pedido."

Var
v1, v2: inteiro
nome: caractere
Inicio

escreval ("Qual seu nome?")
leia (nome)
escreval ("Bem-Vindo ", nome, " qual é o seu pedido!")


repita
        escreval ("Menu de Opções")
        escreval ("1... Picole")
        escreval ("2... Sorvete")
        escreval ("3... Milkshake")
        escreval ("Escolha uma opção!")
        leia (v1)
   ate  ((v1 >=1) e (v1 <=3))

escolha (v1)
   caso 1
        repita
        escreval("Qual sabor do picole?")
        escreval("1... uva")
        escreval("2... chocolate")
        escreval("3... leite condensado")
        leia (v2)
        ate  ((v2 >=1) e (v2 <=3))

   caso 2
        repita
        escreval("Qual sabor do sorvete?")
        escreval("1... chocolate")
        escreval("2... flocos")
        escreval("3... morango")
        leia (v2)
        ate  ((v2 >=1) e (v2 <=3))

   caso 3
        repita
        escreval("Qual sabor do milkshake?")
        escreval("1... chocolate com baunilha")
        escreval("2... morango com chocolate")
        escreval("3... napolitano")
        leia (v2)
        ate  ((v2 >=1) e (v2 <=3))

fimescolha

escreval ("Obrigado ", nome," e volte sempre!")


Fimalgoritmo