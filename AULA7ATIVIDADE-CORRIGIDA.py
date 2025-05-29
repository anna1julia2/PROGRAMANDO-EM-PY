# # Exercício 1: Crie uma lista chamada pessoas que contenha 
# # os números inteiros de pessoa1 a pessoa5 e imprima-a na tela.

# for numeros in range(1,6):
#     print('pessoa'+str(numeros))


# # Exercício 2: Acesse e imprima o terceiro elemento 
# # da lista `numeros`.


# numeros = [1,2,3,4,5,6]
# print(numeros[2])



# # Exercício 3: Adicione o número 9 à lista `numeros` e imprima a
# #  lista atualizada.

# # Exercício 4: Remova o número 5 da lista `numeros` 
# # e imprima a 
# # lista resultante.

# # del numeros[4]
# # numeros.remove(5)
# print(numeros)



# # Exercício 5: Crie uma lista chamada carros 
# # contendo três nomes 
# # de carros diferentes. Em seguida, concatene 
# # essa lista com a lista `numeros` e imprima o resultado.



# concatene =  carros + numeros
# print(concatene)


lista  =  [1,2,3]
carros  =  ['ferrari', 'hb20', 'fusca']
x =  lista + carros

 
   



# # Exercício 6: Use um loop `for` para percorrer e 
# # imprimir todos 
# # os elementos da lista  = [12,45,45,89,78,3,6,78,87]

# lista  =  [12,45,45,89,78,3,6,78,87]
# for n_lista in lista: 
#     print(n_lista)



# # Exercício 7: Verifique se o número 5 está 
# # presente na lista 
# # `numeros` e imprima uma mensagem informando 
# # se ele está na 
# # lista ou não.

if 5 in numeros: 
   print('existe')
else: 
   print('Não existe')     

variavel  = 5
for n in range(5,6):
    # x  =  int(input('Digite'))
    if variavel in numeros:
       print('certo')
    else: 
       print('Não esta')     
         

# 1

lista  =  list(range(2,21,2))
print(lista)

# 2

numeros = [1,2,3,4,5,6,7,8,9,10]
numeros =  list(range(1,11))


# 3

numeros.append(9)


# 4

numeros.remove(5)



# 5


carros  =  ['tesla', 'ferrari','Jeep']
print(carros,numeros)

carros +=(numeros)

print(carros)
