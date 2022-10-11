def insert_min(num, arr):
    arr.append(num)
    j = len(arr) - 1
    while j - 1 >= 0:
        if arr[j][1] < arr[(j - 1) // 2][1]:
            arr[j], arr[(j - 1) // 2] = arr[(j - 1) // 2], arr[j]
            j = (j - 1) // 2
        else:
            break


def del_min(arr, num):
    arr[num], arr[len(arr) - 1] = arr[len(arr) - 1], arr[num]
    j = num
    while j - 1 >= 0:
        if arr[j][1] < arr[(j - 1) // 2][1]:
            arr[j], arr[(j - 1) // 2] = arr[(j - 1) // 2], arr[j]
            j = (j - 1) // 2
        else:
            break
    while 2 * j + 1 < len(arr) - 1:
        if (2 * j) + 2 < len(arr) - 1:
            if arr[2 * j + 1][1] < arr[2 * j + 2][1]:
                x = 2 * j + 1
            else:
                x = 2 * j + 2
        else:
            x = 2 * j + 1
        if arr[j][1] > arr[x][1]:
            arr[j], arr[x] = arr[x], arr[j]
            j = x
        else:
            break
    arr.pop(len(arr) - 1)


points = [int] * 4
h = input().split(' ')
n, m = int(h[0]), int(h[1])
h = input().split(' ')
points[0], points[1] = int(h[0]) - 1, int(h[1]) - 1
h = input().split(' ')
points[2], points[3] = int(h[0]) - 1, int(h[1]) - 1

way1 = []
way2 = []
graph = [list()] * n
bestPair1 = [int] * n
bestPair2 = [int] * n
d = [list()] * 4
for i in range(n):
    if i < 4:
        d[i] = []
    graph[i] = []
    bestPair1[i] = i
    bestPair2[i] = i
for i in range(m):
    h3 = input().split(' ')
    first = int(h3[0]) - 1
    second = int(h3[1]) - 1
    wight = int(h3[2])
    graph[first].append([second, wight])
    graph[second].append([first, wight])
for k in range(4):
    d[k] = [0] * n
    mark = [0] * n
    mark2 = [0] * n
    mark[points[k]] = 1
    finish = [0] * n
    queue = [] * n
    queue.append([points[k], 0])
    while len(queue) > 0:
        u = queue[0][0]
        if finish[u] == 1:
            if (k == 1) & (mark2[u] == 0):
                way1.append(u)
                mark2[u] = 1
            elif (k == 0) & (mark2[u] == 0):
                way2.append(u)
                mark2[u] = 1

            del_min(queue, 0)
        else:
            finish[u] = 1
            for i in range(graph[u].__len__()):
                if mark[graph[u][i][0]] == 0:
                    d[k][graph[u][i][0]] = d[k][u] + graph[u][i][1]
                    mark[graph[u][i][0]] = 1
                    insert_min([graph[u][i][0], d[k][graph[u][i][0]]], queue)
                elif finish[graph[u][i][0]] == 0:
                    if d[k][graph[u][i][0]] > d[k][u] + graph[u][i][1]:
                        d[k][graph[u][i][0]] = d[k][u] + graph[u][i][1]
                        insert_min([graph[u][i][0], d[k][graph[u][i][0]]], queue)


for i in range(n):
    u = way1[i]
    if d[0][u] + d[1][u] == d[0][points[1]]:
        for j in range(len(graph[u])):
            if ((d[0][graph[u][j][0]] + d[1][graph[u][j][0]]) == d[0][points[1]]) & ((graph[u][j][1] + d[1][u]) == d[1][graph[u][j][0]]):
                if d[3][bestPair1[graph[u][j][0]]] > d[3][bestPair1[u]]:
                    bestPair1[graph[u][j][0]] = bestPair1[u]
    u = way2[i]
    if d[0][u] + d[1][u] == d[0][points[1]]:
        for j in range(len(graph[u])):
            if ((d[0][graph[u][j][0]] + d[1][graph[u][j][0]]) == d[0][points[1]]) & ((graph[u][j][1] + d[0][u]) == d[0][graph[u][j][0]]):
                if d[3][bestPair2[graph[u][j][0]]] > d[3][bestPair2[u]]:
                    bestPair2[graph[u][j][0]] = bestPair2[u]


for i in range(n):
    if i == 0:
        min1 = d[2][i] + d[3][bestPair1[i]]
        min2 = d[2][i] + d[3][bestPair2[i]]
    else:
        x1 = d[2][i] + d[3][bestPair1[i]]
        if min1 > x1:
            min1 = x1
        x2 = d[2][i] + d[3][bestPair2[i]]
        if min2 > x2:
            min2 = x2
print(min(min1, min2))

