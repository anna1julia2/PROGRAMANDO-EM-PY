# 1* 
# Peça para o usuário digitar um número, verifique se um número é positivo, 
# negativo ou zero.

# 2*

# Peça para o usuário digitar a idade, verifique se uma pessoa pode votar com 
# base na idade.

# 3*

# Declara uma variável com um número qualquer, determine se um número é par ou ímpar.

# 4*

# Usuário vai digitar 3  números, para criar um triângulo, verifique se um triângulo 
# é equilátero, isósceles ou escaleno

# Um triângulo é chamado de equilátero se todos os lados possuem a mesma medida. 
# Um triângulo é chamado de isósceles se dois lados possuem a mesma medida. 
# Um triângulo é chamado de escaleno se todos os lados possuem medidas diferentes.

# 5*

# Determine se um número é múltiplo de 5 e 7.

# 6*

# Verifique se um número é positivo e maior que 10

# 7*

# Verifique se um número é divisível por 3 ou 5.

#------------------------------------------------------------------------------------------

#1
n = int(input('numero: '))

if n > 0:
    print('POsitivo')
elif n < 0:
    print('negativo')
else:
    print('Zero')


# 2
idade  = 18

if idade >= 16:
    print('Pode votar')
else:
    print('Não pode votar')
    
# 3     

var  =  10

if var % 2 == 0:
    print('par')
else:
    print('Impar')
    
# 4

l1 = 1
l2 = 2
l3 = 3

if l1 == l2 == l3 == l1:
    print('Equilatero')
elif l1 != l2 != l3 != l1:
    print('Escaleno')
else: 
    print('isocesles')  
#5

multiplo  = int(input('nº>  '))

if multiplo % 5 == 0 and multiplo % 7 == 0:
    print('São multiplos')
elif multiplo % 5 == 0 or multiplo % 7 == 0:
    print('Apenas 1 é multiplo')
else:
    print('nenhum é...')

#6
    
n =  15

if n > 10:
    print('O número é positivo e maior que 10')
    
else:
    print('Não é nada')


#7
    
n1   =  15

if n1 % 3 == 0 and n1 % 5==0:
    print('São divisiveis')
else:
    print('Não são!')