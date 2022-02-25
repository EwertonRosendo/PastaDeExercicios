from time import sleep
jogador = dict()
#  Solicitando as informações do jogador.. Nome, numero de partidas jogadas e numero de gols por partida..
jogador["nome"] = str(input("Informe o nome do jogador: ")).strip()
jogador["n_de_partidas"] = int(input("Informe o numero de partidas jogadas: "))
jogador["Gols por partida"] = []
for c in range(0, jogador["n_de_partidas"]):
    jogador["Gols por partida"].append(int(input(f"Informe quantos gols na partida {c}: ")))
jogador["Total de gols"] = sum(jogador["Gols por partida"])
print("-="*20)
print(jogador)
print("-="*20)
for k, v in jogador.items():
    sleep(1)
    print(f"O campo {k} tem o valor {v}")
print("-="*20)
print("O jogador {} jogou {} partidas.".format(jogador["nome"], jogador["n_de_partidas"]))
for c, g in enumerate(jogador["Gols por partida"]):
    print(f"=> Na partida {c}, fez {g} gols.")
    sleep(1)
