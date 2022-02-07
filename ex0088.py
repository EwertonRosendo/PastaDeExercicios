from random import randint
import time
palpite = []
lista_de_palpites = []
c = 0
print("{}\nJOGA NA MEGA SENA\n{}".format("="*20, "="*20))
vezes = int(input("Quantos palpites você quer que seja sorteado? "))
numero_gerado = 0
print("{} SORTEANDO {} JOGOS {}".format("=-"*10, vezes, "=-"*10))
while True:
    numero_gerado = randint(0, 60)
    if numero_gerado not in palpite:
        palpite.append(numero_gerado)
    if len(palpite) == 6:
        lista_de_palpites.append(palpite[:])
        palpite.sort()
        palpite.clear()
        c += 1
    if c == vezes:
        break
for c in lista_de_palpites:
    time.sleep(1.5)
    print(f"SORTEANDO JOGO {lista_de_palpites.index(c)+1}: {c}")
print("{} BOA SORTE {}".format("=-"*10, "=-"*10))
