pessoa_e_peso = []
listagem = []
maior = 0
menor = 0
while True:
    pessoa_e_peso.append(str(input("Informe o nome: ")))
    pessoa_e_peso.append(float(input("Informe o peso: ")))
    listagem.append(pessoa_e_peso[:])
    pessoa_e_peso.clear()
    continuar = str(input("Deseja continuar? [S/N]")).strip().upper()
    if continuar in "NAO NÃO N NOA NÕA":
        break
for c in listagem:
    if maior == 0 and menor == 0:
        maior = c[1]
        menor = c[1]
    elif c[1] > maior:
        maior = c[1]
    elif c[1] < menor:
        menor = c[1]
print(f"O maior peso detectado foi {maior}")
print(f"O menor peso detectado foi {menor}")
print("O maior peso foi {} das pessoas: ".format(maior), end="")
for p in listagem:
    if p[1] == maior:
        print(f"[ {p[0]} ]", end=" ")
print("\nO maior peso foi {} das pessoas: ".format(menor), end="")
for p in listagem:
    if p[1] == menor:
        print(f"[ {p[0]} ]", end=" ")
print("A listagem geral foi {}".format(listagem))
print("E o total de cadastros foram {}".format(len(listagem)))
