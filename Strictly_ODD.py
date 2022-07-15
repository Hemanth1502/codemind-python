n = int(input())
a = list(map(int, input().split()))
c = 0
for i in range(len(a)):
    if (a[i])%2!=0 and (i)%2!=0:
        c = 0
    else:
        if (a[i])%2!=0 and i%2==0:
            c = c+1
            break
        else:
            continue
if c>0:
    print(False)
else:
    print(True)