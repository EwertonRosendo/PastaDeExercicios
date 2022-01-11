frase = "curso em video python"
frase2 = frase[9:13]
print(frase2)

print("a frase curso em video python usa {} microespaços da memoria".format(len(frase)))
print("a frase curso em video python usa a letra o {} vezes".format(frase.count("o")))
#print("curso em video python")
#print(frase.count("o")) --> informaria
#que são três letras na frase
print("o 'deo' começa na posição {} na frase curso em video python de um total de {} posições ".format(frase.find("deo"), len(frase)))
print("curso" in frase)
print(frase.replace("python", "android"))
print(frase.upper())
frase3 = "SEU NOIA ESTUDANTE"
print(frase3.lower())
print(frase.capitalize())
print(frase.title())
frase4 = "   aprenda python  "
print(len(frase4))
print(frase4.strip())
print(frase4.lstrip())
#dar uma estudada na função split
print(frase.split())
frase5 = frase.split()
print(" ".join(frase5))
