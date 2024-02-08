n = int(input())
sizes = input().split()
sizes = [int(sizes[i]) for i in range(n)]

sizes.sort()

tem = False
for j in range(2, n):
    lado1 = sizes[j-2]
    lado2 = sizes[j-1]
    lado3 = sizes[j]
    if lado1+lado2 > lado3 and lado1+lado3 > lado2 and lado2 + lado3 > lado1:
        tem = True
        print("YES")
        break
if not tem: print("NO")

