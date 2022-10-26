import sqlite3
import datetime
conexao = sqlite3.connect('banco.sqlite3')
cursor = conexao.cursor()
#cursor.execute('CREATE TABLE pedido (cliente_id INT NOT NULL,data varchar(100));')
#cursor.execute('CREATE TABLE item_pedido (pedido_id INT NOT NULL, produto varchar(100), valor varchar(100), quantidade varchar(100));')
print("Insira os dados do Pedido")
cliente_id = input("Qual o ID do cliente? ")
hoje = datetime.date.today()
valores = [cliente_id, hoje]
sql_pedido = 'insert into pedido (cliente_id, data) values (?, ?)'
cursor = conexao.cursor()
cursor.execute(sql_pedido, valores)
print( 'ID do pedido:', cursor.lastrowid)

pedido_id = cursor.lastrowid
quantidade_itens = input("Quantos itens deseja adicionar? ")
quantidade_itens = int(quantidade_itens)
for i in range(quantidade_itens):
    produto = input("Qual o produto? ")
    quantidade = input("Qual a quantidade? ")
    quantidade = int(quantidade)
    valor = input("Qual o valor? ")
    valor = float(valor)
    sql_item = '''
    insert into item_pedido
    (pedido_id, produto, valor, quantidade)
    values (?, ?, ?, ?)
    '''
    valores = [pedido_id, produto, valor, quantidade]
    
    cursor.execute(sql_item, valores)
    
    conexao.commit()
    conexao.close()