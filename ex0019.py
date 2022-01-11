import random

aluno1 = str(input("informe o nome do primeiro aluno: "))
aluno2 = str(input("informe o nome do segundo aluno: "))
aluno3 = str(input("informe o nome do terceiro aluno: "))
aluno4 = str(input("informe o nome do ultimo aluno: "))
print("o aluno escolhido para apagar o quadro é o {}".format(random.choice([aluno4, aluno3, aluno2, aluno1])))


