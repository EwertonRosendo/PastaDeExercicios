from datetime import date


def voto(nascimento):
    import datetime
    if (datetime.datetime.today().year - nascimento) == 16 or (nascimento - datetime.datetime.today().year) == 17:
        print("Você tem voto opcional")

    elif (datetime.datetime.today().year - nascimento < 16):
        print("Você não tem nascimento suficiente para votar")
    
    elif (datetime.datetime.today().year - nascimento > 17):
        print("Você é obrigado a votar")

voto(int(input("Qual ano você nasceu? ")))
