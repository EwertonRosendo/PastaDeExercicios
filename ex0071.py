qtd50 = 0
qtd20 = 0
qtd10 = 0
qtd1 = 0
novovalor = 0
continuar = ""
while True:
    while True:
        valor = int(input("Informe o valor a ser sacado: "))
        while valor > 50:
            qtd50 = valor // 50
            valor = valor - (50*qtd50)
            novovalor = (valor % 50)
        while valor > 20:
            qtd20 = valor // 20
            valor = valor - (20*qtd20)
            novovalor = (valor % 20)
        while valor > 10:
            qtd10 = valor // 10
            valor = valor - (10*qtd10)
            novovalor = (valor % 10)
        while valor > 1:
            qtd1 = valor // 1
            valor = valor - (1*qtd1)
            novovalor = valor % 1
        if novovalor == 0:
            break
    print(f"A quantidade de notas de 50 é {qtd50}")
    print(f"A quantidade de notas de 20 é {qtd20}")
    print(f"A quantidade de notas de 10 é {qtd10}")
    print(f"A quantidade de notas de 1 é {qtd1}")
    continuar = str(input("Quer continuar? [S/N]")).upper().strip()
    if continuar == "N":
        break
print("FIM")
