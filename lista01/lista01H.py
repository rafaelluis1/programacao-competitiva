def QuatroSete(n):
    string = ''
    while True:
        if n < 4:
            resto = n
            break
        if n%7 != 0:
            n -= 4
            string += '4'

        if n%7 == 0:
            string += (n//7)*'7'
            resto = n%7
            break
        
    if resto:
        return -1
    else:
        return string

n = int(input())

print(QuatroSete(n))

