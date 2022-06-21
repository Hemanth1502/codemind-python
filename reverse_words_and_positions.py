n = input().split()
a = list(n)
for i in range(len(a)):
    a[i]=a[i][::-1]
print(*a[::-1])