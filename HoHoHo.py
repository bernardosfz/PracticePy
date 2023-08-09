n = int(input("Digite um valor entre 0 e 10: "))

if n > 10 or n < 0:
    n = False
    print("Digite um número válido")
else:
    print("Ho " * n, end="!")
