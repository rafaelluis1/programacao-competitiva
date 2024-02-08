def coins(num):
    for i in range(0, num//1234567 + 1):
        for j in range(0,(num - i*1234567)//123456 + 1):
            k = (num - i*1234567 - j*123456)//1234
            if i*1234567 + j*123456 + k*1234 == num:
                return "YES"
            
    return "NO"


n = int(input())
print(coins(n))
