a = int(input())
b = int(input())
r = 0
c = 0
for i in range (a, b+1):
    I=i
    dc = 0
    c = 0
    while(i):
        d = i%10
        i = i//10
        dc = dc+1
        if d == 0:
            continue
        if I%d == 0:
                c = c + 1
    if dc == c:
        print(I, end= ' ')