t = int(input())
ans = []
for i in range(t):
    position = input().split()
    a = abs(int(position[0]))
    b = abs(int(position[1]))
    if a == b:
        ans.append(a + b)
    else:
        ans.append(a + b + (abs(a - b) - 1))

for n in ans:
    print(n)
