"""""""""
Criando operacao de soma
   
1. Criamos a variavel numero_x e numero_y como dados interiros.
2. Criamos a variavel  soma que ira soma os valores das variaveis numero_x e numero_y
3. Com os valores do usuario, criamos a operação soma com numero_x + numero_y
4. Imprime na tela os valores.
5. 'f' antes das aspas indica que é uma f-string. O 'f' permite incorporar expressões entre chaves {} diretamente dentro da string,
   que serão avaliadas e formatadas automaticamente.
6. Imprime:  A soma dos numeros 5 + 5 é iqual a 10 

"""""""""
## Inserir numero 5 ##
numero_x = int(input('Insira o numero X: '))
## Inserir numero 5 ##
numero_y = int(input('Insira o numero Y: '))
## Resultado = 10 ##
soma = numero_x + numero_y

print(f" A soma dos numeros {numero_x} + {numero_y} é iqual a {soma} ")