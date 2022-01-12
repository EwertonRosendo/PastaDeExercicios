num = 0
soma = 0
qtdn = 0
print("Para parar digite 999")
while True:
    num = int(input("Informe um numero: "))
    if num == 999:
        break
    soma += num
    qtdn += 1
print(f"Você digitou {qtdn} numeros, e a soma entre eles é de {soma}!")