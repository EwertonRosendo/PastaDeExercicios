def fatorial(numero=1, show=bool):
    resul = 1
    if show == True:
        for c in range(numero, 0, -1):
            if c != 1:
                resul *= c
                print(f"{c}x", end="")
            elif c == 1:
                print(f"{c}", end="")
        print(f" = {resul}")
    else:
        for c in range(numero, 0, -1):
            resul *= c
        print(f"O fatorial de {numero} é {resul}")


fatorial(4, False)
