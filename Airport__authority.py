n = int(input())
c = 0
s = []
for i in range (n):
    a = int(input())
    s.append(a)
k = int(input())
for i in range (len(s)):
    if s[i]<=k:
        c = c + 1
    else:
        c = c+2
print(c)