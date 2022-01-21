tabela = ("atletico-MG", "flamengo", "palmeiras", "ortaleza", "corinthians",
          "bragantino", "fluminense", "america-mg", "atletico-go", "santos",
          "ceara", "internacional", "são paulo", "atletico-pr", "cuiaba",
          "juventude", "gremio", "bahia", "sport", "chapecoence")

print("os cinco primeiros são: ", tabela[0:6])
print("os quatro ultimos são: ", tabela[16:])
print("a tabela organizada é: ", sorted(tabela))
print("a posição da chapecoence é {}a posição".format(tabela.index("chapecoence")+1))
