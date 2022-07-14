def palindrome(n):
    x = int(str(n)[::-1])
    if x==n:
        return 1
    else:
        return 0
n = int(input())
a = list(map(int, input().split()))
c = 0
for i in range(len(a)):
    if palindrome(a[i]):
        c = c+1
print(c)