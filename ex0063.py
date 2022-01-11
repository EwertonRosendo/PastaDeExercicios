n = int(input("Quantos numeros da sequencia de fibbonaci você deseja ver: "))
x = 0
n1 = 0
n2 = 1
while x != n/2 :
    print("{}, {} ".format(n1, n2), end=", ")
    # 0 , 1 , 1, 2, 3, 5
    n1 = n1 + n2
    n2 = n2 + n1
    x = x + 1

