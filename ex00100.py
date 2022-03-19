numerosPares = []
numeros = list()
def sorteia():
    from time import sleep
    from random import randint
    for c in range(0, 5):
        numeros.append(randint(0, 100))
        sleep(1)
        print(f"Adicionando numeros: {numeros}")


sorteia()
def somaPar(* lstNumeros):
    for c in numeros:
        if c % 2 == 0:
            numerosPares.append(c)
    print(f"A soma de todos o numeros pares é {sum(numerosPares)}")


somaPar(numeros)