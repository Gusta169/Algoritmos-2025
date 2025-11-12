def cadastrar(nome, valor, data):
    nome = input("Digite o nome")
    valor = float(input("Digite o valor"))
    data = input("Informea data: ")
    return nome, valor, data

def alterar():
    novo_nome = input("Informe o novo nome: ")
    novo_valor = float(input("informe o novo valor: "))
    nova_data = input("Informe a nova data: ")
    return novo_nome, novo_valor, nova_data
    
def excluir():
    ID = int(input("Informe o ID do produto a excluir: "))
    return ID