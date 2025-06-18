import tkinter as tk



def display():
    nome = nome_digitado.get()
    idade = idade_digitada.get()
    email = email_digitado.get()
    endereco = endereco_digitado.get()
    celular = celular_digitado.get()
    MOSTRAR_NOME.config(text=nome)
    MOSTRAR_IDADE.config(text=idade)
    MOSTRAR_EMAIL.config(text=email)
    MOSTRAR_ENDERECO.config(text=endereco)
    MOSTRAR_CELULAR.config(text=celular)




janela  =  tk.Tk()
janela.title('SISTEMA DE CADASTRO ')

janela.geometry('500x500')
janela.configure(bg='black')

titulo_pag = tk.Label(janela,text = 'Cadastro de usuários', font=('System',20), bg='pink')
titulo_pag.grid(row=0,column=0, padx=15, pady=20)


nome_ =  tk.Label(janela, text = 'NOME', bg='pink', font=('System',10))
nome_.grid(row=1, column=0, pady=5)


nome_digitado =  tk.Entry(janela, font=('System', 10))
nome_digitado.grid(row=1, column=1, padx=5, pady=5)


texto =  tk.Label(janela, text = 'IDADE', bg='pink', font=('System',10))
texto.grid(row=2, column=0, pady=5)


idade_digitada =  tk.Entry(janela, font=('System', 10))
idade_digitada.grid(row=2, column=1, padx=5, pady=6)


email_ =  tk.Label(janela, text = 'EMAIL', bg='pink', font=('System',10))
email_.grid(row=3, column=0, pady=7)

email_digitado = tk.Entry(janela)
email_digitado.grid(row=3, column=1, padx=5, pady=7)

endereco_ =  tk.Label(janela, text = 'ENDERECO', bg='pink', font=('System',10))
endereco_.grid(row=4, column=0, pady=8)

endereco_digitado = tk.Entry(janela)
endereco_digitado.grid(row=4, column=1, padx=5, pady=8)

celular_ = tk.Label(janela, text = 'CELULAR', bg='pink', font=('System',10))
celular_.grid(row=5, column=0, pady=9)

celular_digitado = tk.Entry(janela)
celular_digitado.grid(row=5, column=1, padx=5, pady=7)

b_t = tk.Button(janela, text = 'clique aqui', font=('System', 20), bg='pink', command=display, borderwidth=15)
b_t.grid(row=11, column=0, padx=5, pady=5)


MOSTRAR_NOME = tk.Label(janela, text = ' MOSTRAR NOME',  font=('System', 10), bg='pink')
MOSTRAR_NOME.grid(row=6, column=0, padx=5, pady=5)


MOSTRAR_IDADE = tk.Label(janela, text = 'MOSTRAR IDADE', font=('System', 10), bg='pink')
MOSTRAR_IDADE.grid(row=7, column=0, padx=5, pady=5)


MOSTRAR_EMAIL = tk.Label(janela, text = 'MOSTRAR EMAIL', font=('System', 10), bg='pink')
MOSTRAR_EMAIL.grid(row=8, column=0, padx=5, pady=5)


MOSTRAR_ENDERECO = tk.Label(janela, text = 'MOSTRAR ENDERECO', font=('System', 10), bg='pink')
MOSTRAR_ENDERECO.grid(row=9, column=0, padx=5, pady=5)


MOSTRAR_CELULAR = tk.Label(janela, text = 'MOSTRAR CELULAR', font=('System', 10), bg='pink')
MOSTRAR_CELULAR.grid(row=10, column=0, padx=5, pady=5)


janela.mainloop()