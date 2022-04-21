

def leiaInt(msg):
    validadorInteiro = False

    while True:
        try:
            x = int(input(msg))

        # except ValueError:
        # print("O valor do tipo inteiro não foi atendido!")

        except Exception as causa:
            print(f"O valor  não é do tipo inteiro, e foi retornado o erro {causa.__class__}")

        except KeyboardInterrupt:
            print("\nO usuario interrompeu o processo!")
            validadorInteiro = True

        else:
            print(f"O valor {x} é do tipo inteiro")
            validadorInteiro = True

        finally:
            if validadorInteiro is True:
                break
        print("VALEU VALEU")

def leiaFoat(msg):

    validadorReal = False

    while True:
        try:
            x = float(input(msg))

        except Exception as causa:
            print(f"A causa do erro foi {causa.__class__}")

        else:
            print("Executado com sucesso!")
            validadorReal = True


        finally:
            if validadorReal is True:
                break
        print("Fim do programa!")




leiaInt("Digite um valor inteiro: ")

leiaFoat("Digite um valor real: ")