######### dfs, bfs #############

def dfs(i):
    visit[i] = True;
    print(i, end = " ");

    if(visit == True):
        print(i, end = "")

    for j in range(1, n + 1):
        if(graph[i][j] == 1 and visit[j] == False):
            dfs(j)

def bfs(i):
    list = []
    list.append(i)
    visit[i] = True;
    print(i, end = " ")

    while(list):
        temp = list.pop(-1)
        for j in range(1, n + 1):
            if(graph[temp][j] == 1 and visit[j] == False):
                list.append(j)
                visit[j] = True
                if(visit == True):
                    print(j, end = "")
                print(j, end = " ")

n, m, v = map(int, input().split(" "))

visit = [False for i in range(n + 1)]
graph = [[0 for col in range(n + 1)] for row in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split(" "))
    graph[a][b] = 1;
    graph[b][a] = 1;

dfs(v)

print()
visit = [False for i in range(n + 1)]

bfs(v)

