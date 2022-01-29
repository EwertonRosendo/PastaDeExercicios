import math
traco = "-"*20
c = 0
# Laço infinito
while True:

    print(f"{traco}INICIO {traco}")
    print("[1] Operações basicas")
    print("[2] Funções")
    print("[3] Progressão")
    print("[4] Sair")
    # outras operações
    c = int(input())
    # condições
    if c == 1:
        while True:
            print("[1] Multiplicar")
            print("[2] Dividir")
            print("[3] Somar")
            print("[4] Subtrair")
            print("[5] Sair")
            c = int(input())
            if c == 1:
                valores = (float(input("Informe o primeiro valor: ")), float(input("Informe o segundo valor: ")))
                print(f"O resultado de {valores[0]}x{valores[1]} é {valores[0]*valores[1]} ")

            elif c == 2:
                valores = (float(input("Informe o primeiro valor: ")), float(input("informe o segundo valor: ")))
                print(f"A divisão de {valores[0]} por {valores[1]} é {valores[0]/valores[1]}")

            elif c == 3:
                valores = (float(input("Informe o primeiro valor: ")), float(input("Informe o segundo valor: ")))
                print(f"A soma de {valores[0]}+{valores[1]} é {valores[0]+valores[1]}")

            elif c == 4:
                valores = (float(input("Informe o primeiro valor: ")), float(input("Informe o segundo valor: ")))
                print(f"A diferença entre {valores[0]} e {valores[1]} é {valores[0]-valores[1]}")

            elif c == 5:
                break

            else:
                print("Insira um valor valido entre 1 e 5")
    elif c == 2:
        while True:
            print("[1] Função afim")
            print("[2] Função do segundo grau")
            print("[3] Função exponencial")
            print("[4] Sair")
            c = int(input())

            if c == 1:
                # Função afim
                print("O que você deseja saber da função afim?")
                print("[1] Saber o Y\n[2] Saber o X\n[3] Saber o coeficiente angular\n[4] Saber o coeficiente Linear")
                c = int(input())
                if c == 1:
                    funafim = [int(input("Informe X: ")), int(input("Informe o coeficiente angular")), int(input("Informe o coeficiente linear: "))]
                    y = ((funafim[0]*funafim[1]) + funafim[2])
                    print("O valor de Y é {}".format(y))
                elif c == 2:
                    funafim = [int(input("Informe o Y: ")), int(input("Informe o coeficiente angular: ")), int(input("Informe o coeficiente linear: "))]
                    # f(x) = ax + b
                    x = ((funafim[0] - funafim[2]) / funafim[1])
                    print("O Valor de x é {}".format(x))
                elif c == 3:
                    funafim = [int(input("Informe o Y: ")), int(input("Informe o X: ")), int(input("Informe o coeficiente linear: "))]
                    coeficienteangular = ((funafim[0] - funafim[2]) / funafim[1])
                    print("O valor do coeficiente angular é: {}".format(coeficienteangular))
                elif c == 4:
                    funafim = [int(input("Informe o Y: ")), int(input("Informe o X: ")), int(input("Informe o coeficiente angular: "))]
                    coeficientelinear = (funafim[0] / (- funafim[1]*funafim[2]))
                    print(f"O valor do coeficiente linear é: {coeficientelinear}")

            elif c == 2:
                # Função do Segundo Grau
                funsegun = [int(input("Informe o A: ")), int(input("Informe o B: ")), int(input("Informe o C: "))]
                delta = pow((pow(funsegun[1], 2) - (4*funsegun[0]*funsegun[2])), 1/2)
                print(f"O valor do delta é {delta}")
                duasraizes = (((-funsegun[1] + delta) / (2*funsegun[0])), ((-funsegun[1] - delta) / (2*funsegun[0])))
                print(f"O valor de x1 é {duasraizes[0]}\nO valor de x2 é {duasraizes[1]}")
            elif c == 3:
                # Função exponencial
                funafimexpo = []
                print("Novidades em breve")
                break
            elif c == 4:
                break
    # Progressão aritmetica

    elif c == 3:
        while True:
            print("[1] Progressão Aritmetica")
            print("[2] Progressão Geometrica")
            print("[3] Sair")
            c = int(input())
            if c == 1:
                print("O que você deseja saber? ")
                print("[1] Primeiro termo? [2] razão? [3] termo especifico? [4] numero de termos?")
                c = int(input())
                if c == 1:
                    termo = int(input("Informe o termo: "))
                    ntermo = int(input("Informe o numero desse termo: "))
                    razao = int(input("Informe a razão da PA: "))
                    primeirotermo = ((ntermo-1)*razao-termo)*-1
                    print("O primeiro termo é {}".format(primeirotermo))
            #elif c == 2:
            elif c == 3:
                break
    elif c == 4:
        break
print(f"{traco}FIM{traco}")