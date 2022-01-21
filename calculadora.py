import math
traco = "-"
c = 0
# Laço infinito
while True:
    while c != 1:
        print(f"{traco*20}INICIO {traco*20}")
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
        if c == 2:
            print("[1] Função afim")
            print("[2] Função do segundo grau")
            print("[2] Função exponencial")
            c = int(input())
        # Progressão aritmetica

        if c == 3:
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
                    