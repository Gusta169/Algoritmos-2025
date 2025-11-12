class Aluno:
    def __init__(self):
        self.nome = ""
        self.idade = 0 

aluno1 = Aluno()
aluno1.nome = ("Gustavo")
aluno1.idade = 18

class Ventilador:
    def __init__(self):
        self.marca = ""
        self.voltagem = 0
        self.numero_de_velocidades =  0
        self.velocidade_atual = 0
def aumentarVelocidade(ventilador):
    if(ventilador_1.velocidade_atual < ventilador_1.numero_de_velocidades):
        ventilador.velocidade_atual += 1

ventilador_1 = Ventilador()
ventilador_1.marca = "delta premmium"
ventilador_1.voltagem = 110
ventilador_1.numero_de_velocidades = 4
ventilador_1.velocidade_atual = 0

print(ventilador_1.velocidade_atual)
aumentarVelocidade(ventilador_1)
print(ventilador_1.velocidade_atual)
