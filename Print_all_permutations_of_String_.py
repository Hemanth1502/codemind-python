from itertools import permutations
n = input()
for i in permutations(n,len(n)):
    print(''.join(i))