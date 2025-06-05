def chamar_nome():
    print('nome:' , 'ju')
chamar_nome()

def mostrar_idade():
    print('idade:' , '21')
mostrar_idade()


#---------------------------------

#ação do banco
# saque - desposito - extrato - emprestimo

def banco():
    saldo= 10000.0
    escolha = input('''
     1 - saque
     2 - deposito
     3 - extrato
     4 - emprestimo
     ''')
    if escolha == '1':
        valor_saque_ = float(input('saque >>'))
        saque = saldo - valor_saque
        print('saque - R$', valor_saque)
        print('saldo - R$' , saque)
    if escolha == '2':
        valor_saque_ = float(input('saque >>'))
        saque = saldo - valor_deposito
        print('deposito - R$', valor_deposito)
        print('saldo - R$' , total)
        elif escolha == '3':
            print('saldo R$' , saldo)
            elif escolha == '4':
                print('voce escolheu emprestimo digite o valor')
                saldo = saldo = float(input('valor:'))
                
                else:
                    print('essa opçao nao existe')
                    
