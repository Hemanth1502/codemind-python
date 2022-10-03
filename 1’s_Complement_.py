n = int(input())
a=list(bin(n)[2:])
for i in range(len(a)):
    if a[i]=='0':
        a[i]='1'
    else:
        a[i]='0'
a=''.join(a)
b=int(a,2)
print(b)