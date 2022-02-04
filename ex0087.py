numeros = []
matriz = []
coluna = 1
linha = 1
cont = -1
soma_de_pares = 0
soma_terceira_coluna = 0
maior_valor_linha2 = []
while True:
    numeros.append(int(input("Informe um valor para a posição {}, {}: ".format(linha, coluna))))
    matriz.append(numeros[:])
    if linha == 2:
        maior_valor_linha2.append(numeros[:])
    coluna += 1
    numeros.clear()
    print(len(matriz))
    if coluna == 4:
        linha += 1
        coluna -= 3
    if len(matriz) == 9:
        break
print(matriz)
for c in range(0, 9):
    print(matriz[c], end=" ")
    if c == 2 or c == 5:
        print()
    if matriz[c][0] % 2 == 0:
        #print(f"O numero {matriz[c][0]} é par")
        soma_de_pares += matriz[c][0]
    if (matriz[c][0].__index__()) % 3 == 0:
        soma_terceira_coluna += matriz[c][0]
print(f"\nA soma de todos os numeros pares citados na matriz é {soma_de_pares}")
print(f"A soma de todos os valores da terceira coluna é: {soma_terceira_coluna} ")
print(f"O maior valor da segunda linha é {max(maior_valor_linha2)}")
