valores = list()
for c in range(0, 5):
    valores.append(int(input("Informe um numero: ")))
print(f"O maior valor foi {max(valores)} e sua posição é {valores.index(max(valores))+1}")
print(f"O menor valor foi {min(valores)} e sua posição é {valores.index(min(valores))+1}")
