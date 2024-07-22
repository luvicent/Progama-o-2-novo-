def maior(lista):
    maior = lista[0]
    for a in lista:
        if a >= maior:
            maior = a
    print(maior)

def menor(lista):
    menor = lista[0]
    for a in lista:
        if a <= menor:
            menor = a
    print(menor)

numeros = input("digite uma lista de numeros: ").split(",")
numero = [int(num) for num in numeros]

maior(numero)
menor(numero)