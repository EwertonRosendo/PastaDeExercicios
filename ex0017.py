import math
oposto = float(input("informe o cateto oposto "))
adjacente = float(input("agora informe o cateto adjacente "))
hipotenusa = math.sqrt(((oposto**2)+(adjacente**2)))
print("a hipotenusa do triangulo retangulo de lados {} e {} é {}".format(oposto, adjacente, hipotenusa))
