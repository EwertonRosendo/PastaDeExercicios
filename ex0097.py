def escreva(txt):
    print("-"*len(txt))
    print(txt)
    print("-"*len(txt))

    
while True:
    escreva(str(input()))
    continuar = str(input("Continuar[S/N]")).upper
    while continuar not in "N S":
        continuar = str(input("Informe um valor valido! [S/N]")).upper
    if continuar in "N":
        break