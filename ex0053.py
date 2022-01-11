frase = str(input("frase: ")).strip()
if frase.replace(" ", "").upper() == frase[::-1].replace(" ", "").upper():
    print("A frase: {}, é um palindromo".format(frase))
else:
    print("A frase {}, não é um palindromo".format(frase))
