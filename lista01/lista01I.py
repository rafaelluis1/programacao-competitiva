data = input().split()
data = [int(data[i]) for i in range(len(data))]

n = data[0]%4
a = data[1]
b = data[2]
c = data[3]

comb = []

if n == 0:
    menor = 0
elif n == 2:
    comb = [b, 2*a, 2*c, a + c]  
    menor = min(comb)
elif n == 3:
    comb = [a, 3*c, b + c]
    menor = min(comb)
elif n == 1:
    comb = [c, 3*a, b + a, 2*b + c, 2*c + a]
    menor = min(comb)

print(menor)

