nome = int(len(input("fale seu nome: ")))
idade = int(input("digite sua idade: "))
salario = float(input("Fale seu salario: "))
sexo = input("fale seu sexo (f ou M): ")
estadoCivil= input("Digite seu estado civil(S,C,V e D): ")

nome= int(len(nome))

while nome <= 3 or idade > 150 or salario <= 0:
    if  nome <= 3:
        print("Seu nome precisa ser maior que 3 caractere.")
        nome = int(len(input("fale seu nome: ")))
    elif idade >= 150:
        idade = int(input("sua idade precisa ta menor que 150anos: "))
    elif salario <= 0:
        salario = int(input("Fale seu salario, novamente: "))
    else:
        print("ta tudo ok")

print("ta tudo ok")
 