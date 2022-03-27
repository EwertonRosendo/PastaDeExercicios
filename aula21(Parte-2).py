'''def contador(i, f, p):
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

contador(2, 10, 1)'''


def fatorial(num, rest = 1):
    '''
    -> Mostra o resultado do fatorial
    :param num: Numero desejado para descobrir seu fatorial
    :param rest: Resultado do fatorial
    '''
    for f in range(num, 0, -1):
        rest *= f
    return rest


r1 = fatorial(int(input("Informe um numero: ")))
r2 = fatorial(int(input("Informe um numero: ")))
r3 = fatorial(int(input("Informe um numero: ")))

print(f"Os resultados dos fatoriais foram {r1}, {r2}, {r3}")
