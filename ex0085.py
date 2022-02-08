from random import randint
pares_e_impares = [[], []]
while True:
    num = int(input("Informe um numero: "))
    if num % 2 == 0:
        pares_e_impares[0].append(num)
    else:
        pares_e_impares[1].append(num)
    continuar = str(input("Deseja continuar? [S/N]")).strip().upper()
    if continuar in "NÃO NAO NOA NÕA":
        break
pares_e_impares[0].sort()
pares_e_impares[1].sort()
print(f"A lista de pares é: {pares_e_impares[0]}\nA lista de impares é:{pares_e_impares[1]}")
