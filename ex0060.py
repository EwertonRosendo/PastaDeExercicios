import math
num = int(input("Informe um numero: "))
x = num
while num != 0:
    fac = math.factorial(num)
    print("O fatorial de {} é {}".format(num, fac))
    while x != 0:
        if x != 1:
            print("{}".format(x), end="x")
            x = x - 1
        # print(x, end="x")
        #x = x - 1
        elif x == 1:
            print(x)
            x = x - 1

    num = int(input(" \nInforme um novo numero: "))
print("FIM")
