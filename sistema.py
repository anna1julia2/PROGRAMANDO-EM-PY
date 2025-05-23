#SISTEMA DE MEDIAS DE NOTAS

print('SEJA BEM VINDA JUJU')
nome = input ('digite o nome: ')
idade_anterior = float(input(' digite a idade anterior: '))
idade_atual = float(input('digite a idade atual: '))
idade_seguinte = float(input('digite a idade seguinte: '))

media = (idade_anterior + idade_atual + idade_seguinte) / 3
print ('a pessoa' , nome, 'esta com a idade', media )

anterior = media <20
seguinte = media >22
media = media >22 and media <20

print(f'''
a juju {nome}
idade anterior {20}
idade atual {21}
idade seguinte {22}
''')
