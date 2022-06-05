def odd(n):
    if n%2!=0 and n!=0:
        return 1
    else:
        return 0
n = int(input())
a = list(map(int, input().split()))
c = 0
for i in range(len(a)):
    if odd(a[i]) and odd(i):
        c = 0
    else:
        if odd(a[i]) and i!=odd:
            c = 1
            break
        else:
            continue
if c==1:
    print(False)
else:
    print(True)