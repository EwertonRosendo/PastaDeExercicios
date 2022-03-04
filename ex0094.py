from time import sleep
pessoa = dict()
listagem = []
soma_idade = 0
while True:
    pessoa["nome"] = str(input("\033[33mNome: \033[m")).strip()
    print("\033[32mInformação Aceita\033[m")
    pessoa["sexo"] = str(input("\033[33mSexo[M/F]: \033[m")).strip().lower()
    while pessoa["sexo"] not in "F M m f":
        pessoa["sexo"] = str(input("\033[31mInforme um sexo valido [F/M]: \033[m")).lower().strip()
    print("\033[32mInformação Aceita\033[m")
    pessoa["idade"] = int(input("\033[33mIdade: \033[m"))
    print("\033[32mInformação Aceita\033[m")
    soma_idade += pessoa["idade"]
    listagem.append(pessoa.copy())
    continuar = str(input("\033[33mDeseja continuar inserindo dados?[S/N] \033[m")).lower()
    while continuar not in "N S n s":
        continuar = str(input("\033[31mInsira um valor valido! Deseja continuar?[S/N] \033[m")).strip().lower()
    if continuar in "N n NÃO nao NOA":
        break
    if continuar in "s S":
        pessoa.clear()
for c in range(0, 3):
    sleep(1)
    print("\033[31m Saindo..\033[m")
print(f"\033[33mTotal de cadastros: {len(listagem)}")
print(f"A media de idades é {soma_idade/len(listagem)}")
for p in listagem:
    sleep(1)
    if p["sexo"] == "f":
        print("--> [{:.^5}] é do sexo feminino".format(p['nome']))

for p in listagem:
    sleep(1)
    if p["idade"] > (soma_idade/len(listagem)):
        print(f'--> [{p["nome"]}] está acima da media de idade')
        sleep(1)
