continuar = str("")
npar = 0
while True:
    tupla = (int(input("Informe o primeiro numero: ")),
             int(input("Informe o segundo numero: ")),
             int(input("Informe o terceiro numero: ")),
             int(input("Informe o quarto numero: ")))
    #tupla = int(input((n1, n2, n3, n4))
    print(f"A tupla com os numeros escolhidos é: {tupla}")
    print(f"O numero 9 aparece {tupla.count(9)} vezes")
    print(f"O numero 3 aparece na posição {tupla.index(3)+1}")
    for pares in tupla:
        if pares%2 == 0:
            npar += 1
    continuar = str(input("Deseja continuar?")).upper()
    if continuar in "NÃO NAO N NOA":
        break
print(f"A quantidade de numeros pares é {npar}")
