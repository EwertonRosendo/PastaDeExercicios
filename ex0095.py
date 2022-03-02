jogador = dict()
lista_de_jogadores = []
lista = []
print("_"*38)
contador = 0
while True:
    jogador["nome"] = str(input("Informe o nome do jogador: ")).strip()
    jogador["partidas"] = int(input("Informe quantas partidas foram jogadas: "))
    jogador["gols marcados"] = []
    for c in range(0, jogador["partidas"]):
        jogador["gols marcados"].append((int(input("Partida {}: ".format(c)))))
    lista.append(jogador.copy())
    lista_de_jogadores.append(lista[:])
    lista.clear()
    print("=-" * 20)
    print("Ultimo jogador cadastrado:")
    for k, v in jogador.items():
        print(f"{k}: {v}")
    jogador.clear()
    print("=-"*20), print()
    print(lista_de_jogadores), print()
    print("=-" * 20)
    continuar = str(input("Deseja continuar? [S/N]")).strip().upper()
    while continuar not in "S N NAO SIM NÃO":
        continuar = str(input("Informe um valor valido[S/N]: ")).upper().strip()
    if continuar in "NAO N NÃO":
        break
for cod, j in enumerate(lista_de_jogadores):
    print(f"{cod} ---- {j}")
while True:
    contador = int(input("Mostrar dados de qual jogador? "))
    for k in lista_de_jogadores[contador][0]['gols marcados']:
        print(f"No jogo {enumerate(k)} fez {k} gols")
