#Escolhendo entre PAR ou IMPAR
from random import randint
vitorias = 0
verde = "\033[32m"
vermelho = "\033[31m"
amarelo = "\033[33m"
fim = "\033[m"
while True:
    print("-"*30)
    escolha = int(input(f"{amarelo}Impar[1] ou Par[2]?{fim}"))
    # Validando a escolha entre PAR e IMPAR
    while escolha != 1 and escolha != 2:
        escolha = int(input(f"{amarelo}Porfavor, escolha [1] para IMPAR ou [2] para PAR: {fim}"))
    if escolha == 1:
        escolhapc = 2
    # Validando um numero entre 0 e 10
    pessoanum = int(input(f"{amarelo}Informe um numero numero entre 0 e 10: {fim}"))
    while pessoanum < 0 or pessoanum > 10:
        pessoanum = int(input(f"{amarelo}Porfavor, informe um numero entre 0 e 10: {fim}"))
    pcnum = randint(0, 10)
    # Validando a vitoria
    if ((pessoanum + pcnum) % 2) == 0 and escolha == 2:
        vitorias += 1
        print(f"{verde}Você escolheu Par e {pessoanum} + {pcnum} é {pessoanum+pcnum} que é PAR e você acertou{fim}")
    elif ((pessoanum + pcnum) % 2) != 0 and escolha == 1:
        vitorias += 1
        print(f"{verde}Você escolheu Impar e {pessoanum} + {pcnum} é {pessoanum+pcnum} que é IMPAR e você acertou{fim}")
    else:
        print(f"{vermelho}Você errou, {pessoanum} + {pcnum} = {pessoanum+pcnum}{fim}")
        break
print("\033[34mVocê fez um total de {} vitorias consecutivas contra o pc".format(vitorias))
