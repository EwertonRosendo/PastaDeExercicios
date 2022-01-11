from random import shuffle
n1 = input("informe o nome do primeiro aluno")
n2 = input("informe o nome do segundo aluno")
n3 = input("informe o nome do terceiro aluno")
n4 = input("informe o nome do quarto aluno")

lista = [n1, n2, n3, n4]
shuffle(lista)
print("a ordem da apresnetção será {} ", end=" ")
print(lista)


