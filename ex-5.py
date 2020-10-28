print("1 - Homem \n2 - Mulher")
sexo = int(input(""))
altura = input("Sua altura: ")
peso = 0.0

if sexo == 1:
	peso = (72.7*float(altura)) - 58
elif sexo == 2:
	peso = (62.1*float(altura)) - 44.7
else:
	print("Altura inválida")
	
print("Peso Ideal:","%2.f"%peso,"Kg")
