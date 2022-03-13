#  Inicio do codigo
from time import sleep # Importando o contador de segundos
#  Criado a função de contar ate 10

def contar_ate_10():
    print("~"*30)
    print("CONTADOR DE 0 A 10: ")
    for c in range(1, 11):
        print(c, end=" ")
        sleep(0.2)
    print()
    print("~"*30)

#  Chamando a função de 1 a 10
contar_ate_10()


#Criando a função de contar de 10 a 0

def contar_ate_0():
    print("~"*30)
    print("CONTADOR DE 10 A 0 DE DOIS EM DOIS")
    for c in range(10, -1, -2):
        print(c, end=" ")
        sleep(0.2)
    print()
    print("~"*30)


#  Chamando a função de 10 a 0 de dois em dois
contar_ate_0()
