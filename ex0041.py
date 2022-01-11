idade = int(input("\033[31;40m Informe a idade: \033[m"))
if idade <=9:
    print("\033[36m Este jovem é da categoria mirim\033[m")
elif 9 < idade <= 14:
    print("\033[33m Este jovem é da categoria infantil\033[m")
elif 14 < idade <= 19:
    print("\033[31m Este marmanjo é da categoria junior \033[m")
elif idade == 20:
    print("Este corno é da categoria senior")
else:
    print("É DA CATEGORIA MASTER")

