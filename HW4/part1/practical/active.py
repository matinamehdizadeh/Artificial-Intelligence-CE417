h = input().split(' ')
n, m = int(h[0]), int(h[1])
graph = [list] * n
for i in range(n):
    graph[i] = []
for i in range(m):
    h = input().split(' ')
    a, b = int(h[0]) - 1, int(h[1]) - 1
    graph[b].append(a)
q = int(input())
for i in range(q):
    inactive = 0
    mark = [0] * n
    path = input().split(' ')
    for j in range(len(path)):
        path[j] = int(path[j]) - 1


    evidence = input().split(' ')
    if evidence[0] == "none":
        evidence.remove("none")
    for j in range(len(evidence)):
        evidence[j] = int(evidence[j]) - 1
    for j in range(len(path)-2):
        left, right = 0, 0
        for k in range(len(graph[path[j+1]])):
            if path[j] == graph[path[j+1]][k]:
                left = 1
            elif path[j+2] == graph[path[j+1]][k]:
                right = 1
        if (right == 1) & (left == 1):
            for k1 in range(len(evidence)):
                stack = []
                stack.append(evidence[k1])
                mark[evidence[k1]] = 1
                while len(stack) > 0:
                    u = stack.pop()
                    for k2 in graph[u]:
                        mark[k2] = 1
                        stack.append(k2)
            if mark[path[j + 1]] != 1:
                inactive = 1
                print("inactive")
                break
        elif right == 1:
            for k in range(len(graph[path[j]])):
                if path[j+1] == graph[path[j]][k]:
                    left = 1
                    break
            if left == 1:
                for k1 in range(len(evidence)):
                    if path[j + 1] == evidence[k1]:
                        inactive = 1
                        print("inactive")
                        break
        elif left == 1:
            for k in range(len(graph[path[j + 2]])):
                if path[j+1] == graph[path[j+2]][k]:
                    right = 1
                    break
            if right == 1:
                for k1 in range(len(evidence)):
                    if path[j + 1] == evidence[k1]:
                        inactive = 1
                        print("inactive")
                        break
        else:
            for k1 in range(len(evidence)):
                if path[j + 1] == evidence[k1]:
                    inactive = 1
                    print("inactive")
                    break
        if inactive == 1:
            break

    if inactive == 0:
        print("active")







