escolha = 9
while escolha > 3 or escolha < 0:
    print("1- Beber")
    print("2- Comer")
    print("3- Jogar")
    print("0- Sair")
    escolha = int(input())
    if escolha == 1:
        print("Você escolheu a bebida")
    elif escolha == 2:
        print("Você escolheu comer")
    elif escolha == 3:
        print("Você escolheu jogar")
    elif escolha == 0:
        print("Você escolheu sair")
    else:
        print("Por Favor, escolha uma opção valida!")
#else:
    #while escolha > 3 or escolha < 0:
      #  print("1- Beber")
       # print("3- Jogar")
       # print("0- Sair")
       # escolha = int(input())