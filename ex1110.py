cnt = 0

x = int(input())
num = x

while True:
    a = num // 10
    b = num % 10

    c = a + b

    d = str(b) + str(c % 10)

    d = int(d)

    cnt = cnt + 1

    if(d==x):
        break
    else:
        num = d
        continue

print(cnt)