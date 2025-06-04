dicionario = {'nome': 'Clara', 'idade': 25, 'cidade':'Guarulhos'}

for key,value in dicionario.items():
    print(key, value)
    
    
dicionario = {'nome': 'Clara', 'idade': 25, 'cidade':'Guarulhos'}

for value in dicionario.values():
    print(value)
    
    
dicionario = {'nome': 'Clara', 'idade': 25, 'cidade':'Guarulhos'}

for key in dicionario.keys():
    print(key)
    
    
lista_keys = []
lista_valores = []
dicionario = {'nome': 'Clara', 'idade': 25, 'cidade':'Guarulhos'}
for k,v in dicionario.items():
    lista_keys.append(k)
    lista_valores.append(v)
print(lista_keys)
print(lista_valores)

#--------------------------------------------------------------------

#tabuada

#for i in range(0,11):
    
n = int(input('digite o multiplicador da tabuada:'))
for i in range(0,11):    
    
    calculo = i * n
    print(n, 'x', i ,'=', calculo)