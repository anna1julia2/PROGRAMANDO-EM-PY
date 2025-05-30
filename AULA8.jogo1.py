import random

numero_da_sorte = random.randint(1,1000)
meu_numero = int(input('digite seu numero da sorte:'))

if numero_da_sorte == meu_numero:
    print('voce e sortuda, acertou em cheio * . * , o numero e', numero_da_sorte )
else:    
    print('voce erroru feio, nao sabe escolher : o numero e', numero_da_sorte)