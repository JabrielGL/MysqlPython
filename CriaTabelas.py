import pymysql

con = pymysql.connect("localhost", "root", "", "quartoanoinfo")

cur = con.cursor()

sql= "CREATE TABLE produtos (idProdutos INT AUTO_INCREMENT PRIMARY KEY, codBar INT, descricao CHAR(225), unidade CHAR(3), cPreco FLOAT, vPreco FLOAT)"
cur.execute(sql)

sql= "CREATE TABLE clientes (idClientes INT AUTO_INCREMENT PRIMARY KEY, nome CHAR(20), cpf CHAR(11), email CHAR(225), telefone CHAR(11))"

cur.execute(sql)

con.commit()
con.close()