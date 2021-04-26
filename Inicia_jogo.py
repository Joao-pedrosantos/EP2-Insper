def inicia_jogo():
	print("Bem vindo ao paciencia!")
	a = input(str("Voce quer jogar (s/n)? "))
	if a == "s":
		return seleciona_cartas
	else:
		print("Ok :(")

def seleciona_cartas():
	return "aa"

print(inicia_jogo)