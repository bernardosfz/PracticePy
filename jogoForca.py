palavra = input("PALAVRA: ").upper()
chutes = []
acertos = 0
while acertos < len(palavra):
        for letra in palavra:
                if letra in chutes:
                      print(letra, end=" ")
                      acertos += palavra.count(tentativa)
                else:
                        print('_', end=" ")
        tentativa = input("\n DIGITE UMA LETRA: ").upper()
        chutes.append(tentativa)
print("Parabéns")
