import pymysql
from pprint import pprint
class Funcoes():
    def __init__(self, idCliente, idProduto, nome, cpf, email, telefone, codigo, descricao, unidade, cPreco, vPreco):
        self.idCliente = idCliente
        self.idProduto = idProduto
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

    def BuscaClientes(self):
        sql = "select * from clientes where idClientes = %s"
        val = self.idCliente
        returno = []
        try:
            con = pymysql.connect("localhost", "root", "", "quartoanoinfo")
            cur = con.cursor()
            cur.execute(sql,val)
            for i in cur.fetchall():
                returno.append(i)
        except:
            con.rollback()
            returno.append("falha")
        con.close()
        return returno

    def EditarClietne(self):
        sql = "UPDATE clientes SET nome = %s, cpf = %s, email = %s, telefone = %s WHERE idClientes = %s"
        val = (self.nome, self.cpf, self.email, self.telefone, self.idCliente)
        try:
            con = pymysql.connect("localhost", "root", "", "quartoanoinfo")
            cur = con.cursor()
            cur.execute(sql,val)
            con.commit()
            returno = "sucesso"
        except:
            con.rollback()
            returno ="falha"
        con.close()
        return returno
    def DeletarClientes(self):
        sql = "DELETE FROM clientes WHERE idClientes=%s"
        val = self.idCliente
        try:
            con = pymysql.connect("localhost", "root", "", "quartoanoinfo")
            cur = con.cursor()
            cur.execute(sql,val)
            con.commit()
            returno = "sucesso"
        except:
            con.rollback()
            returno ="falha"
        con.close()
        return returno

    def BuscaProduto(self):
        sql = "select * from produtos where idProdutos = %s"
        val = self.idProduto
        returno = []
        try:
            con = pymysql.connect("localhost", "root", "", "quartoanoinfo")
            cur = con.cursor()
            cur.execute(sql,val)
            for i in cur.fetchall():
                returno.append(i)
        except:
            con.rollback()
            returno.append("falha")
        con.close()
        return returno

    def EditarProduto(self):
        sql = "UPDATE produtos SET codBar = %s, descricao = %s, unidade = %s, cPreco = %s vPreco = %s WHERE idProdutos = %s"
        val = (self.codigo, self.descricao, self.unidade, self.cPreco, self.vPreco, self.idProduto)
        try:
            con = pymysql.connect("localhost", "root", "", "quartoanoinfo")
            cur = con.cursor()
            cur.execute(sql,val)
            con.commit()
            returno = "sucesso"
        except:
            con.rollback()
            returno ="falha"
        con.close()
        return returno

    def DeletarProduto(self):
        sql = "DELETE FROM produtos WHERE idProdutos=%s"
        val = self.idProduto
        try:
            con = pymysql.connect("localhost", "root", "", "quartoanoinfo")
            cur = con.cursor()
            cur.execute(sql,val)
            con.commit()
            returno = "sucesso"
        except:
            con.rollback()
            returno ="falha"
        con.close()
        return returno