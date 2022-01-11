soma = 0
maior = 0
MaisVelho = ""
maior20 = 0
for c in range(1, 5):
    nome = str(input("Infome seu nome: ")).strip().upper()
    idade = int(input("Informe sua idade: "))
    sexo = str(input("Informe F para sexo feminino e M para sexo masculino: ")).upper()
    soma += idade
    if sexo == "M" and idade > maior:
        maior = idade
        MaisVelho = nome
    elif sexo == "F" and idade < 20:
        maior20 = maior20 + 1
print("O cara mais velho é {}, com {} anos".format(MaisVelho, maior))
print("No total temos {} meninas com mais de 20 anos".format(maior20))
print("A media das idades do grupo é de {}".format(soma/4))


