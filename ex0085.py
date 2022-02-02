from random import randint
num = []
lista_de_numeros_pares = []
lista_de_numeros_impares = []
lista_geral = []
for c in range(0, 7):
    # num.append(int(input("Informe um numero: ")))
    num = randint(0, 50)
    print("O numero sorteado foi: {}".format(num))
    if (num % 2) == 0:
        lista_de_numeros_pares.append(num)
    else:
        lista_de_numeros_impares.append(num)
lista_de_numeros_impares.sort()
lista_de_numeros_pares.sort()
lista_geral.append(lista_de_numeros_pares), lista_geral.append(lista_de_numeros_impares)
print(f"A lista de numeros organizados pares é: {lista_geral[0]}")
print(f"A Lista com numeros impares é : {lista_geral[1]}")
print(lista_geral)
