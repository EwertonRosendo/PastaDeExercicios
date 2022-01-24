valores = list()
for c in range(0, 5):
    valores.append(int(input("Informe um numero para a posição {}: ".format(c))))
    maior = max(valores)
print(f"O maior valor é {max(valores)} na posição ", end="")
for x, maior in enumerate(valores):
    if max(valores) == maior:
        print(x, end="..")
print(f"\nO menor valor é {min(valores)} na posição ", end="")
menor = min(valores)
for x, menor in enumerate(valores):
    if min(valores) == menor:
        print(x, end="..")
print("\nFIM")