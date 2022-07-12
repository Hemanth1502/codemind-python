def prime(n):
    for i in range(2,n):
        if n%i==0:
            return 0
    else:
        return 1
n = int(input())
a = []
for i in range(1,n+1):
    if n%i==0:
        a.append(i)
for i in a:
    if prime(i):
        a.remove(i)
    else:
        continue
print(len(a))