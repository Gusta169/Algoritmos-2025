import psycopg2

nome = input("Informe o nome do produto: ")
preco = float(input("Informe o preço do produto: "))
data = input("Informe a data de validade: ")

con = psycopg2.connect(
    host = "localhost",
    database = "Aula",
    user = "postgres",
    password = "p@ssw0rd",
    port = 5432
)
print("Conectado no banco de dados")

# Passo 2: obter o manipulador do BD

cursor = con.cursor()

#Passo 3: Definir comandoI SQL e dados

# sql = """
#     INSERT INTO produtos (nome, valor, data)
#     VALUES (%s, %s, %s)
#     """

sql = """
    SELECT * FROM produtos
"""

valores = (nome , preco, data)

# Passo 4: Executar o comando SQL

# cursor.execute(sql, valores)
# con.commit()
cursor.execute(sql)

resultado = cursor.fetchall() #pega todo o registro no BD e coloca na variavel

for linha in resultado:
    print("ID: ", linha [0])
    print("nome: ", linha [1])
    print("preço: ", linha[2])
    print("Data de validade: ", linha[3])

if (cursor.rowcount > 0):
    print("Registro inserido com sucesso")
else:
    print("Um erro ocorreu")