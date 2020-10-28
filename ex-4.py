salAtual = float(input("Salário Atual: "))
cargo = str(input("Cargo: "))
cargo = cargo.upper()

if cargo == "AUXILIAR DE ESCRITORIO":
    reajuste = salAtual*0.07

if cargo == "SECRETARIO" or cargo == "SECRETARIA":
    reajuste = salAtual*0.09

if cargo == "COZINHEIRO" or cargo == "COZINHEIRA":
    reajuste = salAtual*0.05

if cargo == "ENTREGADOR" or cargo == "ENTREGADORA":
    reajuste = salAtual*0.12

# Valor do reajuste
print("Reajuste:","%.2f"%reajuste,"R$")
# Novo salário
salNovo = salAtual+reajuste

print("Novo Salário:","%.2f"%salNovo,"R$")