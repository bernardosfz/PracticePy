tamanhoPedido = int(input("Digite quantos produtos serão comprados: "))

cardapio = [1001, 1002, 1003, 1004, 1005]
print(""" CÓDIGOS DOS PRODUTOS:
      1001   1002    1003    1004    1005
      1,50   2,50    3.50    4.50    5.50     
        """)

i = 1
valor = 0
total = []

while i <= tamanhoPedido:
    produtos = int(input("Digite o código do produto " +str(i)+ ": "))
    quantidade = int(input("Digite a quantidade do produto " +str(i)+ ": "))
    print(produtos,quantidade)

    if produtos - cardapio[0] == 0:
            valor = 1.50 * quantidade
            total.append(valor)
    elif produtos - cardapio[1] == 0:
            valor = 2.50 * quantidade
            total.append(valor)
    elif produtos - cardapio[2] == 0:
            valor = 3.50 * quantidade
            total.append(valor)
    elif produtos - cardapio[3] == 0:
            valor = 4.50 * quantidade
            total.append(valor)
    elif produtos - cardapio[4] == 0:
            valor = 5.50 * quantidade
            total.append(valor)

    i = i + 1
print("Total: ", sum(total))
