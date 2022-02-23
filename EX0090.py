lista_de_alunos = []
nome_e_media = dict()
continuar = "k"
while True:
    nome_e_media = {"Nome": str(input("Informe o nome")), "Nota": float(input("Informe a nota: ")), "Situação": ""}
    if nome_e_media["Nota"] >= 7:
        nome_e_media["Situação"] = "Aprovado"
    else:
        nome_e_media["Situação"] = "Recuperação"
    lista_de_alunos.append(nome_e_media.copy())
    nome_e_media.clear()
    continuar = str(input("Deseja continuar? [S/N]")).upper().strip()
    while continuar not in "S N":
        continuar = str(input("Informe um valor valido: [S/N]")).strip().upper()
    if continuar in "N":
        break
print(lista_de_alunos)
for n in lista_de_alunos:
    for k, v in n.items():
        print(f" {k} igual a {v} ", end="")
        print()
