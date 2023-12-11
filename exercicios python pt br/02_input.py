"""""""""
Vamos entender a função do Input

1. Esta linha de código é responsável por obter uma entrada do usuário e armazená-la na variável x.
2. input(): Esta função é usada para ler uma linha de entrada do teclado como uma string. O texto "Informe um numero: " é exibido na tela como uma solicitação para o usuário digitar algo.
3. int(): Esta função converte a string fornecida pelo usuário em um número inteiro. Isso é necessário porque o que é retornado pela função input() é sempre uma string, e aqui, estamos esperando que o usuário insira um número.
4. print(): Esta função é usada para enviar saída para a tela. Neste caso, ela exibe o valor da variável x, que é o número inteiro fornecido pelo usuário.

int, float, e str são tipos de dados básicos em Python, cada um com um propósito e características específicas:

int: A abreviação de "integer", que significa número inteiro(1).
float: A abreviação de "floating point number", que significa número de ponto flutuante(1.0).
str: A abreviação de "string"('1').

***** print(type(x)) *****
type imprime o tipo de dado do codigo.

Poderiamos fazer este codigo das seguintes maneiras:
"""""""""
x = int(input("Informe um numero: "))
print(type(x))

x = str(input("Informe um numero: "))
print(type(x))

x = float(input("Informe um numero: "))
print(x)
print(type(x))