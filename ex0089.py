from random import choice, randint
lista_de_alunos = []
aluno_e_nota = []
c = 0
n = 0
nomes = ("Mel", "Nina", "Paçoca", "Luna", "Amora", "Flora", "Belinha", "Cacau", "Pandora", "Frida", "Kiara", "Maya")
while len(lista_de_alunos) != 6:
    aluno_e_nota.append(c)
    #  aluno_e_nota.append(str(input("Nome: ")))
    aluno_e_nota.append(choice(nomes))
    #  aluno_e_nota.append(int(input("Nota 1: ")))
    aluno_e_nota.append(randint(0, 10))
    #  aluno_e_nota.append(int(input("Nota 2:")))
    aluno_e_nota.append(randint(0, 10))
    lista_de_alunos.append(aluno_e_nota[:])
    aluno_e_nota.clear()
    #continuar = str(input("Quer continuar? [S/N]"))
    #  if continuar in "NAO N NÃO NOA NÕA":
        #  break
    c += 1
print(lista_de_alunos)
print(f"No. NOME           MEDIA")
for p in lista_de_alunos:
    print(f"{p[0]} {p[1]}-----------------{(p[2]+p[3])/2}")
print(lista_de_alunos)
while n != 999:
    n = int(input("Qual aluno você quer ver individualmente(999 interrompe): "))
    print(f"As notas de {lista_de_alunos[n][1]} são {lista_de_alunos[n][2]} e {lista_de_alunos[n][3]}")
