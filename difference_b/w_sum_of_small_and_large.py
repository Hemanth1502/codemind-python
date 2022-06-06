n = input()
a = list(n.split())
k = len(a)
x2 = 0
y2 = 0
for i in range(len(a)):
    x = min(a[i])
    y = max(a[i])
    x1 = ord(x)
    y1 = ord(y)
    x2 = x2 + x1
    y2 = y2 + y1
print(abs(x2-y2))