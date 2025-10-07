# Crie um programa que abra (ou crie) um arquivo chamado frutas.txt e escreva nele 5 nomes de frutas, um em cada linha. Use o modo de abertura w.

arquivo = open("frutas.txt", "w", encoding="utf8")

arquivo.write("Abacaxi\n")
arquivo.write("Limão\n")
arquivo.write("Uva\n")
arquivo.write("Kiwi\n")
arquivo.write("Banana\n")

arquivo.close()

#Crie um programa que leia o conteúdo do arquivo frutas.txt e mostre cada fruta precedida da frase:
# "Eu adoro a fruta: <fruta>"

arquivo = open("frutas.txt", "r", encoding="utf8")

linhas = arquivo.readlines()

for i in range(0,len(linhas)):
    print(f"Eu adoro a fruta: {linhas [i]}")

arquivo.close()

#Agora abra o arquivo frutas.txt no modo a e adicione mais 3 frutas. Depois, leia e exiba todo o conteúdo novamente.

arquivo = open("frutas.txt", "a", encoding="utf8")

arquivo.write("Morango\n")
arquivo.write("Pessego\n")
arquivo.write("Tangerina\n")

arquivo.close()

# Crie um programa que apague todo o conteúdo do arquivo frutas.txt (dica: modo w sem escrever nada) e escreva apenas: "Desculpe, esqueci tudo 😅"

arquivo = open("frutas.txt", "w", encoding="utf8")

arquivo.write("Desculpe, esqueci tudo 😅")

arquivo.close()

#Lista de compras interativa
#Peça para o usuário digitar 5 itens de compra e escreva cada um em uma nova linha no arquivo compras.txt.

arquivo = open("compras.txt", "w", encoding="utf8")
itens = [0] * 5

for i in range(0, len(itens)):
    itens [i] = input(f"Digite {i+1} itens de compras: ")
    arquivo.write(f"{itens[i]}\n")

arquivo.close()
