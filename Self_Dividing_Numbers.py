def sd(n):
    temp = n
    n = list(str(n))
    c = 0
    for i in range(len(n)):
        n[i]=int(n[i])
    for i in range(len(n)):
        if n[i]!=0:
            if temp%n[i]==0:
                c = c+1
        else:
            continue
    if c==len(n):
        return 1
    else:
        return 0
a = int(input())
b = int(input())
c = []
for i in range(a, b+1):
    if sd(i):
        c.append(i)
    else:
        continue
print(*c)