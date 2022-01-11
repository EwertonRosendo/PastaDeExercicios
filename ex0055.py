maior = float(input("informe um peso: "))
menor = maior
for c in range(1, 5):
    peso = float(input("Informe um peso: "))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print("O maior peso foi de {}".format(maior))
print("O menor peso foi de {}".format(menor))
