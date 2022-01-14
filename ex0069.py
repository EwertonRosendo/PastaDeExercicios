qtd18 = 0
qtdhomens = 0
qtdmulheres = 0
while True:
    # Validando a idade
    idade = int(input("Informe a idade: "))
    while idade < 0 or idade > 105:
        idade = int(input("Informe uma idade valida: "))
    # Validando o sexo
    sexo = str(input("Informe o sexo [M/F]: ")).strip().upper()
    while sexo not in "FMfm":
        sexo = str(input("Informe um sexo valido [F/M]: ")).strip().upper()
    # quantidade de pessoas maiores de 18 anos
    if idade > 18:
        qtd18 += 1
    # quantidade de homens
    elif sexo == "M":
        qtdhomens += 1
    # quantidade de mulheres com menos de 20 anos
    elif sexo == "F" and idade < 20:
        qtdmulheres += 1
    duvida = str(input("Quer continuar? [S/N]"))
    while duvida not in "SIM sim NAO nao NÃO n N S s":
        duvida = str(input("Insira um valor valido: "))
    if duvida in "nao não NÃO NAO N":
        break
print(f"{qtd18} pessoas da pesquisa tem mais de 18 anos")
print(f"{qtdhomens} homens foram cadastrados no aplicativo")
print(f"{qtdmulheres} mulheres com menos de 20 anos foram cadastradas")
