perguntas = ["Telefonou para a vítima? (1) Sim (0) Não: ", "Esteve no local do crime? (1) Sim (0) Não: ", "Mora perto da vítima? (1) Sim (0) Não: ", "Devia para a vítima? (1) Sim (0) Não: ", "Já trabalhou com a vítima? (1) Sim (0) Não: "]

soma = 0
for resposta in perguntas:
    soma = soma + int(input(resposta))

if soma < 2:
    print("Inocente")
elif soma == 2:
    print("Suspeito")
elif soma <= 4:
    print("Cúmplice")
else:
    print("Assaltante")
