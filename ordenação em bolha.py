def ordenar_bolha(vet):
    # Controla a quantidade de ciclos/repetições do algoritmo que faz as trocas e verificações
    for ciclo in range(0, len(vet)-1):
        # i começa em 0 e vai até n-1, por isso len(vet)-1
        for i in range(0, len(vet)-1):
            # compara o valor na pos i e o da frente i+1
            if(vet[i] > vet[i+1]):
                # Salva o num no vet[i]
                troca = vet[i]
                # altera o valor no vet[i] para o num da frente
                vet[i] = vet[i+1]
                # Recupera o valor original do vet[i]
                vet[i+1] = troca
        print(f"Fim do {ciclo+1}º ciclo: {vet}")
    return vet


vet = [32, 9, 12, 3, 68, 27, 15]
print(f"Vetor original: {vet}")

vet_ordenado = ordenar_bolha(vet)
print(f"Vetor ordenado: {vet_ordenado}")