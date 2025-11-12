import psycopg2
from funcoes import *

nome = None
valor = None
data = None

con = psycopg2.connect(
    host = "localhost",
    database = "Aula",
    user = "postgres",
    password = "p@ssw0rd",
    port = 5432
)

cursor = con.cursor()
while(True):
    print("""CADASTRO DE PRODUTOS
        1. Cadastrar produto
        2. Alterar produto
        3. Excluir produto
        4. Listar todos os produtos
        5. Sair""")

    usuario = int(input("Escolha: "))
    
    if(usuario == 1):
        nome = None
        valor = None
        data = None
        nome, valor, data = cadastrar(nome,valor,data)

        sql = """INSERT INTO produtos (nome, valor, data)
                VALUES (%s, %s, %s)
            """
        cursor.execute(sql, (nome,valor,data))
        con.commit()
        print("Produto cadastrado")

    elif(usuario == 2):
        ID = int(input("Informe o ID do produto: "))
        novo_nome, novo_valor, nova_data = alterar()
        sql = """
            UPDATE produtos 
            SET nome = %s, valor = %s, data = %s
            WHERE id = %s
        """
        cursor.execute(sql, (novo_nome, novo_valor, nova_data, ID))
        con.commit()
        print("Produto alterado")

    elif(usuario == 3):
        ID = excluir()
        sql = """DELETE from produtos WHERE id = %s"""
        cursor.execute(sql, (ID,))
        con.commit()
        print("Produto excluido")

    elif(usuario == 4):
        sql = """SELECT * FROM produtos"""
        cursor.execute(sql)
        produtos = cursor.fetchall()
        print("Lista de produtos: ")
        for i in produtos:
            print("ID: ", i [0])
            print("Nome: ", i [1])
            print("Valor: ", i [2])
            print("Data: ", i [3])

    elif(usuario == 5):
        print("Saindo...")
        break
    else:
        print("Opção invalida, tente novamente")