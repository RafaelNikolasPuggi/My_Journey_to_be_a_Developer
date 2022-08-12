Algoritmo "Media salarial de funcionarios"

Var
nome: vetor[1..3] de caractere
salario: vetor[1..3] de real
indicador: inteiro
media: real

Inicio
      para indicador de 1 ate 3 faca
          escreval("Nome do", indicador, "º funcionario(a): ")
          leia(nome[indicador])
      fimpara

      para indicador de 1 ate 3 faca
      escreval("Qual salario do funcionario(a) ", nome[indicador], "?")
      leia(salario[indicador])
      fimpara


      para indicador de 1 ate 3 faca
      escreval("O(a) ", nome[indicador]," tem o salario de: R$ ", salario[indicador])
      media <- media + salario[indicador]
      fimpara
      escreval("A média salarial entre eles é de: R$ ", media/3)
      
Fimalgoritmo