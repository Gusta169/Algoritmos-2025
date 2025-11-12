# Crie uma classe Pessoa com os atributos nome e idade, e um método apresentar() que imprime:
# "Olá, meu nome é <nome> e tenho <idade> anos."

class Pessoa: #define a classe.
    def __init__(self, nome, idade): #__init__ -> é o construtor (roda quando o objeto é criado). / #self -> referência ao próprio objeto.
        self.nome = nome 
        self.idade = idade #self.marca, self.cor → atributos do objeto.

    def mostrar(self):
        print(f"Ola, meu nome é {self.nome} e tenho {self.idade} anos.")

#Herança da classe Pessoa:

class Cliente:
    def __init__(self, nome, idade, conta):
        super.__init__(nome, idade)
        self.conta = conta
    
    def mostrar(self):
        print(f"O nome é {self.nome} contém {self.idade} de idade e é cliente") 
        self.conta.mostrar_saldo() #Utilização de um objeto dentro de outro objeto retirado da conta bancaria.

class Funcionario:
    def __init__(self, nome, idade, cargo, ):
        super.__init__(nome, idade)
        self.cargo = cargo
    
    def mostrar(self):
        print(f"O nome é {self.nome} com {self.idade} no cargo de {self.cargo}")
        
# Crie uma classe ContaBancaria com:

# atributos: titular, saldo

# métodos: depositar(valor), sacar(valor) e mostrar_saldo()
#. Encapsulamento — melhorando a classe ContaBancaria:
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo #Deixa privado conseguindo ter acesso apenas pelo metodos da classe
    
    def depositar(self, valor):
        if(valor > 0): 
            self.saldo += valor
            print(f"Deposito de R${valor:.2f} realizado com sucesso!")
        else:
            print(f"Valor invalido")
    
    def sacar(self, valor):
        if(self.__saldo <= valor):
            self.saldo -= valor
            print(f"Saque de valor R${valor:.2f} realizado com sucesso!")
        else:
            print("Saldo Insuficiente")
    def mostrar_saldo(self):
        print(f"Salto atual de {self.titular}: R${self.saldo:.2f} ")

#Crie uma classe Livro com atributos titulo, autor e ano, e um método descricao() que retorna uma string formatada.

class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
    def descricao(self):
        print(f"O titulo do livro é {self.titulo}, sendo o autor {self.autor} criado no ano {self.ano}")

#Modo de utilizar:
livro1 = Livro("Dom Casmurro", "Machado de Assis", 1899) 
livro1.descricao()
