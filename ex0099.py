#  Definindo  a função para descobrir o maior numero


def maior(listagem):
    for c in listagem:
        if listagem.index(c) == 0:
            maior_num = c
        elif c > maior_num:
            maior_num = c
    print(f"O maior numero é {maior_num}")

#  Criando a lista que será usada como parametro


listaDeNumeros = []


#  Laço infinito para adicionar numeros a lista


while True:
    listaDeNumeros.append(int(input("Informe um numero: ")))
    continuar = str(input("Deseja continuar? [S/N] ")).strip().upper()
    while continuar not in "S N NAO SIM NÃO":
        continuar = str(input("Informe um valor valido, CONTINUAR OU NÃO [S/N] ")).strip().upper()
    if continuar in "N NÃO NAO":
        break


#  Chamando a função maior 
maior(listaDeNumeros)
