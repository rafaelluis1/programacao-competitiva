n = int(input())
problems = input().split()
problems = [int(problems[i]) for i in range(n)]

problems.sort()
count = j = 0
k = 1
while j < n:
    if problems[j] < k:
        j += 1
    else:
        count += 1
        k += 1
        j += 1

print(count)
