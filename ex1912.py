n = int(input())

numlist = list(map(int, input().split(" ")))
dp = []

dp.append(numlist[0])

for i in range(n):
    dp.append(dp[i - 1] + numlist[i])

print(max(dp))