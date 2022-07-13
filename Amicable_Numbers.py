a = int(input())
b = int(input())
s1 = []
for i in range(1, a):
    if a%i==0:
        s1.append(i)
s2 = []
for i in range(1, b):
    if b%i==0:
        s2.append(i)
if sum(s1)==b and sum(s2)==a:
    print('Amicable')
else:
    print('Not Amicable')
# print(s1)
# print(s2)