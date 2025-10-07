# Importa a biblioteca de geração de números
import random

# Recebe os valores informados pelo usuário
min = int(input("Informe um valor mín: "))
max = int(input("informe um valor max: "))

# Confere se os valores estão na ordem correta
if (min > max):
    # Se estiver invertido, faz a troca de valores
    a = min
    min = max
    max = a

# Recebe a quantidade de números que serão gerados
# Será usado para controlar a quantidade de repetições do FOR
quantidade = int(input("quantidade: "))

# Variável para armazenar a soma
soma = 0

# Variável para armazenar o maior valor
maior = 0
# Também é possível atribuir ao maior valor o min gerado do intervalo, assim todo valor será maior que ele
# maior = min

# Variável para armazenar o menor valor
menor = 0
# Também é possível atribuir ao menor valor o max gerado do intervalo, assim todo valor será menor que ele
# menor = max

# Cria o laço de repetição
for i in range(0, quantidade):
    # Gera um valor no intervalo definido
    x = random.randint(min,max)

    # Se for a primeira rodada do for, então X vai ser o maior e o menor
    # Se usar a ideia do min e max das linhas 25 e 30 não precisa desse if
    if(i==0):
        maior = x
        menor = x
    
    # Pega o valor da soma atual e adiciona o valor gerado
    soma = soma + x

    # Comparar o valor gerado com o maior armazenado
    if(x > maior):
        maior = x

    # Comparar o valor gerado com o menor armazenado
    if(x < menor):
        menor = x

    # Apresenta o valor na tela
    print(x)

# Apresentar ao final do programa o relatório:
# a soma dos valores gerados
print(f"A soma é {soma}")

# o maior valor gerado
print(f"O maior valor gerado é {maior}")

# o menor valor gerado
print(f"O menor valor gerado é {menor}")   