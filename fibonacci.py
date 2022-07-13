n = int(input())
a = 0
b = 1
s = []
while(True):
    s.append(a)
    c = a+b
    a = b
    b = c
    if len(s)>=n:
        break
print(*s)