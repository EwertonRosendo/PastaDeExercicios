velo = float(input("informe a velocidade do carro: "))
if velo > 80:
    print("Você ultrapassou o limite de velocidade e será multado")
    print("o valor da multa é de exatos {:.2f}".format((velo-80)*7))
else:
    print("Você não ultrapassou o limite de velocidade, portanto, não será multado!")
print("-----------------FIM DO PROGRAMA------------------")