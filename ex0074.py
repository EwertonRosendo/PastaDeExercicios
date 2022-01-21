from random import randint
listagem = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
organizado = sorted(listagem)
print(listagem)
print(organizado)
print(f"o menor valor é {organizado[0]} e o maior valor é {organizado[-1]}")
#outro jeito de mostrar o menor e maior valor é:
#print(f"o menor valor é {min(listagem)} e o maior é {max(listagem)}")