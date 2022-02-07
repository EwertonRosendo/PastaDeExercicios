n = []
matriz = []
linha = 1
coluna = 1
for c in range(0, 9):
    n.append(int(input(f"Informeu numero para a poseção {linha}, {coluna}")))
    matriz.append(n[:])
    n.clear()
    coluna += 1
    if len(matriz) == 3:
        linha = 2
        coluna = 1
    elif len(matriz) == 6:
        linha = 3
        coluna = 1
for num in matriz:
    print(num, end=" ")
    if matriz.index(num) == 2 or matriz.index(num) == 5:
        print(end="\n")