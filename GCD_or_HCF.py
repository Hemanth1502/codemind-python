a, b = map(int, input().split())
k = max(a,b)
for i in range(1,k+1):
    if(a%i == 0 and b%i == 0):
        GCD = i
print(GCD)