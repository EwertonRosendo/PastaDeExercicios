n1 = float(input("infome a primeira nota"))
n2 = float(input("informe a segunda nota"))
n3 = float(input("informe a terceira nota"))
n4 = float(input("informe a quarta nota"))
if (n1+n2+n3+n4)/4 >= 6:
    print("Parabens, você foi aprovado")
else:
    print("infelizmente você foi reprovado")
print("-----fim-----")
print("parabens, você foi aprovado" if (n1+n2+n3+n4)/4>=6 else "desculpe, infelizmente você não obteve uma nota maior que 6")