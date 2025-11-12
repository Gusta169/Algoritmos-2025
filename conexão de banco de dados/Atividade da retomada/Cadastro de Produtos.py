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
        cadastrar(nome,valor,data)

        sql = """INSERT INTO produtos (nome, valor, data)
                VALUES (%s, %s, %s)
                """
        cursor.execute(sql)
        print("Produto cadastrado")

    if(usuario == 2):
        ID = int(input("Informe o ID do produto: "))
        alterar(ID, nome, valor, data)
        sql = """
            UPDATE produtos 
            SET nome = 'nome';
            SET valor = valor;
            SET data = 'data';
        """
    cursor.execute(sql)
    print("Produto alterado")

        
