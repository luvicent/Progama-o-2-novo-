print("Digite M para matutino,Digite V para Vespetino e Digite N para Noturno")

turno= input("digite o turno que você estuda: ").upper()

if turno == "M":
    print("Bom dia")
elif turno == "V":
    print("Boa tarde")
elif turno == "N":
    print("Boa noite")
else:
    print("Digita a letra certa ze ruela")