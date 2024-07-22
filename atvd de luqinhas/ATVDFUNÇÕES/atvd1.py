def saudaçoes(nome):
    for nomes in nome:
        print(f"saudações: {nomes}")

nome = input("Fale nomes de pessoas: ").split(",")
saudaçoes(nome)