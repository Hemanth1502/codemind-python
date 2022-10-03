t=int(input())
for i in range(t):
    n = input()
    a=int(n,16)
    b = list(str(bin(a))[2:])
    b=b[::-1]
    while(len(b)%4!=0):
        b.append('0')
    print(''.join(b[::-1]))