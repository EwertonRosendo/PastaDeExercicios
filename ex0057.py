''' sexo = "k"
while sexo != "M" and sexo != "F":
    print("=-="*7)
    print("Informe seu sexo, F para feminino, M para masculino")
    sexo = str(input()).upper()
    if sexo == "M".upper():
        print("Você escolheu o sexo masculino")
    elif sexo == "F".upper():
        print("Você escolheu o sexo feminino")
    else:
        print("Você escolheu uma opção invalida, tente novamente") '''
sexo = str(input("Informe seu sexo [M/F]")).strip().upper()[0]
while sexo not in "MmFf":
    sexo = str(input("Você informou um sexo errado! Informe novamente [M/F]!"))
    if sexo in "Mn":
        print("Você escolheu o sexo feminino")
    elif sexo in "fF":
        print("você escolheu o sexo feminino")
