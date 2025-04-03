#exercicio07
comb =  input("digite o tipo de combustivel:\n"
              "G pra gasolina\n "
              "E pra etanol\n ")
litros = float(input("qual o litro: "))
Vgas = 5.8
Veta = 4.9
if comb == "G":
    valor = litros * Vgas
else:
    valor = litros * Veta

print(f"você gastou em R${valor:.2f}")