from tkinter import *
from Funcoes import Funcoes
from os import *
def TelaCadastrarClientes():
    def chamaFuncao():
        n=nome.get()
        c=cpf.get()
        e=email.get()
        t=telefone.get()
        cadastro = Funcoes(n, c, e, t, "", "", "", 0,0)
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
        cadastro = Funcoes("","","","", c,d,u,float(cP),float(vP))
        Label(produtos, text=cadastro.cadastraProdutos()).place(x=100, y=300)
    produtos = Tk()
    produtos.title("Cadastro de Produtos")
    produtos.geometry("400x400")
    Label(produtos, text="Cód. de Barras").place(x=50, y=50)
    codigo = Entry(produtos)
    codigo.place(x=150,y=50)
    Label(produtos, text="Descrição").place(x=50, y=100)
    descricao = Entry(produtos)
    descricao.place(x=150,y=100)
    Label(produtos, text="Unidade").place(x=50, y=150)
    unidade = Entry(produtos)
    unidade.place(x=150,y=150)
    Label(produtos, text="Preço de Compra").place(x=50, y=200)
    cPreco = Entry(produtos)
    cPreco.place(x=150,y=200)
    Label(produtos, text="Preço de Venda").place(x=50, y=250)
    vPreco = Entry(produtos)
    vPreco.place(x=150,y=250)
    btn = Button(produtos, text="Cadastrar", command=chamaFuncao)
    btn.place(x=200,y=300)

def TelaListaClientes():
    listaCli = Tk()
    listaCli.title("Lista Clientes")
    lista = Funcoes("","","","","","","",0,0)
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
    lista = Funcoes("", "", "", "", "", "", "", 0, 0)
    for i in range(len(lista.listaProdutos())):
        val = lista.listaProdutos()[i]
        for n in range(len(val)):  # Column
            b = Entry(root)
            b.insert(0, val[n])
            b.grid(row=i, column=n)
    root.mainloop()
def hibernar():
    system("shutdown -h")
def fechar():
    exit(0)
tk = Tk()
tk.title("Escolha uma Função")
tk.geometry("300x300")
cadClientes = Button(tk, text="Cadastrar Clientes", command=TelaCadastrarClientes)
cadClientes.place(x=50, y=50)
cadProdutos = Button(tk, text="Cadastrar Produtos", command=TelaCadastroProdutos)
cadProdutos.place(x=50, y=100)
listaClientes = Button(tk, text="Lista Clientes", command=TelaListaClientes)
listaClientes.place(x=50,y=150)
listaProdutos = Button(tk, text="Lista Produtos", command=TelaListaProdutos)
listaProdutos.place(x=50,y=200)
hibernar = Button(tk, text="Não Clique Aqui", command=hibernar)
hibernar.place(x=190,y=10)
fechar = Button(tk, text="Fechar", command=fechar)
fechar.place(x=10,y=10)
tk.mainloop()
