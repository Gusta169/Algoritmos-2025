import psycopg2

# abrir uma conexão
con = psycopg2.connect(
    host="localhost",          # Endereço do servidor do banco de dados (geralmente 'localhost' se for local)
    database="algoritmos",     # Nome do banco de dados
    user="postgres",           # Usuário do PostgreSQL
    password="p@ssw0rd",        # Senha de acesso do usuário
    port ='5432'
)

cursor = con.cursor()  # abrir o manipulador do BD (cursor é quem envia comandos SQL ao banco)

# comando SQL para inserir dados

sql = "INSERT INTO alunos (nome, idade) VALUES (%s, %s)"  
valores = ("Maria", 20)  # valores a serem inseridos nos campos da tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    idade INT
);
""")

cursor.execute(sql, valores)  # executa o comando SQL substituindo os %s pelos valores
con.commit()  # confirma a gravação dos dados no banco (sem isso nada é salvo)

# Confirmação se aumentou uma linha no BD
if cursor.rowcount > 0:
    print("Registro inserido")  # imprime mensagem de sucesso
else:
    print("Nada foi salvo")  # imprime caso não tenha ocorrido inserção

sql_select = "SELECT * FROM alunos"
cursor.execute(sql_select)
registros = cursor.fetchall()
cursor.close()  # fechar o manipulador (cursor)
con.close()     # fechar a conexão com o banco de dados

"""
Comandos SQL básicos:
--------------------

INSERT INTO tabela (campo1, campo2, ...)
VALUES (valor1, valor2, ...);
    → Insere um novo registro na tabela.

UPDATE tabela SET
    campo1 = valor1,
    campo2 = valor2,
    ...
WHERE id = valor;
    → Atualiza os dados de um registro existente.

DELETE FROM tabela
WHERE id = valor;
    → Remove um registro da tabela.

SELECT * FROM tabela;
    → Consulta (lê) todos os dados da tabela.
"""
