def cadastrar(cadastros):
    nomeEIdade = dict()
    listaIndividuo = list()
    while True:
        try:
            nomeEIdade.clear()
            nomeEIdade["Nome"] = str(input("Infome o nome: ")).strip()
            nomeEIdade["Idade"] = int(input("Informe a idade: "))

        except ValueError:
            print("\033[31mERRO: Informe um numero inteiro!\033[m")

        except KeyboardInterrupt:
            print("\033[31mERRO: O Usuario preferiu não informar a idade!\033[m")

        else:
            listaIndividuo.append(nomeEIdade.copy())
            cadastros.append(listaIndividuo[:])
            break
    print(cadastros)


def mostrarLista(lista):
    for pessoacadastrada in lista:
        for i, v in pessoacadastrada[0].items():
            print(f"[{i}] com [{v}]", end=" ")
        print()

