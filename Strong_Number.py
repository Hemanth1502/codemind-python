n = int(input())
temp = n
n = list(str(n))
for i in range(len(n)):
    n[i]=int(n[i])
c = 0
for i in range(len(n)):
    fact = 1
    for j in range(1,n[i]+1):
        fact = fact*j
    n[i]=fact
if sum(n)==temp:
    print('The number',temp,'is a strong number')
else:
    print('The number',temp,'is not a strong number')