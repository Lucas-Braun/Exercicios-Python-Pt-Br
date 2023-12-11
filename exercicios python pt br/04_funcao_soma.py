"""""""""

######################## Criando soma  com Função ####################################################################################################################

1. Define uma função chamada soma que aceita dois argumentos, numero_x e numero_y, e retorna a soma desses dois números.

2. Solicita ao usuário que insira um número para numero_x usando a função input e converte o valor inserido em um número inteiro usando int(input(...)).

3. Solicita ao usuário que insira um número para numero_y da mesma maneira.

4. Chama a função soma(numero_x, numero_y) com os valores fornecidos pelo usuário para calcular a soma e armazena o resultado em uma variável chamada resultado.

5. Imprime o resultado da soma usando uma f-string, mostrando a expressão completa da soma, como "A soma dos números {numero_x} + {numero_y} é igual a {resultado}".

######################################################################################################################################################################

"""""""""

def soma(numero_x,numero_y):
    return numero_x + numero_y

numero_x = int(input('Insira o numero X: '))
## Inserir numero 5 ##
numero_y = int(input('Insira o numero Y: '))

resultado = soma(numero_x, numero_y)
 
print(f" A soma dos numeros {numero_x} + {numero_y} é iqual a {resultado} ")
