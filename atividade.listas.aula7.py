#e-comerce com listas

produtos = ['','iphone 17', 'notebook dell', 'fone', 'ssd']
valores = ['',7000.0,10000.0,400.0,350.55]
print()
print( 'escolha o produto atraves do id 1 - 2 - 3 - 4')
print('produtos da loja x')
print(produtos[1], '-R$', valores[1])
print(produtos[2], '-R$', valores[2])
print(produtos[3], '-R$', valores[3])
print(produtos[4], '-R$', valores[4])
print()
pedido1 = int(input('digite o id do pruduto'))
pedido2 = int(input('digite o id do produto'))
pedido3 = int(input('digite o id do pruduto'))


carrinho = []
meu_total = []

carrinho.append(produtos[pedido1])
carrinho.append(produtos[pedido2])
carrinho.append(produtos[pedido3])

meu_total.append(valores[pedido1])
meu_total.append(valores[pedido2])
meu_total.append(valores[pedido3])

print('produtos no carrinho -', carrinho)
total = sum(meu_total)
print('R$', total)

print('escolha a forma de pagamento 1 pix   2 CC   3 paypall')
formas = ['','pix', 'CC', 'paypall']
escolha = int(input('digite o id: '))
print('a sua forma de pagamento é ',formas[escolha])
print('------x------')
print('obrigada volte sempre')