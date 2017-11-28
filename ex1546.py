n = int(input())

score = input()
scorelist = list(map(int, score.split(" ")))

m = max(scorelist)

for i in range(len(scorelist)):
    scorelist[i] = scorelist[i] / m * 100

sum = 0

for i in scorelist:
    sum += i

avg = sum / n

print("%.2f" % avg)
print(scorelist)