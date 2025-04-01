#exercicio05 se esta aprovodado ou reprovado
nota01 = float(input("digite a nota 1: "))
nota02 = float(input("digite a nota 2: "))
nota03 = float(input("digite a nota 3: "))
media = (nota01 + nota02 + nota03)/3

if media>=7:
    print(f"você foi aprovado, sua média é {media}")
elif media<=4:
    print(f"você está reprovado, sua media foi {media}")
else:
    print(f"você está em recuperação, sua média é {media}")