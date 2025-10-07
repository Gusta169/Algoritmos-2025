import random

# Crie um vetor e armazene os números de 1 a 100.
lista = [0] * 100
for i in range(0, len(lista)):
    lista[i] = i + 1

# Mostre na tela todos os números do vetor em ordem crescente (1 a 100).
for i in range(0, len(lista)):
    print( lista[i], end=" ")
print("")

# Mostre na tela todos os números do vetor em ordem decrescente (100 a 1).
for i in range(len(lista)-1, -1, -1):
    print( lista[i], end=" ")
print("")

# Mostre na tela o dobro de todos os números.
for i in range(0, len(lista)):
    dobro = lista[i] * 2
    print( dobro, end=" ")
print("")

# Apresente na tela a soma de todos os números.
soma = 0
for i in range(0, len(lista)):
    soma = soma + lista[i]
print(f"A soma dos números é {soma}")

# Apresente na tela a média geral dos valores contidos na lista
media = soma / len(lista)
print(f"A média dos valores é {media}")

# Conte os números pares
pares = 0
for i in range(0, len(lista)):
    if(lista[i] % 2 == 0):
        pares = pares + 1

# Faça um programa para armazenar 6 números 
# inteiros para uma loteria, permitindo que 
# o usuário informe os números. 
# Depois de preencher, informe uma mensagem 
# e os números sorteados.        
sorteio = [0] * 6
for i in range(0, len(sorteio)):
    sorteio[i] = int(input("Número da loto: "))

print("Números sorteados:", end=" ")
for i in range(0, len(sorteio)):
    print(sorteio[i], end=" ")
print("")

# Sorteio de números aleatórios
sorteio = [0] * 6
for i in range(0, len(sorteio)):
    sorteio[i] = random.randint(1, 60)

print("Dados do sorteio:", sorteio)