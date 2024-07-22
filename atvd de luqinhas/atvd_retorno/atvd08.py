estado= input("informe se tu é idoso, gestante ou PCD. Caso nada se aplique a você, digite(EU SO O MILIOR): ")

if estado == "idoso" or estado == "gestante" or estado == "PCD":
    print("voce ta na fila d prioridade")
else:
    print("vai pro fim da fila, rapaz")