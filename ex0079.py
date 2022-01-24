valoresdalista = list()
while True:
    valores = int(input("Informe um numero: "))
    if valoresdalista.count(valores) == 1:
        print("O Valor já existe na lista")
    else:
        valoresdalista.append(valores)
    continuar = str(input("Deseja continuar? [S/N]")).upper()
    if continuar in "NÃO NAO N NOA NÕA":
        break
valoresdalista.sort()
for c in valoresdalista:
    print(c, end="..")
print("\nFIM")
