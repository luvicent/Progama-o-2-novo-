number = int(input('Numero: '))

if number >= 1:
    for i in range(1, number):
        if number % i != 0:
            print(number, 'é primo')
        else:
            print(number, 'não é primo')
            break
elif number == 0:
    print(number, 'é zero')
else:
    print(number, 'é negativo')