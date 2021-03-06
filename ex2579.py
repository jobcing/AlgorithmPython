n = int(input())

stair = []

for i in range(n):
    temp = int(input())
    stair.append(temp)

dp = []

dp.append(stair[0]) # 첫 번째
dp.append(stair[1] + dp[0]) # 두 번째
dp.append(max(stair[2] + stair[0], stair[2] + stair[1]))

for i in range(3, n):
    dp.append(max(stair[i] + dp[i - 2], stair[i] + stair[i - 1] + dp[i - 3]))

print(dp[n - 1])

