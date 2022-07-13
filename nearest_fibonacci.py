n = int(input())
a = 0
b = 1
c = a+b
s = []
for i in range(n):
    c = a+b
    a = b
    b = c
    s.append(a)
    if a>n:
        break
for i in range(len(s)):
    if s[i]>n:
        s.insert(i, n)
    else:
        continue
k = s.index(n)
if abs(s[k-1]-n)>abs(s[k+1]-n):
    print(s[k+1])
elif abs(s[k-1]-n)==abs(s[k+1]-n):
    print(s[k-1], s[k+1])
elif abs(s[k-1]-n)<abs(s[k+1]-n):
    print(s[k-1])