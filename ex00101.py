import datetime

def voto(nascimento):
    if datetime.datetime.today().year - nascimento > 17:
        return "Você é obrigado a votar"

    elif datetime.datetime.today().year - nascimento < 16:
        return "Você não tem idade suficiente para votar"

    else:
        return "Você tem direito a voto opcional"

print(voto(int(input("Seu ano de nascimento? "))))
