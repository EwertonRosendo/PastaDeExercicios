soma = 0
for vezes in range(1, 7):
    num = int(input("Informe um numero"))
    if num % 2 == 0:
        soma += num
        print("O numero {} é par, por isso será somado aos outros numeros".format(num))
    else:
        print("O numero {} é impar, por isso não será somado".format(num))
print(soma)
