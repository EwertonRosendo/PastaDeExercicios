nome = input("informe um nome completo").strip( )
num = int(len(nome.split()))
print(num)
print("o primeiro nome da pessoa é {}".format(nome.split()[0]))
print("o ultimo nome da pessoa é {}".format(nome.split()[num-1]))


