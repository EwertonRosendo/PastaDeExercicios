import datetime
pessoa = {
    "nome": str(input("Nome: ")).strip(),
    "idade": (datetime.datetime.now().year - int(input("Ano de nascimento: "))),
    "carteira_tb": int(input("Numero da carteira(0 não tem): "))
}
if pessoa["carteira_tb"] != 0:
    pessoa["ano_de_contratação"] = int(input("Ano de contratação: "))
    pessoa["salario"] = float(input("Salario: "))
    pessoa["ano_de_aposentar"] = pessoa["ano_de_contratação"]+35
    pessoa["idade_aposentar"] = (pessoa["ano_de_contratação"] + 35) - (pessoa["ano_de_contratação"]- pessoa["idade"])
print(pessoa["idade_aposentar"])