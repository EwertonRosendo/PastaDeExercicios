lado1 = float(input("Informe o primeiro lado do triangulo: "))
lado2 = float(input("Informe o segundo lado do triangulo: "))
lado3 = float(input("Informe o terceiro lado do triangulo: "))
if lado3 > lado2-lado1 and lado2 > lado3-lado1 and lado1 > lado3 - lado2:
    print("\033[32mAs medidas {}, {}, {} podem ser lados de um triangulo!".format(lado2, lado3, lado1))
    if lado3 == lado2 == lado1:
        print("Essas medidas formam um triangulo equilatero! Todos os lados iguais!")
    elif lado1 == lado2 or lado1 == lado3 or lado3 == lado2:
        print("Essas medidas formam um triangulo isosceles! Dois lados iguais!")
    else:
        print("Todos os lados são triangulos escalenos! Todos os lados diferentes!")
else:
    print("\033[31mAs medidas citadas não podem formar um triangulo")
