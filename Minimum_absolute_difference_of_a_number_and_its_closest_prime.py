def prime(n):
    for i in range(2, n):
        if n%i==0:
            return 0
    else:
        return 1
n = int(input())
# print(n)
if prime(n):
    print(0)
else:
    i = n+1
    while(True):
        if prime(i):
            s = i
            break
        else:
            i = i+1
    j = n-1
    while(True):
        if prime(j):
            c = j
            break
        else:
            j = j-1
    print(min(abs(s-n), abs(c-n)))