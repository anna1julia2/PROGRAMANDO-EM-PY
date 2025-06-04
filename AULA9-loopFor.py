#loop for = para

# range

for variavel in range (11):
    print(variavel)

for variavel in range (0,11,2):
    print(variavel)
    
# lista

lista_letras =  ['A','B','C']

for n in lista_letras:
    print(n)
    
for i in list(range(1,11)):
    print(i)
    
#-----------------------------------------------------
    
import random

chances = {3,2,1}

for i in chances:
    numero_aleatorio = random.randint(1,11)
    
    print('voce tem apenas..' , i , 'chances')
    chute = int(input('digite seu chute: '))
    
    if numero_aleatorio == chute:
        print('acertou em cheio')
        break
    else:
        print('errou feio')
else:
    print('chances esgotadas')