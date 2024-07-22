def converter_hora(hora):
	if hora > 12 and hora != 24:
		contador = 0
		for x in range(hora):
			if x >= 12:
				contador+=1
		return contador
	elif hora == 24:
		return 0
	else:
		return hora
controle = 1
while controle != 0:
	hora = int(input("Digite a hora a ser convertida: "))
	minuto = int(input("Digite o minuto: "))
	print("Convertido: %i:%i"%(converter_hora(hora),minuto))
	controle = input("Continuar? 1(sim)/0(nao): ")
print("Obrigado até mais")