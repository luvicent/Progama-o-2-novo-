numA= int(input("fale um numero: "))
numB= int(input("fale um numero: "))

for a in range(numA, numB+1):
    if a == numB:
        print(a, end=". ")
    else:
        print(a, end=", ")