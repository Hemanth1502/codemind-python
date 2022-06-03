def prime(n):
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
           return 0
    return 1
def palindrome(n):
    a = list(str(n))
    if a == a[::-1]:
        return 1
    else:
        return 0
n = int(input())
i=n+1
while(True):
    if prime(i) and palindrome(i):
        print(i)
        break
    i = i + 1