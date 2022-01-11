import datetime
maior = 0
menor = 0
nesseano = 0
for c in range(1, 8):
    nascimento = int(input("Infome seu ano de nascimento: "))
    if datetime.datetime.today().year - nascimento > 18:
        print("-"*20)
        print("voce é de maior")
        print("-"*20)
        maior = maior + 1
    elif datetime.datetime.today().year - nascimento == 18:
        print("Ou você já fez 18 anos e é de maior, ou entrará na maior idade ainda em {}".format(datetime.datetime.today().year))
        print("-"*20)
        nesseano = nesseano + 1
    else:
        print("Você ainda é de menor")
        print("-"*20)
        menor = menor + 1
print("{} são maiores de idade,\n{} fazem 18 esse ano\n{} são menores de idade".format(maior, nesseano, menor))
