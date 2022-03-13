from re import S


def dobra(lst):
    for c in range(0, len(lst)):
        lst[c] *= 2
        print(lst[c], end="..")
    print(f"A lista dobrada é: {lst}")


valores = [3, 4, 5, 6]
dobra(valores)
