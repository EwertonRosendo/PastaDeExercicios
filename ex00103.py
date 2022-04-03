

def ficha(nomeJogador="<DESCONHECIDO>", qtdGols="<NAO INFORMADO>"):
    if qtdGols.isnumeric():
        int(qtdGols)
    else:
        qtdGols = 0
    if nomeJogador.isalpha():
        str(nomeJogador)
    else:
        nomeJogador = "<DESCONHECIDO>"
    print(f"{'~'*15}FICHA{'~'*15}")
    return f"Nome do JOGADOR     - [{nomeJogador}]\nQuantidade de gols  - [{qtdGols}]"
print(ficha(nomeJogador=str(input("Nome do jogador: ")), qtdGols=str(input("Quantidade de gols: "))))
