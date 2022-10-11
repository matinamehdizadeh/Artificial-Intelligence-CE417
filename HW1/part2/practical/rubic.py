from queue import PriorityQueue


class Node:

    def __init__(self, states, level, heuristicValue):
        self.states = states
        self.level = level
        self.heuristicValue = heuristicValue/n

    def getKey(self):
        return str(self.states)

    def __gt__(self, other):
        return self.heuristicValue + self.level >= other.heuristicValue + other.level



def Manhattan(state):
    man = 0
    for i in range(n*n):
        man += abs(goal[i] // n - state[i] // n) + abs(goal[i] % n - state[i] % n)
    return man


n = int(input())
n2 = n * n
state0 = [int] * n2
state = [int] * n2
goal = [int] * n2
end = 0
for i in range(n):
    h = input().split(' ')
    for j in range(n):
        goal[n*i + j] = n*i + j + 1
        state0[n*i + j] = int(h[j])


node = Node(state0, 0, Manhattan(state0))

frontier = PriorityQueue()
frontier.put(node)
explored = {}
explored[node.getKey()] = node.level
while True:

    if frontier.empty():
        break

    node = frontier.get()
    if node.heuristicValue == 0:
        print(node.level)
        break
    state0[0:] = node.states[0:]
    for i in range(n):
        if i != 0:
            state[0:n * i] = state0[0:n * i]
        state[n * i] = state0[n * i + n - 1]
        state[n * i + 1:n * i + n] = state0[n * i: n * i + n - 1]
        if i != n - 1:
            state[n * (i + 1):] = state0[n * (i + 1):]

        if str(state) not in explored or explored[str(state)] > node.level + 1:
            child = Node(state[0:], node.level + 1, Manhattan(state))
            if child.heuristicValue == 0:
                print(child.level)
                end = 1
                break
            frontier.put(child)
            explored[child.getKey()] = child.level
    if end == 1:
        break
    for i in range(n):
        if i != 0:
            state[0:n * i] = state0[0:n * i]
        state[n * i + n - 1] = state0[n * i]
        state[n * i:n * i + n - 1] = state0[n * i + 1: n * i + n]
        if i != n - 1:
            state[n * (i + 1):] = state0[n * (i + 1):]

        if str(state) not in explored or explored[str(state)] > node.level + 1:
            child = Node(state[0:], node.level + 1, Manhattan(state))
            if child.heuristicValue == 0:
                print(child.level)
                end = 1
                break
            frontier.put(child)
            explored[child.getKey()] = child.level
    if end == 1:
        break
    for i in range(n):
        state[0:] = state0[0:]
        for j in range(n - 1):
            state[n * (j + 1) + i] = state0[n * j + i]
        state[i] = state0[n * (n - 1) + i]
        if str(state) not in explored or explored[str(state)] > node.level + 1:
            child = Node(state[0:], node.level + 1, Manhattan(state))

            if child.heuristicValue == 0:
                print(child.level)
                end = 1
                break
            frontier.put(child)
            explored[child.getKey()] = child.level
    if end == 1:
        break
    for i in range(n):
        state[0:] = state0[0:]
        for j in range(1, n):
            state[n * (j - 1) + i] = state0[n * j + i]
        state[n * (n - 1) + i] = state0[i]

        if str(state) not in explored or explored[str(state)] > node.level + 1:
            child = Node(state[0:], node.level + 1, Manhattan(state))
            if child.heuristicValue == 0:
                print(child.level)
                end = 1
                break
            frontier.put(child)
            explored[child.getKey()] = child.level
    if end == 1:
        break
