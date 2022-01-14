preco = 0
nomebarato = ""
precobarato = 0
maisde1000 = 0
while True:
    # Validação do nome
    nome = str(input("Informe o nome do produto: ")).strip()
    while nome in " 0 1 2 3 4 5 6 7 8 9 -1 -2 -3 -4 -5 -6 -7 -8 -9":
        nome = str(input("Informe um nome valido para o produto"))
    # Validação do preço
    preco = float(input("Informe o preço para o produto: "))
    # Recebendo o primeiro valor
    if nomebarato == "":
        nomebarato = nome
        precobarato = preco
    # Verificando se o preço é negativo
    while preco < 0:
        preco = float(input("Informe um valor valido para o produto: "))
    if preco > 1000:
        maisde1000 += 1
    if preco < precobarato:
        precobarato = preco
        nomebarato = nome
    # Verificando se o usuario deseja continuar
    duvida = str(input("Quer continuar? [S/N]")).upper()
    while duvida not in "S N":
        duvida = str(input("Informe um valor valido[S/N]: ")).upper()
    if duvida == "N":
        break
    # FIM
print(f" O produto mais barato foi {nomebarato} por {precobarato}R$")
if maisde1000 == 1:
    print("Um produto custou mais de 1000R$")
elif maisde1000 > 1:
    print(f" {maisde1000} produtos custaram mais de 1000R$ ")
elif maisde1000 < 0:
    print("Nenhum produto custou mais de 1000R$")
