def maior(* lista):
    for c in lista:
        if lista.index(c) == 0:
            maior_num = lista[c]
        elif lista[c] > maior_num:
            maior_num = lista[c]
    print(f"O maior numero da lista é {maior_num}")


while True:
    lista_de_numeros = list()
    lista_de_numeros.append(int(input("Informe um numero: ")))
    continuar = str(input("Deseja continuar? [S/N]"))
    if continuar in "N NAO NÃO":
        break