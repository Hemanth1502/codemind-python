def prime(n):
    for i in range(2,n):
        if n%i==0:
            return 'not a prime'
    else:
        return 'prime'
n = int(input())
print(prime(n))