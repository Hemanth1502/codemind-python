P, R, T = map(int, input().split())
CI = P*((1+(R/100))**T)
print('%0.2f'%CI)