n = int(input())
num = int(input())

sum = 0

for i in range(n - 1, -1, -1):
    sum += num // (10**i)

    num = num % (10**i)

print(sum)