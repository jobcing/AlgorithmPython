senten = input()

str = senten.split(sep=' ')
cnt = 0

for i in str:
    if(i==''):
        continue
    else:
        cnt = cnt + 1

print(cnt)

