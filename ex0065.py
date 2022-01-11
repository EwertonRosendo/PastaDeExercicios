maior = 0
menor = 0
soma = 0
num = 0
qtdnum = num
duvida = "nada"
print("--------------------INICIO--------------------")
while duvida not in "nao NAO não noa nõa NÃO ":
    duvida = str(input("Quer continuar inserindo valores? [SIM/NÃO]")).strip().replace(" ", "").upper()
    if duvida not in "nao NAO não noa NÃO nõa":
        num = int(input("Informe um numero: "))
        qtdnum = qtdnum + 1
        soma += num
        if maior == 0 and menor == 0:
            maior = num
            menor = num
        elif num > maior:
            maior = num
        elif num < menor:
            menor = num
print("A Media entre todos os valores é de {}".format(soma/qtdnum))
print("O maior valor é {}, já o menor valor é {}".format(maior, menor))
print("--------------------FIM--------------------")
