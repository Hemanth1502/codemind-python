def palindrome(n):
    temp = n
    r = 0
    while(n):
        d = n%10
        r = r*10 + d
        n = n//10
    if temp == r:
        return 1
    else:
        return 0
a = int(input())
b = int(input())
for i in range (a, b+1):
    if palindrome (i):
        print(i, end=' ')
    else:
        continue