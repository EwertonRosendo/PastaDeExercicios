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


#  Criando a função de contar de 10 a 0

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


#  Criando função de contador
def contador(inicio, fim, passo):
    print("~"*30)
    print("CONTADOR PERSONALIZADO")
    
    #  FIM > inicio    
    if fim > inicio and passo > 0:
        for c in range(inicio, fim + 1, passo):
            print(c, end=" ")
            sleep(0.2)
        print()

    # Fim > inicio e passo == 0
    elif fim > inicio and passo == 0:
        for c in range(inicio, fim+1, 1):
            print(c, end=" ")
            sleep(0.2)
        print()

    #  Inicio > Fim e Passo > 0    
    elif inicio > fim and passo > 0:
        for c in range(inicio, fim-1, -1*passo):
            print(c, end=" ")
            sleep(0.2)
        print()

    #  Inicio > Fim e passo < 0
    elif inicio > fim and passo < 0:
        for c in range(inicio, fim-1, passo):    
            print(c, end=" ")
            sleep(0.2)
        print()

    # Inicio > Fim e passo == 0
    elif inicio > fim and passo == 0:
        for c in range(inicio, fim-1, -1):
            print(c, end=" ")
            sleep(0.2)
        print()
    print("~"*30)
#  Chamando contador personalizado
contador(inicio=int(input("Inicio: ")), fim=int(input("FIM: ")), passo=int(input("Passo: ")))
