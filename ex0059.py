n1 = int(input("Informe um valor: "))
n2 = int(input("Informe outro valor: "))
x = 6
while x != 5:
    print("[1] Somar")
    print("[2] Multiplicar")
    print("[3] Maior")
    print("[4] Novos numeros")
    print("[5] Sair")
    x = int(input())
    if x == 1:
        print("A soma de {} e {} é {}".format(n1, n2, n1+n2))
    elif x == 2:
        print("{} x {} é {}".format(n1, n2, n1*n2))
    elif x == 3:
        if n1 > n2:
            print("{} é maior que {}".format(n1, n2))
        elif n1 == n2:
            print("{} e {} são iguais".format(n1, n2))
        else:
            print("{} é maior que {}".format(n2, n1))
    elif x == 4:
        n1 = int(input("Informe um novo valor: "))
        n2 = int(input("Informe um outro novo valor: "))
    else:
        print("Informe um valor valido ")
print("-----FIM-----")
