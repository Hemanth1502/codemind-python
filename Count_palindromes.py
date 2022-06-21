def palindrome(n):
    n = str(n)
    if n==n[::-1]:
        return 1
    else:
        return 0
n = int(input())
a = list(map(int, input().split()))
c = 0
for i in range(n):
    if palindrome(a[i]):
        c = c+1
    else:
        continue
print(c)