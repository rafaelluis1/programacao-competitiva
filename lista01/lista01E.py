def k_step_ladder(lista):
    lista.sort()
    n = len(lista)
    plank1 = n - 1
    plank2 = n - 2

    while plank1 > 0 and plank2 > 0:
        if lista[plank2] >= plank2 + 1:
            return plank2
        elif lista[plank2] > 1:
            return lista[plank2] -1
        else:
            plank1 -= 1
            plank2 -= 1
    if plank2 < 0: plank2 = 0
    if plank1 < 0: plank1 = 0

    return plank2




queries = int(input())
ladders = []
for i in range(queries):
    planks = int(input())
    lengths = input().split()
    lengths = [int(lengths[j]) for j in range(len(lengths))]
    ladders.append(k_step_ladder(lengths))

for ladder in ladders:
    print(ladder)
