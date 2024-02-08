def ordena_merge(lista):
    if len(lista) > 1:
        meio = len(lista)//2
        left = [lista[i] for i in range(meio)]
        right = [lista[j] for j in range(meio,len(lista))]

        ordena_merge(left)
        ordena_merge(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lista[k] = left[i]
                i += 1
            else:
                lista[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lista[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            lista[k] = right[j]
            j += 1
            k += 1

n = int(input())
radii = input().split()
radii = [int(radii[i]) for i in range(n)]
ordena_merge(radii)
area = 0
for j in range(n-1, -1, -1):
    if n%2 == 0:
        if j%2 != 0:
            area += radii[j]**2
        else:
            area -= radii[j]**2
    else:
        if j%2 == 0:
            area += radii[j]**2
        else:
            area -= radii[j]**2
print(area*3.1415926536)

