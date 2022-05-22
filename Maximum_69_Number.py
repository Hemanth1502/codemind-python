n = int(input())
a = list(str(n))
for i in range (0,len(a)):
    if(a[i]=='6'):
        a[i]='9'
        break
    else:
        continue
n = ''.join(a)
print(n)
