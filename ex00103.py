jogador = dict()

def ficha(nomeJogador="<DESCONHECIDO>", qtdGols="<NAO INFORMADO>"):
    jogador["nome"] = nomeJogador
    jogador["gols"] = qtdGols

    print(f"{'~'*15}FICHA{'~'*15}")
    return f"Nome do JOGADOR     - [{jogador['nome']}]\nQuantidade de gols  - [{jogador['gols']}]"
print(ficha(nomeJogador=str(input("Nome do jogador: ")), qtdGols=str(input("Quantidade de gols: "))))
