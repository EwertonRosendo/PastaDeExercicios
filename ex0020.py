'''import random
aluno1 = input("nome do primeiro aluno ")
aluno2 = input("nome do aluno dois ")
aluno3 = input("nome do terceiro aluno ")
aluno4 = input("nome do quarto aluno") '''
# salve rosendo que ta vendo os exerciocios, você não conseguiu entender a parte do [0,0,0,0]
import random

aluno1 = input("nome do primeiro aluno ")
aluno2 = input("nome do aluno dois ")
aluno3 = input("nome do terceiro aluno ")
aluno4 = input("nome do quarto aluno")
lista = [aluno4, aluno3, aluno2, aluno1]
ordem = random.choices(lista)
print("A ordem das apresentações será: {}".format(ordem))


