# #Matriz

# linhas = 4 
# colunas = 3
# matriz = [0] * linhas
# for i in range( 0, linhas):
#     matriz[i] = 0 * colunas
# print(matriz)

# matriz[1][2] = 5

# print(matriz)

# #Classes

# class Disciplina:
#     def __init__(self):
#         self.id = 0
#         self.nome = ""
#         self.ch = ""
#         self.professor = ""

# #Listas 
# lista = []
# print(lista)


# lista.append(5) #append - insere no fim
# lista.append("Aula")
# lista.append(80.2)

# print(lista)
# lista.insert(2, "oi") #insere no indice iformado
# print(lista)

# lista.pop(2) #exclui o valor do indice
# print(lista)

# lista.remove(80.2) #exclui até encontrar oque foi colocado

# print(lista)

#-----------------------------------------------------------

#exercicio

# lista = []
# for i in range(0, 5):
#     usuario = input("Digite os nomes: ")
#     lista.append(usuario)

# for i in range(0, len((usuario))):
#     usuario = input("Digite o nome que voce deseja remover: ")
#     lista.remove(usuario)
#     break
# print("--------Lista Final-------")
# for i in range(0, len(lista)):
#     print(lista[i])

#Tuplas
#Tuplas são imutaveis
# tuplas = ("Ayslan", 40, 8,79, False)
# print(tuplas[2])
# print(tuplas)

# nome = input("Informe o nome do Produto: ")
# preço = float(input("Informe o preço do produto"))
# estoque = int(input("Informe q quantidade que contem no estoque"))

# produto = (nome, preço, estoque)

# for i in range(0, len(produto)):
#     print(produto[i])
#     tamanho = len(produto)

# print(f"tamanho da tupla {tamanho}")

#Conjuntos

# conjunto = set()
# conjunto.add(1)
# conjunto.add(4)
# conjunto.add(7)
# conjunto.add(9)
# conjunto.add(1)

# turma_a = {"Ana", "Beto", "Carlos", "Duda"}
# turmba_b = {"Carlos", "Edu", "Fernanda", "Ana"}

#Dicionario (dict)
#chave : valor
#Exemplo:
pessoa = {
    "nome": "Alberto",
    "idade": 35,
    "filhos": {"Pedro", "Maria"},
    "formacao": ["Informatica", "Egenharia de Software"],
    "profissao": {
        "empresa": "Google",
        "cargo": "Desenvolvedor"
    }
}

#exercicio

aluno = {
    "nome": "Amauri",
    "idade": 13,
    "curso": {"Engenharia de software"}
}

print("-_Lista_-")
print("Nome: ", aluno["nome"])
print("Idade: ", aluno["idade"])
print("curso: ", aluno["curso"])

aluno ["idade"] = int(input("Nova idade: "))

aluno["nota"] = int(input("Nova nota: "))

for chave, valor in aluno.item():
    print(f"{chave} é {valor}")