while True:
    num = int(input("Informe o numero para descobrir sua tabuada: "))
    for c in range(1, 11):
        print(f"{num}x{c}={num*c}")
    continuar = str(input("Deseja continuar? [SIM/NÃO]")).strip().upper().replace(" ", "")
    if continuar in "NÃO não NÕA NAO":
        break
