from random import randint
soma = 0
num = int(input("Informe um numero de 0 a 10: "))
pcnum = randint(0, 10)
soma += 1
# Caso acerte de primeira o numero pensado pelo pc
if num == pcnum:
    print("===========Inicio===========")
    print("você acertou o numero")
# Caso erre o numero pensado pelo pc
while num != pcnum:
    print("===========Inicio===========")
    num = int(input("Você errou, tente novamente. \nInforme um numero de 0 a 10: "))
    pcnum = randint(0, 10)
    soma = soma + 1
    if 0 <= num <= 10 and num != pcnum:
        print("Você errou o numero pensado pelo pc")
        print("O pc pensou em {} e você digitou {}".format(pcnum, num))
        print("===========FIM===========")
    # Caso de numero invalido
    elif num > 10 or num < 0:
        print("Numero invalido!")
        print("===========FIM===========")
    else:
        print("Você acertou, o pc pensou em {} e você digitou {}".format(pcnum, num))
        print("===========FIM===========")
        print("Foram feitas {} tentativas!".format(soma))
