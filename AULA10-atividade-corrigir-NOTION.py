#atividade funções
#1 - CRIE UMA FUNÇÃO PARA COMPARAR 2 NÚMEROS (par ou impar). UTILIZE VARIÁVEIS LOCAIS.

def comparar_par_impar(n1, n2):
    if n1 % 2 == 0 and n2 % 2 ==0:
       print('ambos são pares')
    else:
        print('ou nenhum é ou apenas um  ')

comparar_par_impar(1, 2)

#------------------------------------------------------------------------------
#2 - CRIE UM AFUNÇÃO PARA MULTIPLICAR 3 NUMEROS.

def mult_tres_n(n1, n2, n3):
    print( n1 * n2 * n3)

mult_tres_n(2, 3, 4)




#-------------------------------------------------------------------------------------
#3 - CRIE UMA FUNÇÃO PARA DESCOBRIR O VALOR ELEVADO DE UM NÚMERO.

def elevado():
    n = 10
    n2 = int(input('valor elevado'))
    print(n**n2)


#-----------------------------------------------------------------------------------------
#4 - CRIE UMA FUNÇÃO PARA MOSTRAR UMA MENSAGEM PERSONALIZADA NA TELA, SE O USUÁRIO  DIGITAR, 18 ANOS.

def verificar_idade():
    idade = (int(input('digite sua idade'))
    if idade >= '18':
           print('parabens voce tem 18 anos agora')
            
        else:
            print('hm ainda nao')
idade()            
            


#------------------------------------------------------------------------------------
#5 - DESENVOLVA UMA FUNÇÃO PARA DESCOBRIR A IDADE DE UMA PESSOA.
ano_atual = 2025
ano_nascimento = int(input('ano nascimento'))
mes = input('digite o numero do mes')             
cal = 2025 - ano_nascimento
             
if mes < 6:
   print('ano nascimento', cal)
else:
   print('ano nascimento', cal -1)
mostrar_ano()   
#--------------------------------------------------------------------------------------------
#6 - DESENVOLVA UMA AFUNÇÃO PARA VER SE O BRASIL GANHOU A COPA DE 1999.
def verificar():
    copas = [58, 62, 70, 94, 02]
    if ano in copas:
       print('ganhou')
    else
       print('nao ganhou')
       
       
       
       
#--------------------------------------------------------------------------------------------       
#7 - DESENVOLVA UM SISTEMA DE RESTAURANTE, ONDE O CLIENTE TEM OPÇÃO DE ESCOLHER ENTRE SALADA, MACARRONADA, SANDUICHE, SORVETE.         
       
lista = ['salada, macarronada, sanduiche ou sorvete?:']
      print ('lista'))
      escolha = int(input9'digite

                    NOTION- RESOLUÇÃO 1- CORRIRGIR

                    # 1
def comparar():
    n1 =  int(input('Digite um número> '))
    n2 =  int(input('Digite um número> '))

    if n1 % 2 == 0 and n2 % 2 == 0:
        print('Ambos sã pares')
    elif n1 % 2 == 0 or n2 % 2 == 0:
        print('Um deles é par')
    else:
        print('Ambos impares')
# 2
def mult():
    print(3*4*5)
    
    
#3
def elevado():
  n  = 10
  n2 = int(input('valor elevado'))
  print(n**n2)
  
# 4
def verificar_idade():
    idade =  int(input('idade: '))
    if idade == 18:
        print('18  anos')
    else:
        print('Não tem 18')


# verificar_idade()



# 5
def mostrar_ano():
    ano_atual = 2025
    ano_nascimento = int(input('Ano nascimento:'))
    mes =  int(input('digite o numero do mês 1'))
    cal  =  2025 - ano_nascimento

    if mes <=6:
        print('Ano nascimento', cal)
    else:

         print('Ano nascimento', cal - 1)

#mostrar_ano()

def verificar():
    copas = [1958,1962,1970,1994,2002]

    ano =  int(input('Digite o ano que vc acha que o br granhou'))
    if ano in copas:
        print('ganhou!')
    else:
        print('Não ganhou!')

#verificar()

def restaurante():
    lista =  ['Macarronada', 'Salada', 'Sanbuiche', 'Sorvete']
    print(lista)
    escolha  =  int(input('Digite o id do produto: '))
    print('Escolha: ',  lista[escolha])

while True:
      restaurante()

       
       
       
       
       
       
    
