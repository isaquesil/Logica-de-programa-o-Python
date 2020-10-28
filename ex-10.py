saldoMedio = float(input("Saldo médio do último ano: "))

if  saldoMedio < 500 or saldoMedio <= 0:
    print("Você não tem direito a crédito")

elif saldoMedio > 500 and saldoMedio <= 1000:
    credito = saldoMedio*0.30
    print("Saldo Médio:",saldoMedio,"R$")
    print("Valor de Crédito:","%.2f"%credito,"R$")

elif saldoMedio > 1000 and saldoMedio <= 3000:
    credito = saldoMedio*0.40
    print("Saldo Médio:",saldoMedio,"R$")
    print("Valor de Crédito:","%.2f"%credito,"R$")

elif saldoMedio > 3000:
    credito = saldoMedio*0.50
    print("Saldo Médio:",saldoMedio,"R$")
    print("Valor de Crédito:","%.2f"%credito,"R$")
