import datetime
sexo = str(input("infome seu sexo, M para masculido e F para feminino")).strip().upper()
if sexo == "M":
    nascimento = int(input("Qual ano você nasceu? "))
    atual = datetime.datetime.today().year
    if atual-nascimento == 18:
        print("Você deve se alistar esse ano, {}".format(atual))
    elif atual-nascimento>18:
        print("você perdeu o ano de alistamento, ele deveria ter sido {} anos atras".format(atual-nascimento-18))
    elif atual-nascimento<18:
        print("seu ano de alistamento ainda não chegou, ele é em {}, ou daqui {} anos".format(nascimento+18, (atual-nascimento-18)*-1))
else:
    print("Mulheres não necessitam se alistar")