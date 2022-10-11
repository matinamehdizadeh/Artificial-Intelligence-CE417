from datetime import timedelta

def backTrack(assignment):
    ac3()
    if len(assignment) == m:
        return assignment

    for i in range(m):
        if marked[i] == 0:
            var = i
            break
    for i in range(len(domain[var])):
        nAssign = 0
        for j in range(len(constrain[var])):
            if constrain[var][j] in assignment:
                if domain[var][i] == assignment[constrain[var][j]]:
                    nAssign = 1
                    break
        if nAssign == 0:
            assignment[var] = domain[var][i]
            marked[var] = 1
            result = backTrack(assignment)
            if result != 0:
                return result
            if var in assignment:
                assignment.pop(var)
                marked[var] = 0
            break
    return 0

def ac3():
    queue = []
    for i in range(len(constrain)):
        for j in range(len(constrain[i])):
            queue.append([i, constrain[i][j]])
    while len(queue) != 0:
        [xi,xj] = queue.pop(0)
        if consistent([xi, xj]):
            for i in range(len(constrain[xi])):
                queue.append([constrain[xi][i],xi])

def consistent(n):
    x = n[0]
    y = n[1]
    remove = []
    for i in range(len(domain[x])):
        check = 0
        for j in range(len(domain[y])):
            if domain[x][i] != domain[y][j]:
                check = 1
                break
        if check == 0:
            remove.append(domain[x][i])


    if len(remove) > 0:
        for i in range(len(remove)):
            domain[x].remove(remove[i])
        return True
    return False


h = input().split(' ')
n, m = int(h[1]), int(h[0])
domain = [list] * m
constrain = [list] * m
Sclock = [timedelta] * m
Eclock = [timedelta] * m
assignment = {}
marked =[0] * m
for i in range(m):
    domain[i] = []
    constrain[i] = []
    h = input().split('-')
    n2 = h[0].split(':')
    Sclock[i] = timedelta(hours=int(n2[0]), minutes=int(n2[1]))
    n2 = h[1].split(':')
    Eclock[i] = timedelta(hours=int(n2[0]), minutes=int(n2[1]))

for i in range(m):
    for j in range(i+1, m):
        if Sclock[j] < Eclock[i]:
            constrain[i].append(j)
            constrain[j].append(i)

for i in range(n):
    h = input().split(' ')
    for j in range(len(h)):
        domain[int(h[j]) - 1].append(i)

if backTrack(assignment) == 0:
    print("NO")
else:
    for i in range(m):
        print(assignment[i] + 1)