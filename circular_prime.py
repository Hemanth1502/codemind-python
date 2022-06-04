def prime(n):
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
           return 0
    return 1
n = int(input())
ns = list(str(n))
rs = ns[::-1]
r = int(''.join(rs))
if prime(n) and prime(r):
    print('circular prime')
elif prime(n) and r!=prime:
        print('prime but not a circular prime')
# elif n!=prime:
#             print('not prime')
else:
    print('not prime')