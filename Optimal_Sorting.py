n = int(input())
while(n):
    s = int(input())
    l = list(map(int, input().split()))
    sl = len(l)
    c = 0
    for i in range (0,sl-1):
        if l[i]>l[i+1]:
            temp = l[i]
            l[i] = l[i+1]
            l[i+1] = temp
            c = c + 1
    if c == 0:
        print('0')
    else:
        f = max(l) - min(l)
        print(f)