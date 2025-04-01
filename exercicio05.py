#exercicio05 se esta aprovodado ou reprovado
nota01 = float(input("digite a nota 1: "))
nota02 = float(input("digite a nota 2: "))
nota03 = float(input("digite a nota 3: "))
media = (nota01 + nota02 + nota03)/3

if media>=7:
    print(f"você foi aprovado, sua média é {media:.2}")
else:
    print(f"você foi reprovado, sua média é {media:.2}")