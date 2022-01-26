valores = list()

while valores.count(0) != 1:
    valores.append(int(input("Informe um valor ou zero para sair: ")))

print(f" O total de numeros digitados foram {len(valores)}")
print(f"A lista informada é {valores}")
valores.sort(reverse=True)
print("Em ordem decrescente é: {}".format(valores))

if valores.count(5) != 0:
    print("O valor 5 aparece na lista")
else:
    print("O valor 5 não aparece na lista")
