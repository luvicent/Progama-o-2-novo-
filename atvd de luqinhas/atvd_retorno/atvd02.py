vogais= ["A","E","I","O","U"]

letra = input("Digite uma letra: ").upper()

if letra in vogais:
    print(f"essa letra é uma vogal:")
else:
    print(f"essa letra não é uma vogal")