# Criando uma lista vazia
valores = list()
# Inserindo os cinco valores da lista
for c in range(0, 5):
    valores.append(int(input("Informe um numero para a posição {}: ".format(c))))
# Analisando o maior valor
maior = max(valores)
print(f"O maior valor é {max(valores)} na posição ", end="")
# Pegando as posições em que se encontram os maiores valores
for x, maior in enumerate(valores):
    if max(valores) == maior:
        print(x, end="..")
print(f"\nO menor valor é {min(valores)} na posição ", end="")
# Analisando o menor valor
menor = min(valores)
# Pegando as posições em que se encontram os menores valores
for x, menor in enumerate(valores):
    if min(valores) == menor:
        print(x, end="..")
print("\nFIM")
