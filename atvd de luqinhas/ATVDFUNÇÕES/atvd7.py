def inteiros(numeros):
    somNum = 0
    numero = [int(num) for num in numeros]
    for a in numero:
        somNum += a
    print(f"A soma de todos numeros são de: {somNum}")
    print(f"A lista somada foi de {numero}")

numero = input("DIgite varios numeros inteiros: ").split(",")
inteiros(numero)