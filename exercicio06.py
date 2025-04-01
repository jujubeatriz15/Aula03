time01 = input("digite aqui o nome do 1 time:")
golstime01 = int(input(f"quantos gols o {time01}: "))
time02 = input("digite aqui o nome do 2 time:")
golstime02 = int(input(f"quantos gols o {time02}: "))

if golstime01 == golstime02:
    print("empate!")
elif golstime01>golstime02:
    print(f"O {time01} ganhou!")
else:
    print(f"O {time02} ganhou!")