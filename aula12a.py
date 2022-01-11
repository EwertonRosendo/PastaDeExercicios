nome = str(input("qual é o seu nome? ")).strip()
if nome == "gustavo":
    print("que nome lindo, bom dia, {}".format(nome))
elif nome == "ewerton" or nome == "rosendo":
    print("que nome bonito cara, {}".format(nome))
elif nome in "ana, julia, jessica":
    print("que belo nome feminino,{}".format(nome))
else:
    print("que nome normal, bom dia {}".format(nome))