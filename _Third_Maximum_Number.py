n = int(input())
a = list(map(int, input().split()))
if n<3:
    print(max(a))
else:
    b = []
    for i in a:
        if i not in b:
            b.append(i)
    b = sorted(b)[::-1]
    print(b[2])