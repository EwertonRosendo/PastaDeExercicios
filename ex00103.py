jogador = dict()

def ficha(nomeJogador="", qtdGols="-1"):
    jogador["nome"] = nomeJogador
    jogador["gols"] = qtdGols

    if nomeJogador in "":
            jogador["nome"] = "<DESCONHECIDO>"
    if qtdGols in "-1":
            jogador["gols"] = "<GOL NAO INFORMADO>"

    print(f"{'~'*15}FICHA{'~'*15}")
    print(f"Nome do JOGADOR     - [{jogador['nome']}]")
    print(f"Quantidade de gols  - [{jogador['gols']}]")
ficha(nomeJogador=str(input("Nome do jogador: ")), qtdGols=str(input("Quantidade de gols: ")))
