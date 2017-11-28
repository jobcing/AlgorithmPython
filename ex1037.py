n = int(input())
numstr = input()

numlist = list(map(int, numstr.split(sep=' ')))

print(min(numlist)*max(numlist))