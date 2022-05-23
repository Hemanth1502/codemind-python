n = int(input())
c = 0
r = 0
x = 0
t=n
while(n):
    d = n%10
    r = r*10+d
    n = n//10
for i in range (1,t+1):
    if(t%i == 0):
        c = c+1
for j in range (1,r+1):
    if(r%j==0):
        x = x+1
if c == 2 and x == 2:
    print('circular prime')
elif(c!=2 and x!=2):
    print('not prime')
else :
    print('prime but not a circular prime')