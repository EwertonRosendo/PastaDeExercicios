''' import random
aluno1 = input("informe o primeiro aluno")
aluno2 = input("informe o segundo aluno")
aluno3 = input("informe o terceiro aluno")
aluno4 = input("informe o quarto aluno")
print("o aluno escolhido para apagar o quadro foi o {}".format(random.choice([aluno4, aluno3, aluno2, aluno1]))) '''
import random

aluno1 = input("informe o primeiro aluno")
aluno2 = input("informe o segundo aluno")
aluno3 = input("informe o terceiro aluno")
aluno4 = input("informe o quarto aluno")
lista = [aluno4, aluno3, aluno2, aluno1]
print("o aluno escolhido foi o {}".format(random.choice(lista)))
