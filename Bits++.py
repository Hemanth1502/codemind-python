t=int(input())
c=0
for i in range(t):
    s=str(input())
    for i in s:
        if i=='X':
            continue
        elif i=='+':
            c=c+(0.5)
        elif i=='-':
            c=c-(0.5)
print(int(c))