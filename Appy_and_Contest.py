# probs ---- 1 and n
# m1 --- probs/a
# m2 ---- probs/b
# leaving the probs div by both a and b
# min k probs
n = int(input())
while(n):
    N, A, B, K = map(int, input().split())
    a = N//A
    b = N//B
    c = N//(A*B)
    if(a+b)-c>=K:
        print('Win')
    else:
        print('Lose')