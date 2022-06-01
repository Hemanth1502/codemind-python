def palindrome(n):
    temp = n
    r = 0
    while(n):
        d = n%10
        r = r*10+d
        n = n//10
    if r == temp:
        return 1
    else:
        return 0
n = int(input())
a = []
a.append(n)
for i in range (1,2*n):
    if palindrome(i):
        a.append(i)
    else:
        continue
g = set(a)
x = list(sorted(g))
d = x.index(n)
if abs(x[d]-x[d+1])==abs(x[d-1]-x[d]):
    print(x[d-1],x[d+1])
else:
    if abs(x[d]-x[d+1])>abs(x[d-1]-x[d]):
        print(int(x[d-1]))
    else:
        print(int(x[d+1]))