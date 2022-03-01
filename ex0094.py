pessoa = dict()
listagem = []
soma_idade = 0
while True:
    pessoa["nome"] = str(input("Nome: ")).strip()
    pessoa["sexo"] = str(input("Sexo: ")).strip().lower()
    while pessoa["sexo"] not in "F M m f":
        pessoa["sexo"] = str(input("Informe um sexo valido [F/M]: ")).lower().strip()
    pessoa["idade"] = int(input("Idade: "))
    soma_idade += pessoa["idade"]
    listagem.append(pessoa.copy())
    continuar = str(input("Deseja continuar inserindo dados?[S/N]")).lower()
    while continuar not in "N S n s":
        continuar = str(input("Insira um valor valido! Deseja continuar? [S/N]")).strip().lower()
    if continuar in "N n NÃO nao NOA":
        break
    if continuar in "s S":
        pessoa.clear()
print(f"Total de cadastros: {len(listagem)}")
print(f"A media de idades é {soma_idade/len(listagem)}")
for p in listagem:
    if p["sexo"] == "f":
        print("--> [{:.^5}] é do sexo feminino".format(p['nome']))

for p in listagem:
    if p["idade"] > (soma_idade/len(listagem)):
        print(f'--> [{p["nome"]}] está acima da media de idade')
