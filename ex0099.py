from time import sleep


def maior(listagem):
    for c in listagem:
        if listagem.index(c) == 0:
            maior_num = c
        elif c > maior_num:
            maior_num = c
    print(f"O maior numero é {maior_num}")

    
listaDeNumeros = []
while True:
    listaDeNumeros.append(int(input("Informe um numero: ")))
    continuar = str(input("Deseja continuar? [S/N] ")).strip().upper()
    while continuar not in "S N NAO SIM NÃO":
        continuar = str(input("Informe um valor valido, CONTINUAR OU NÃO [S/N] ")).strip().upper()
    if continuar in "N NÃO NAO":
        break
maior(listaDeNumeros)
