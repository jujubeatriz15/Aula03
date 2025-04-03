#exercicio07
comb =  input("digite o tipo de combustivel:\n"
              "G pra gasolina\n "
              "E pra etanol\n ")
litros = float(input("digite aqui o litro: "))
Vgas = 5.8
Veta = 4.9
if comb == "G" or comb == "g":
    valor = litros * Vgas

elif comb == "E" or comb == "e":
    valor = litros * Veta
else:
    print("tipo de combustível invalido!")
print(f"você gastou em R${valor:.2f}")
