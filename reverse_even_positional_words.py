n = input()
a = list(map(str, n.split()))
for i in range(len(a)):
    if i%2==0:
        temp = a[i]
        a[i] = temp[::-1]
    else:
        continue
print(*a)