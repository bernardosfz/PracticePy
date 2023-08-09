username = "admin"
password = "123"

print("Bem Vindo!")
user = input("User: ")
senha = input("Senha: ")

if user == username and senha == password:
    print("Acesso Liberado")
else:
    print("Usuário ou senha incorretos")
