import math

MAX_N = 100000
dp = [0 for _ in range(MAX_N+1)]
square_num = []
for i in range(1, int(math.sqrt(MAX_N))+1):
    square_num.append(i**2)
    dp[i**2] = 1

N = int(input())

for i in range(1, N+1):
    min_count = 1000000
    if dp[i] == 1:
        pass
    for num in square_num:
        if i-num < 0:
            break
        min_count = min(dp[i-num], min_count)
    dp[i] = min_count + 1

print(dp[N])


