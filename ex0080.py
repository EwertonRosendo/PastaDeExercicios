valores = list()
zero = 0
um = 1
antigo = 0
for c in range (0, 5):
    valores.append(int(input("Informe o valor {}: ".format(c))))
while True:
    if valores[0] > min(valores):
        valores[0] = min(valores)
        valores[len(valores.index(min(valores)))] = valores[0]
    else:
        break
print(valores)