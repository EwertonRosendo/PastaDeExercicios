import random
n = random.randint(0, 5)
resul = int(input("Tente adivinhar um numero entre 0 e 5"))
if n == resul:
    print("PARABENS, você acertou, o numero era realmente {}".format(resul))
else:
    print("f noia, infelizmente você errou, o numero era {}".format(n))
print("----------FIM----------")
