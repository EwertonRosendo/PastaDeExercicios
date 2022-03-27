import datetime

def voto(nascimento):
    if datetime.datetime.today().year - nascimento > 17:
        print("Você é obrigado a votar")

    elif datetime.datetime.today().year - nascimento < 16:
        print("Você não tem idade suficiente para votar")

    else:
        return "Você tem direito a voto opcional"

voto(int(input("Seu ano de nascimento? ")))
