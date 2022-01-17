tabela = ("atletico-MG", "flamengo", "palmeiras", "ortaleza", "corinthians", "bragantino", "fluminense", "america-mg", "atletico-go", "santos")
tabela2 = ("ceara", "internacional", "são paulo", "atletico-pr", "cuiaba", "juventude", "gremio", "bahia", "sport", "chapecoence")
tabelageral = tabela+tabela2
print("os cinco primeiros são: ", tabela[0:6])
print("os quatro ultimos são: ", tabelageral[16: ])
print("a tabela organizada é: ", sorted(tabela+tabela2))
print("a posição da chapecoence é: ", tabelageral.index("chapecoence")+1)
