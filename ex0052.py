soma = 1
#divisores = 0
num = int(input("Informe um numero"))
for c in range(1, num):
    if num % c == 0:
        soma = soma + 1
if soma != 2 :
     print("\033[31mo numero {} não é primo ".format(num))
     print("O numero {} é divisivel por {} numeros".format(num, soma))
else:
     print("\033[32mo numero {} é primo, e tem {} divisores ".format(num, soma))
