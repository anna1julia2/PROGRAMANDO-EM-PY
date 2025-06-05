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

       
       
       
       
       
       
    