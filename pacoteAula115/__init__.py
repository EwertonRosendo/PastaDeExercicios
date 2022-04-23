
def cadastrar(cadastros):
    nomeEIdade = dict()
    listaIndividuo = list()
    while True:
        try:
            nomeEIdade.clear()
            nomeEIdade["nome"] = str(input("Infome o nome: ")).strip()
            nomeEIdade["idade"] = int(input("Informe a idade: "))

        except ValueError:
            print("\033[31mERRO: Informe um numero inteiro!\033[m")

        except KeyboardInterrupt:
            print("\033[31mERRO: O Usuario preferiu não informar a idade!\033[m")

        else:
            listaIndividuo.append(nomeEIdade.copy())
            cadastros.append(listaIndividuo[:])
            break
    print(cadastros)


def mostrarLista(*lista):
    print(lista)