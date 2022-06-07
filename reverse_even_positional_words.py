n = input()
a = list(map(str, n.split()))
for i in range(len(a)):
    if i%2==0:
        a[i] = a[i][::-1]
print(*a)