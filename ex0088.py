from random import randint
palpite = []
lista_de_palpites = []
c = 0
vezes = int(input("Quantos palpites você deseja? "))
while True:
    palpite.append(randint(0, 60))
    if len(palpite) == 6:
        lista_de_palpites.append(palpite[:])
        palpite.clear()
        c += 1
    if c == vezes:
        break
print(lista_de_palpites)
