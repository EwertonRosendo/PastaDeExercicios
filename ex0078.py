valores = list()
for c in range(0, 5):
    valores.append(int(input("Informe um numero para a posição {}: ".format(c))))
    maior = max(valores)
print(f"O maior valor é {max(valores)} na posição ")
for x, maior in enumerate(valores):
    if max(valores) == maior:
        print(x)
