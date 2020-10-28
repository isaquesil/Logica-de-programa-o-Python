print("Escolha seu destino")
print("A - Região Norte")
print("B - Região Nordeste")
print("C - Centro-Oeste")
print("D - Região Sul")
destino = str(input(""))
destino = destino.upper()
retorno = str(input("Inclui retorno? s/n: "))
retorno = retorno.upper()
if retorno != "S" and retorno != "N":
    print("Retorno inválido")
if destino=="A":
    if retorno == "N":
        print("Passagem de ida para Região Norte é R$ 500,00")
    elif retorno == "S":
        print("Passagem de ida e volta para Região Norte é R$ 900,00")
elif destino=="B":
    if retorno == "N":
        print("Passagem de ida para Região Nordeste é R$ 350,00")
    elif retorno == "S":
        print("Passagem de ida e volta para Região Nordeste é R$ 650,00")
elif destino=="C":
    if retorno == "N":
        print("Passagem de ida para Região Centro-Oeste é R$ 350,00")
    elif retorno == "S":
        print("Passagem de ida e volta para Região Centro-Oeste é R$ 600,00")
elif destino=="D":
    if retorno == "N":
        print("Passagem de ida para Região Sul é R$ 300,00")
    elif retorno == "S":
        print("Passagem de ida e volta para Região Sul é R$ 550,00")
else :
    print("Destino inválido")
