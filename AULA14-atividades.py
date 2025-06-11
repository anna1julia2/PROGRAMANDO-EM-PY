# nome = 'anna'

# match nome:
#     case 'julia':
#         print('ola', nome)
#     case 'ana': 
#         print('ola', nome)
#     case _:
#         print('nao foi dessa vez')

#         # nome =  input('nome: ')

# #-------------------------------------------------------

# # match nome:
# #     case 'Carlos':
# #         print('Olá ', nome)
# #     case 'Maria':
# #         print('Olá', nome)
# #     case _:
# #         print('Não foi dessa vez')



# #n = int(input('Teste'))


# match n:
#     case 10:
#         print('O numero é ', n)
#     case 20:
#         print('O numero é ', n)


#     case _:
#         print('O numero desconhecido')

# #----------------------------------------------------------------

# numero =  100


# match numero:
#     case x if x == 100:
#         print('é 100')
#     case x if x > 100:
#         print('x é > 100')
#     case x if x < 100:
#         print('numero é menor que 100')

#----------------------------------------------------------------------
#ATIVIDADE 3 AULA 14

texto = input('texto')
match texto:
    case '':
        print('e vazia')
    case 'aaaa':
        print('nao e vazia')

#-------------------------------------------------------
#atividade 4 aula 14

numero =  10

match numero:
      case x if x == 10:
          print('é 10')
      case x if x > 10:
          print('x é > 11')
      case x if x < 9:
          print('numero é menor que 10')

#--------------------------------------------------------------------

idade = int(input('idade'))

match idade:
    case x if x >= 65 :
        print('idoso')
    case x if x >= 35 and x <= 64:
        print('adulto') 
    case x if x >= 13 and x <= 17:
        print('adolescente')
    case x if x <= 12:
        print('criança')


