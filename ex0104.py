'''
def leiaInt(msg):
    valor = 0
    ok = False
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print("\033[31mVocê não digitou um valor numerico\033[m")
        if ok:
            break
    return valor



n = leiaInt("Digite um numero: ")
print(f"Você digitou {n}")
'''
def leiaInt(num):
    n = str(num)
    if n.isnumeric():
        return "É UM VALOR NUMERICO"
    else:
        return "NÃO É UM VALOR NUMERICO"

print(leiaInt(input("Digite um numero: ")))

