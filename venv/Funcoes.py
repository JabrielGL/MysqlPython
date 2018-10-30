import pymysql
from pprint import pprint
class Funcoes():
    def __init__(self, nome, cpf, email, telefone, codigo, descricao, unidade, cPreco, vPreco):
        self.nome= nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
        self.codigo = codigo
        self.descricao = descricao
        self.unidade = unidade
        self.cPreco = cPreco
        self.vPreco = vPreco
    def cadastraClientes(self):
        sql = "INSERT INTO clientes (nome,cpf,email,telefone) VALUES (%s,%s,%s,%s)"
        val = (self.nome, self.cpf,self.email,self.telefone)
        try:
            con = pymysql.connect("localhost", "root", "", "quartoanoinfo")
            cur = con.cursor()
            cur.execute(sql, val)
            con.commit()
            returno = "Sucesso"
        except:
            con.rollback()
            returno = "Falha"
        con.close()
        return returno
    def cadastraProdutos(self):
        sql = "INSERT INTO produtos (codBar,descricao,unidade,cPreco,vPreco) VALUES (%s,%s,%s,%s,%s)"
        val = (self.codigo, self.descricao,self.unidade,self.cPreco,self.vPreco)
        try:
            con = pymysql.connect("localhost", "root", "", "quartoanoinfo")
            cur = con.cursor()
            cur.execute(sql, val)
            con.commit()
            returno = "Sucesso"
        except:
            con.rollback()
            returno = "Falha"
        con.close()
        return returno

    def listaClientes(self):
        sql = "select * from clientes"
        try:
            con = pymysql.connect("localhost", "root", "", "quartoanoinfo")
            cur = con.cursor()
            cur.execute(sql)
            returno = []
            for i in cur.fetchall():
                returno.append(i)
        except:
            con.rollback()
            returno = "falha"
        con.close()
        return returno

    def listaProdutos(self):
        sql = "select * from produtos"
        try:
            con = pymysql.connect("localhost", "root", "", "quartoanoinfo")
            cur = con.cursor()
            cur.execute(sql)
            returno = []
            for i in cur.fetchall():
                returno.append(i)
        except:
            con.rollback()
            returno = "falha"
        con.close()
        return returno
