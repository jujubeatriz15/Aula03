#atividade do dia 01/04
nome = input("digite seu nome ")
idade = int(input("digite sua idade "))
salario = float(input("qual o seu salario: "))
aumento = float(input("qual foi o percentual do seu aumento: "))
valorReal = salario*aumento/100
novoSalario = salario+valorReal
print(f"Ola {nome} sua idade é {idade} e seu salario é {salario}")
print(f"Seu aumento foi {novoSalario}")
