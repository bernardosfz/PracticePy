vetor = []
codigo = int(input("Digite o código: "))

if codigo == 1 or codigo == 2:
    for i in range(5):
        vetor.append(input("Digite um valor: "))
    if codigo == 1:
        for i in range(5):
            print(vetor[i], end=" ")
    elif codigo == 2:
        for i in range(4,-1,-1):
            print(vetor[i], end=" ")
        
else:
    print("Fechando programa......")
