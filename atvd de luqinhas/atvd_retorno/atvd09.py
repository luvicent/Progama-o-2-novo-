usuario = input("fale nome de usuario: ")
senha = input("fale sua senha: ")

while senha == usuario:
    print("mude de senha. a senha não pode ser ingual nome de usuario.")
    senha = input("mude a sua senha: ")