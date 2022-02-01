nome_peso = []
pessoas = []
qtd_pessoas = 0
soma = 0
while True:
    nome_peso.append(str(input("Infome o nome"))), nome_peso.append(int(input("Informe o peso ")))
    soma += nome_peso[1]
    pessoas.append(nome_peso[:])
    nome_peso.clear()
    qtd_pessoas += 1
    duvida = str(input("Deseja continuar?[S/N]")).upper()
    if duvida in "NAO NÃO NOA NOÃ N":
        break
    else:
        print("----------NOVAMENTE------------")
print(pessoas)
for p in pessoas:
    print("PESOS MAIORES QUE A MEDIA - ")
    if p[1] > (soma/qtd_pessoas):
        print("Pessoa {} com peso {}".format(p[0], p[1]))
            
    elif p[1] < (soma/qtd_pessoas):
        print(" Pessoa {} com peso {}".format(p[0], p[1]))
