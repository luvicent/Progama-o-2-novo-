def cadastro():
    usuario = input("deseja cadastrar C pra cliete ou F pra funcionario").upper()
    cliente = []
    funcionario = []
    if usuario == "C":
        cliente.append(input("Fale NOME do cliente: "))
        cliente.append(input("Fale CPF do cliente: "))
        cliente.append(input("Fale ENDEROÇO do cliente: "))
        print(cliente)
    elif usuario == "F":
        funcionario.append(input("Fale NOME do funcionario: "))
        funcionario.append(input("Fale CPF do funcionario: "))
        funcionario.append(input("Fale ENDEROÇO do funcionario: "))
        print(funcionario)
    else: 
        print("erro")
    
    

cadastro()