def contador(i, f, p):
    """"
    -> Faz uma contagem e mostra na tela
    :param i: Inicio da contagem
    :param f: Fim da contagem
    :param p: Passo da contagem
    >return : Sem retorno 
    """
    for c in range(i, f, p):
        print(c)

help(contador)

contador(2, 10, 1)