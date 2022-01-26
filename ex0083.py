expressao = list()
expressao.append(str(input("Informe uma expressão: ")))
lado1 = expressao[0].count("(")
lado2 = expressao[0].count(")")
if lado1 == lado2:
    print("A expressão é valida")
else:
    print("A expressão é invalida")