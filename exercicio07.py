#exercicio07
comb =  input("digite o tipo de combustivel:\n"
              "G ou g pra gasolina\n "
              "E ou e pra etanol\n ")
litros = float(input("digite aqui o litro: "))
Vgas = 5.8
Veta = 4.9
if comb == "G":
    valor = litros * Vgas
else:
    valor = litros * Veta
print(f"você gastou em R${valor:.2f}")
