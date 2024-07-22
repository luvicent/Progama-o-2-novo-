def sla():
    pais = input("digite o valor e o pais que quer converter a moeda(dolar, euro, peso): ").split(",")
    
    if pais[0] == "dolar":
        print(int(pais[1])*0.18)
    elif pais[0] == "euro":
        print(int(pais[1])*0.18)
    elif pais[0] == "peso":
        print(int(pais[1])*0.18)
    else:
        print("erro")
sla()