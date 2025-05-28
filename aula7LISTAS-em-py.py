#vazia
lista = []
#lista preenchida
#- de tras pra frente - ao contrario
lista_teste = [1,2,3,4,5,6,7,8,9]
#              0 1 2 3 4 5 6 7 8  indices
print(lista_teste[-3])> 7

lista_teste[5] = 100
print(lista_teste)

#------------------------

#funções das listas
lista = []
#alteram a estrutura da lista
#append() extend() +=()

lista.append(10)
print(lista)

#varios dados no final da lista -> extend() +=()
lista.extend([10,20,30,40,50,100]) add texto tambem no final 'teste'
print(lista)
lista += ('a','b')
print(lista)

#add dado em um indice especifico
lista.insert(0,200)

#deletar dado del remove()

lista.pop() #deleta o indice que voce declarou

print(lista)

lista.remove('a') #remove o valor que vc ve

del lista[0] #deleta o indice
lista.insert(0,200)
print(lista)

print(lend(lista))