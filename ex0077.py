palavras = ("aprender", "programar", "linguagem", "python", "python", "curso", "gratis", "estudar", "praticar", "trabalhar", "mercado", "programador", "futuro",)
c = 0
a = "a"
e = "e"
i = "i"
o = "o"
u = "u"
while len(palavras) != c:
    print("Na palavra {} temos ".format(palavras[c]).lower(), end=" ")
    if a in palavras[c]:
        print("a", end=" ")
    if e in palavras[c]:
        print("e", end=" ")
    if i in palavras[c]:
        print("i", end=" ")
    if o in palavras[c]:
        print("o", end=" ")
    if u in palavras[c]:
        print("u", end=" ")
    print("\n")
    c += 1

