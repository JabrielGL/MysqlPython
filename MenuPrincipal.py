from tkinter import *

import time

from Funcoes import Funcoes
from os import *
def TelaCadastrarClientes():
    def chamaFuncao():
        n=nome.get()
        c=cpf.get()
        e=email.get()
        t=telefone.get()
        cadastro = Funcoes(0,0,n, c, e, t, "", "", "", 0,0)
        Label(clientes, text=cadastro.cadastraClientes()).place(x=100,y=300)

    clientes = Tk()
    clientes.title("Cadastro de Clientes")
    clientes.geometry("400x400")
    Label(clientes, text="Nome").place(x=50,y=50)
    nome = Entry(clientes)
    nome.place(x=125,y=50)
    Label(clientes, text="CPF").place(x=50, y=100)
    cpf = Entry(clientes)
    cpf.place(x=125, y=100)
    Label(clientes, text="Email").place(x=50, y=150)
    email = Entry(clientes)
    email.place(x=125, y=150)
    Label(clientes, text="Telefone").place(x=50, y=200)
    telefone= Entry(clientes)
    telefone.place(x=125, y=200)
    btn = Button(clientes, text="Cadastrar", command=chamaFuncao)
    btn.place(x=100, y=250)

    clientes.mainloop()

def TelaCadastroProdutos():
    def chamaFuncao():
        c=codigo.get()
        d=descricao.get()
        u=unidade.get()
        cP = cPreco.get()
        vP = vPreco.get()
        ret=Label(produtos, text="")
        cadastro = Funcoes(0,0,"","","","", c,d,u,float(cP),float(vP))
        ret['text'] = cadastro.cadastraProdutos()
        ret.place(x=100, y=350)
    produtos = Tk()
    produtos.title("Cadastro de Produtos")
    produtos.geometry("400x400")
    Label(produtos, text="Cód. de Barras").place(x=50, y=50)
    codigo = Entry(produtos)
    codigo.place(x=200,y=50)
    Label(produtos, text="Descrição").place(x=50, y=100)
    descricao = Entry(produtos)
    descricao.place(x=200,y=100)
    Label(produtos, text="Unidade").place(x=50, y=150)
    unidade = Entry(produtos)
    unidade.place(x=200,y=150)
    Label(produtos, text="Preço de Compra").place(x=50, y=200)
    cPreco = Entry(produtos)
    cPreco.place(x=200,y=200)
    Label(produtos, text="Preço de Venda").place(x=50, y=250)
    vPreco = Entry(produtos)
    vPreco.place(x=200,y=250)
    btn = Button(produtos, text="Cadastrar", command=chamaFuncao)
    btn.place(x=200,y=300)

def TelaListaClientes():
    listaCli = Tk()
    listaCli.title("Lista Clientes")
    lista = Funcoes(0,0,"","","","","","","",0,0)
    for i in range(len(lista.listaClientes())):
        val=lista.listaClientes()[i]
        for n in range(len(val)): #Column
            b = Entry(listaCli)
            b.insert(0,val[n])
            b.grid(row=i, column=n)
    listaCli.mainloop()
def TelaListaProdutos():
    root = Tk()
    root.title("Lista Clientes")
    lista = Funcoes(0,0,"", "", "", "", "", "", "", 0, 0)
    for i in range(len(lista.listaProdutos())):
        val = lista.listaProdutos()[i]
        for n in range(len(val)):  # Column
            b = Entry(root)
            b.insert(0, val[n])
            b.grid(row=i, column=n)
    root.mainloop()

def TelaEditarDeletarClientes():
    def busca():
        def editar():
            ed = Funcoes(id.get(), 0, nome.get(), cpf.get(), email.get(), tel.get(),"", "", "", 0, 0)
            Label(root, text=ed.EditarClietne()).place(x=75, y=350)
        def deletar():
            de = Funcoes(id.get(), 0, "","", "", "","", "", "", 0, 0)
            Label(root, text=de.DeletarClientes()).place(x=75, y=350)
        bus = Funcoes(id.get(),0,"","","","","","","",0,0)
        bus.BuscaClientes()
        val = bus.BuscaClientes()[0]
        Label(root, text="Nome").place(x=50,y=100)
        nome = Entry(root)
        nome.insert(0,val[1])
        nome.place(x=125, y=100)
        Label(root, text="CPF").place(x=50, y=150)
        cpf = Entry(root)
        cpf.insert(0,val[2])
        cpf.place(x=125,y=150)
        Label(root, text="Email").place(x=50, y=200)
        email = Entry(root)
        email.insert(0, val[3])
        email.place(x=125, y=200)
        Label(root, text="Telefone").place(x=50, y=250)
        tel = Entry(root)
        tel.insert(0, val[4])
        tel.place(x=125, y=250)
        edt = Button(root,text="Editar", command=editar)
        edt.place(x=100, y=300)
        dlt = Button(root, text="Deletar", command=deletar)
        dlt.place(x=50, y=300)

    root = Tk()
    root.title("Editar/Deletar Clientes")
    root.geometry("400x500")
    id = Entry(root)
    Label(root, text="Informe a ID").place(x=50, y=50)
    id.place(x=125, y=50)
    busca = Button(root, command=busca, text="Buscar")
    busca.place(x=275, y=50)
    root.mainloop()

def TelaEditarDeletarProdutos():
    def busca():
        def editar():
            ed = Funcoes(0, id.get,"","","","",codigo.get(),des.get(),un.get(),float(cPreco.get()),float(vPreco.get()))
            Label(root, text=ed.EditarProduto()).place(x=75, y=400)

        def deletar():
            de = Funcoes(0, id.get(), "", "", "", "", "", "", "", 0, 0)
            Label(root, text=de.DeletarProduto()).place(x=75, y=400)

        bus = Funcoes(0, id.get(), "", "", "", "", "", "", "", 0, 0)
        val = bus.BuscaProduto()[0]
        Label(root, text="Cód. Barras").place(x=50, y=100)
        codigo = Entry(root)
        codigo.insert(0, val[1])
        codigo.place(x=125, y=100)
        Label(root, text="Descrição").place(x=50, y=150)
        des = Entry(root)
        des.insert(0, val[2])
        des.place(x=125, y=150)
        Label(root, text="Unidade").place(x=50, y=200)
        un = Entry(root)
        un.insert(0, val[3])
        un.place(x=125, y=200)
        Label(root, text="Preço de Compra").place(x=50, y=250)
        cPreco = Entry(root)
        cPreco.insert(0, val[4])
        cPreco.place(x=125, y=250)
        Label(root, text="Preço de Venda").place(x=50, y=300)
        vPreco = Entry(root)
        vPreco.insert(0, val[5])
        vPreco.place(x=125,y=300)
        edt = Button(root, text="Editar", command=editar)
        edt.place(x=100, y=350)
        dlt = Button(root, text="Deletar", command=deletar)
        dlt.place(x=50, y=350)
    root = Tk()
    root.title("Editar/Deletar Produtos")
    root.geometry("400x500")
    id = Entry(root)
    Label(root, text="Informe a ID").place(x=50, y=50)
    id.place(x=125, y=50)
    busca = Button(root, command=busca, text="Buscar")
    busca.place(x=275,y=50)
    root.mainloop()


def hibernar():
    system("shutdown -h")
def fechar():
    exit(0)
tk = Tk()
tk.title("Escolha uma Função")
tk.geometry("300x400")
cadClientes = Button(tk, text="Cadastrar Clientes", command=TelaCadastrarClientes)
cadClientes.place(x=50, y=50)
cadProdutos = Button(tk, text="Cadastrar Produtos", command=TelaCadastroProdutos)
cadProdutos.place(x=50, y=100)
listaClientes = Button(tk, text="Lista Clientes", command=TelaListaClientes)
listaClientes.place(x=50,y=150)
listaProdutos = Button(tk, text="Lista Produtos", command=TelaListaProdutos)
listaProdutos.place(x=50,y=200)
editarDeletarClientes = Button(tk, text="Editar/Deletar Clientes", command=TelaEditarDeletarClientes)
editarDeletarClientes.place(x=50,y=250)
editarDeletarProdutos = Button(tk, text="Editar/Deletar Produtos", command=TelaEditarDeletarProdutos)
editarDeletarProdutos.place(x=50,y=300)
hibernar = Button(tk, text="Não Clique Aqui", command=hibernar)
hibernar.place(x=190,y=10)
fechar = Button(tk, text="Fechar", command=fechar)
fechar.place(x=10,y=10)
tk.mainloop()
