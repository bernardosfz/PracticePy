numero = int(input("Digite o número de páginas: "))
inteiros =(1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
romanos = ("M", "CM,", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I")
numConvertido = 0

if 0 < numero < 1000:
    for i in range (len(inteiros)):
        divisao = int(numero / inteiros[i])
        numConvertido = (romanos[i]*divisao)
        print(numConvertido, end="")
        numero = numero - (inteiros[i] * divisao)
else:
    print("Número Inválido")
