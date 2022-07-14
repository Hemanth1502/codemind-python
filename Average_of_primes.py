def prime(n):
    for i in range(2,n):
        if n%i==0:
            return 0
    else:
        return 1
n = int(input())
a = list(map(int, input().split()))
b = []
for i in a:
    if prime(i) and i!=1:
        b.append(i)
print('%0.2f'%(sum(b)/len(b)))