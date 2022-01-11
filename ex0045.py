import random
print("Vamos jogar pedra, papel, tesoura")
print("1- Pedra")
print(("2- Papel"))
print("3- Tesoura")
humano = int(input())
possibilidades = ["Pedra","Papel", "Tesoura"]
maquina = random.choice(possibilidades)
lista = ["Pedra", "Papel", "Tesoura"]
if humano == 1 and maquina=="Pedra" or humano == 2 and maquina == "Papel" or humano == 3 and maquina =="Tesoura":
    print("\033[33m Houve um empate, {} x {}\033[m".format(lista[(humano-1)], maquina))
elif  humano == 1 and maquina =="Tesoura" or humano == 2 and maquina =="Pedra" or humano == 3 and maquina == "Papel":
    print("\033[32m O humano venceu! {} x {}\033[m".format(lista[humano-1], maquina))
else:
    print("\033[31m A maquina venceu! {} x {}\033[m".format(lista[humano-1], maquina))

