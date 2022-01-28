x = 0
valores = list()
for c in range(0, 5):
    x = int(input("Informe um numero: "))
    # Primeiro valor
    if c == 0:
        valores.append(x)
    # Novo maior valor
    elif x > max(valores):
        valores.append(x)
    # Novo menor valor
    elif x < min(valores):
        valores.insert(0, x)
    elif x > valores[0]:
        valores.insert(1, x)
    elif x < valores[4]:
        valores.insert(3, x)
print(valores)
print(max(valores))
print(min(valores))
