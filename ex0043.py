from random import randint
import math
peso = float(input("informe seu peso: "))
altura = float(input("informe sua altura: "))
print("=-="*10)
print("Calculando IMC..\n"*randint(1, 5))
imc = peso/(math.pow(altura, 2))
if imc < 18.5:
    print("\033[31m Você está abaixo do peso, {:.2f}\033[m".format(imc))
elif 18.5 <= imc <25:
    print("\033[32mVocê está no peso ideal, {:.2f}\033[m".format(imc))
elif 25<= imc <30:
    print("\033[33mVocê está no sobrepeso, {:.2f}\033[m".format(imc))
elif 30<= imc <40:
    print("\033[31mVocê está na obesidade, {:.2f}\033[m".format(imc))
elif imc >40:
    print("\033[31mVocê está mórbido, {:.2f} \033[m".format(imc))

