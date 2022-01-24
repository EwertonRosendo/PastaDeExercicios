palavras = ("aprender", "programar", "linguagem", "python",
            "python", "curso", "gratis", "estudar", "praticar",
            "trabalhar", "mercado", "programador", "futuro",)
for p in palavras:
    print("\nNa palavra {} temos".format(p), end=" ")
    for letra in p:
        if letra in "aeiou":
            print(f"{letra} ", end=" ")
