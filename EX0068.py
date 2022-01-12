import random
print("{}{}{}".format("-"*10, "INICIO", "-"*10))
duvida = str(input("Deseja par ou impar? [PAR/IMPAR]")).upper().strip()
numpc = 0
num = -1
numdeacertos = 0
while duvida not in "PAR IMPAR":
    duvida = str(input("Informe se você deseja par ou impar, por favor[PAR/IMPAR]")).upper().strip()
    if duvida == "PAR":
        duvidapc = "IMPAR"
    else:
        duvidapc = "PAR"
    num = int(input("Informe um numero entre 0 e 10: "))
    if 0 > num > 10:
        num = int(input("Insira um numero valido entre 0 e 10: "))
    else:
        numpc = random.randint(0, 10)
        if ((num + numpc) % 2) == 0 and duvida == "PAR":
            print("\033[33mVocê acertou\033[m")
            numdeacertos += 1
        elif ((num + numpc) % 2) != 0 and duvida == "IMPAR":
            print("\033[33mVocê acertou\033[m")
            numdeacertos += 1
        else:
            print("\033[31mVocê errou")
            break
print(f"Você ganhou da maquina {numdeacertos} vezes")



