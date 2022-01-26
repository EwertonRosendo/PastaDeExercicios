valores = list()
pares = list()
impares = list()
while True:
    valores.append(int(input("Informe um numero: ")))
    continuar = str(input("Deseja continuar[S/N]? ")).strip().upper()
    if continuar in "NAO NOA NO NÃO N ":
        break
for c in valores:
    if c % 2 == 0:
        pares.append(c)
    else:
        impares.append(c)
print(f"A lista de valores é {valores}")
print(f"Os valores pares digitados foram {pares}")
print(f"Os valores impares digitados foram {impares}")
