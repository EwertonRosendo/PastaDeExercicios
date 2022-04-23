def leiaInt(msg):
    validadorInteiro = False

    while True:
        global x
        try:
            x = int(input(msg))

        # except ValueError:
        # print("O valor do tipo inteiro não foi atendido!")

        except Exception as causa:
            print(f"O valor  não é do tipo inteiro, e foi retornado o erro {causa.__class__}")

        except KeyboardInterrupt:

            print("\n\033[31mO usuario interrompeu o processo!\033[m")
            x = 0
            validadorInteiro = True

        else:
            print(f"O valor {x} é do tipo inteiro")
            validadorInteiro = True

        finally:
            if validadorInteiro is True:
                break
    print("Numero inteiro digitado com sucesso!")
    return x


def leiaFoat(msg):
    global y
    global teste
    validadorReal = False

    while True:
        try:
            teste = (input(msg))
            y = float(teste.replace(",", "."))

            print(f"O valor de y é {y} ")

        except Exception as causa:
            print(f"A causa do erro foi {causa.__class__}")

        except KeyboardInterrupt:

            print("\n\033[31mO usuario interrompeu o processo!\033[m")
            y = 0
            validadorReal = True

        else:
            print("Executado com sucesso!")
            validadorReal = True
        finally:
            if validadorReal is True:
                break

    print("Numero real digitado com sucesso!")
    return y



print(f"O inteiro digitado foi {leiaInt('Digite um valor inteiro: ')} e o valor real digitado foi {leiaFoat('Digite um valor real: ')}")