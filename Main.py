num = int(input("Número: ")) 

x = int(input("Valor inicial: "))
y = int(input("Valor final: "))

for i in range(x, y+1): ##cria uma variavel e adiciona a quantidade que ele fará o ciclo
    print(f"{num} X {i} = {num*i}") 