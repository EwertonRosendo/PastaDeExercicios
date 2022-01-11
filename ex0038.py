n1 = int(input("informe um numero "))
n2 = int(input("informe outro numero "))
if n1>n2:
    print(" {} é maior que {}".format(n1, n2))
elif n2>n1:
    print("{} é maior que {}".format(n2, n1))
elif n1 == n2:
    print("não existe numero maior, {} e {} são iguais".format(n1, n2))
    