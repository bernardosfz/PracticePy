import random

vetor = []
palpite = []
acertos = 0
for i in range(6):
    numero = random.randint(1,60)
    vetor.append(numero)

for j in range(6):
    chute = int(input("Informe um número: "))
    if chute in vetor:
        acertos = acertos + 1
        palpite.append(chute)

print("Numero de acertos: ", acertos)
print("Numeros sorteados: ", vetor)
print("Numeros que voce acertou: ", palpite)
