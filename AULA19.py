#create = criar
#read = ler 
#update =  atualizar
#dalete = detelar 
#CRUD

#tkinter = interface grafica
#sqlite3 = banco de dados
#ttl = submodulo tkinter
#messagebox = biblioteca que cria uma caixa de dialogo
#python puro

import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def conecter():
    return sqlite3.connect('teste.db')

def criar_tabela():
    conn = conectar()
    c = conn.cursor()
    c.execute('''
        CREAT TABLE IF NOT EXISTS usuarios()
        id  INTERGER NOT NULL,
        nome TEXT NOT NULL, 
        email TEXT NOT NULL,     
''')
    conn.commit() 
    conn.close()

#CREAT

def inserir_usuario():
    nome = entry_nome.get()
    email = entry_email.get()
    cpf = entry_cpf.get()
    if nome and email:
        conn.conectar()
        c = conn.cursor()
        c.execute('INSERT INTO usuarios(id, nome, email) VALUES(?,?,?)',(cpf, nome, email))
        conn.commit()
        conn.close()
        messagebox.showinfo('AVISO', 'DADOS INSERIDOS')
        mostrar_usuario() 
    else:
        messagebox.showerror('ERRO', 'ALGO DEU ERRRADO')  

#READ LER
 
def mostrar_usuario():
    for row in tree.get_children():
        tree.detele(row)
    conn = conectar()
    c = conn.cursor()
    c.execute('SELECT * FROM usuarios')
    usuarios = c.fetchall()
    for user in usuarios:
            tree.insert("", "end", values=(user[0], user[1], user[2]))
    conn.close()

#DELETE DELETAR
            
def detele_usuario():
    dados_del = tree.selection()
    if dados_del:
        user_id = tree.item(dados_del)['values'][0]
        conn = conectar()
        c = conn.cursor()
        c.execute('DELETE FROM usuarios WHERE id= ? ',(user_id,))
        conn.commit()
        conn.close()
        messagebox.showinfo('', 'DADO DELETADO')
        mostrar_usuario()
    else:
        messagebox.showerror('ERRO','OCORREU UM ERRO')

#UPDATE ATUALIZAR
         
def editar():
 selecao = tree.selection()
 if selecao:
    user_id = tree.item(selecao)['values'][0]
    novo_nome = entry_nome.get()
    novo_email = entry_email.get()
    if nome_nome and novo_email:
         conn = conectar()
         c = conn.cursor()
         c.execute('UPDATE usuarios SET nome = ? , email = ? WHERE id = ?',(novo_nome, novo_email, user_id))
         conn.commit()
         conn.close()
         messagebox.showinfo('EDICAO', 'DADOS EDITADOS')
         mostrar_usuario()
    else:
        messagebox.showerror('ERRO', 'NAO HOUVE ALTERACAO')
 else:
    messagebox.showwarning('', 'PREENCHA TUDO')


janela = tk.Tk()
janela.configure(bg='magenta')
janela.title('CRUD')
janela.geometry('600x600')

TITULO = tk.Label(janela, text = 'SISTEMA DE CADASTRO',fg = 'black', font=('lexend',20, 'bold'))
TITULO.grid(padx=10, pady=10)

label_cpf = tk.Label(janela, text='CPF:', font=('lexend',14))
label_cpf.grid(row=1,column=0, padx=10, pady=10)

entry_cpf = tk.Entry(janela, font=('arial',15))
entry_cpf.grid(row=1,column=1,padx=10, pady=10)

label_nome = tk.Label(janela, text='NOME:', font=('lexend',14))
label_nome.grid(row=2,column=0, padx=10, pady=10)

entry_nome = tk.Entry(janela, font=('arial',15))
entry_nome.grid(row=2,column=1,padx=10, pady=10)

label_email = tk.Label(janela, text='EMAIL:', font=('lexend',14))
label_email.grid(row=3,column=0, padx=10, pady=10)

entry_email = tk.Entry(janela, font=('arial',15))
entry_email.grid(row=3,column=1,padx=10, pady=10)

btn_salvar = tk.Button(janela, text = "salvar", font= ('lexend', 15))
btn_salvar.grid(row=4,column=1, padx=10, pady=10)

btn_editar = tk.Button(janela, text= 'editar', font= ('lexend', 15))
btn_editar.grid(row=5,column=2, padx=11, pady=11)

btn_deletar = tk.Button(janela, text= 'deletar', font= ('lexend', 15))
btn_deletar.grid(row=6, column=3, padx=12, pady=12)

columns = ('ID', 'NOME', 'EMAIL')
tree = ttk.Treeview(janela, columns=columns, show='headings')
tree.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

for col in columns:
    tree.heading(col, text=col)

criar_tabela()
mostrar_usuario()    

janela.mainloop()

    





