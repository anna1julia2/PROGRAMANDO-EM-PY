c = 10
while c > 0:
    print('teste', c)
    c= c - 1
    
escolha = input('escolha s ou n')

while escolha == 'sim':
    prit('tudo bem?')
    escolha = input('escolha s ou n')
    
else:
    print('pq')
    
#-----------------------------------------------------
    
# exemplos while

# com  contador
i = 0
while i <= 10:
    print(i)
    i = i  + 1
    
# com um contador     
n = 10    
while n > 0:
    print(n)
    n  =  n - 1





# string como condição
escolha  =  input('Escolha sim ou não ')
while escolha  ==  'sim':
    n  = input('Digite qualquer coisa ')
    print('Ola como vai')
    escolha  =  input('Escolha sim ou não ')
    
    
else:
    print('Tchau fui')
    
# Loop infinito    
#while True:
#      print('teste')