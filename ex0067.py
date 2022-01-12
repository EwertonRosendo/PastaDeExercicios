n = 1
c = 1
f = "-"
print(f"{f*10}INICIO | DIGITE UM NUMERO NEGATIVO PARA SAIR{f*10}")
while True:
    n = int(input("Informe um valor para ver sua tabuada: "))
    c = 1
    if n > 0:
        while n*11 != n*c:
            print(f"{n}x{c}={n*c}")
            c += 1
    else:
        break
print("FIM")
