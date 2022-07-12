def palindrome(n):
    n = str(n)
    if n==n[::-1]:
        return 1
    else:
        return 0
def prime(n):
    for i in range(2,n):
        if n%i==0:
            return 0
    else:
        return 1
n = int(input())
i = n+1
while(True):
    if palindrome(i) and prime(i):
        print(i)
        break
    else:
        i = i+1