def palindrome(n):
    k = int(str(n)[::-1])
    if k==n:
        return 1
    else:
        return 0
n = int(input())
i = n+1
while(True):
    if palindrome(i):
        p1 = i
        break
    else:
        i = i+1
j = n-1
while(True):
    if palindrome(j):
        p2 = j
        break
    else:
        j = j-1
if abs(p1-n)>abs(p2-n):
    print(p2)
elif abs(p1-n)==abs(p2-n):
    print(min(p1, p2), max(p1, p2))
else:
    print(p1)