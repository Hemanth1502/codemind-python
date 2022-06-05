def even(n):
    if n%2==0 or n==0:
        return 1
    else:
        return 0
n = int(input())
a = list(map(int, input().split()))
c = 0
for i in range(len(a)):
    if even(a[i]) and even(i):
        c = 0
    else:
        if even(a[i]) and i!=even:
            c = c+1
        else:
            continue
if c>0:
    print(False)
else:
    print(True)
