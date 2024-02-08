n = int(input())
data = input().split()

#disregard starting zeroes:
i = 0
while i < n and data[i] == '0':
    i+=1

#disregard trailing zeroes:
j = n - 1
while j > 0  and data[j] == '0':
    j -=1

#count occurrences of groups of zeros:

ones = 0
count = 0

while i <= j:
    if data[i] =='1':
        i +=1
        ones += 1
    else:
        zeros = 0
        while i <= j and data[i] == '0':
            zeros += 1
            i +=1
        if zeros > 1:
            count += 1
        else: ones += 1

print(count + ones)
        
       
