perguntas= ["Telefonou para a vítima?",
"Esteve no local do crime?",
"Mora perto da vítima?",
"Devia para a vítima?",
"Já trabalhou com a vítima?"
]

s = 0
for a in perguntas:
    print(a)
    resposta= input("Responda a pergunta com S=sim e N=não: ").upper()
    if a == "Esteve no local do crime?":
        if resposta == "S":
            print("suspeito")
            s += 1
    elif a == "Mora perto da vítima?":
        if resposta == "S":
            print("cumplice")
            s += 1
    elif a == "Devia para a vítima?":
        if resposta == "S":
            print("cumplice")
            s += 1
    elif a == "Já trabalhou com a vítima?":
        if resposta == "S":
            print("assassino")
            s += 1

if s > 0:
    print("calma ae amigao, vai pra onde")
else:
    print("ta livre irmão")
