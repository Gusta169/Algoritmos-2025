# # # # # # # # # # # ##
# Exercício 1 - Frutas #
# # # # # # # # # # # ##

# precosFrutas = [0.0] * 6

# for i in range(0, len(precosFrutas)):
#     # Fruta 1 - R$9.99
#     msg = f"Fruta {i+1} R$"
#     precosFrutas[i] = float(input(msg))
# print("-------------------------")

# for i in range(0, len(precosFrutas)):
#     msg = f"Fruta {i+1}: R${precosFrutas[i]}"
#     print(msg)


# # # # # # # # # # # # # # ##
# Exercício 2 - Temperaturas #
# # # # # # # # # # # # # # ##

# Importar a biblioteca random
import random
# Cria o vetor com 24 posições (o índice representa o horário)
temperaturas = [0] * 24

# Preenche com valores aleatórios
for i in range(0, len(temperaturas)):
    temperaturas[i] = random.randint(25,30)

# Exibe na tela só pra conferência do programador
print(temperaturas)

# Cria variáveis para armazenar alguns dados a serem analisados
# Armazena a maior temperatura
maiorT = temperaturas[0]
# Armazena o horário (índice) da maior temperatura
maiorH = 0
# Armazena a soma das temperaturas
soma = 0

# Percorre o vetor
for i in range(0, len(temperaturas)):
    # Faz a soma das temperaturas
    soma += temperaturas[i] 
    # Verifica se a temperatura em i é a maior encontrada
    if(temperaturas[i] > maiorT):
        # Atualiza o valor da maior temperatura
        maiorT = temperaturas[i]
        # Atualiza o horário da maior temperatura
        maiorH = i

# Faz a média e exibe outras informações
media = soma / len(temperaturas)
print(f"A temperatura média é {media} graus.")
print(f"A maior temperatura é {maiorT} graus.")
print(f"Registrada às {maiorH}h.")

# Cria uma variável para contar quantas vezes aparece a maior temperatura
cont = 0
for i in range(0, len(temperaturas)):
    if(maiorT == temperaturas[i]):
        cont += 1

print(f"{maiorT} graus foi registrado {cont} vezes.")

# Cria um vetor para armazenar os "cont" horários da maior temperatura
horarios = [0] * cont
# Cria uma variável de controle para percorrer esse vetor
controle = 0

# Percorre o vetor completo de temperaturas
for i in range(0, len(temperaturas)):
    # Se identificar a maior
    if(maiorT == temperaturas[i]):
        # Adiciona o horário (índice) no vetor de horários
        horarios[controle] = i
        # Aumenta o valor da variável de controle para depois armazenar outro horário (índice)
        controle += 1 

# Percorre o vetor de horários e exibe na tela os valores
print("Horários de maior temperatura:")
for j in range(0, len(horarios)):
    print(f"{horarios[j]}h")