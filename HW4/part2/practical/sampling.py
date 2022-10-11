import random
import matplotlib.pyplot as plt


def probability(prob, cpt):
    while len(prob) > 0:
        cpt = cpt[prob[0]]
        prob = prob[1:]
    return cpt[0]


def gibbs(iteration):
    sample = [int] * 7
    counter = 0
    for i in range(7):
        if i in evidence.keys():
            sample[i] = evidence[i]
        else:
            sample[i] = random.randrange(0, 2)
    for j in range(iteration):
        for node in range(7):
            if evidence.get(node) is None:
                prob = []
                pNode = [1, 1]
                for i in parents[node]:
                    prob.append(sample[i])
                x = probability(prob, cpt[node])
                pNode[0] *= x
                pNode[1] *= (1 - x)
                for i in children[node]:
                    prob = []
                    for j in parents[i]:
                        if j == node:
                            prob.append(0)
                        else:
                            prob.append(sample[j])
                    x = probability(prob, cpt[i])
                    if sample[i] == 1:
                        pNode[1] *= x
                    else:
                        pNode[1] *= (1 - x)
                    prob = []
                    for j in parents[i]:
                        if j == node:
                            prob.append(1)
                        else:
                            prob.append(sample[j])
                    x = probability(prob, cpt[i])
                    if sample[i] == 1:
                        pNode[0] *= x
                    else:
                        pNode[0] *= (1 - x)
                pNode = [pNode[0] / (pNode[0] + pNode[1]), pNode[1] / (pNode[0] + pNode[1])]
                r = random.uniform(0, 1)
                if r < pNode[0]:
                    sample[node] = 1
                else:
                    sample[node] = 0
        valid = 1
        for i in query.keys():
            if sample[i] != query[i]:
                valid = 0
        if valid == 1:
            counter += 1
    return counter / iteration




cpt = [[0.6], [[0.45], [0.25]], [[0.7], [0.4]], [[[0.5], [0.6]], [[0.7], [0.8]]],
       [[[0.6], [0.2]], [[0.1], [0.5]]], [[0.25], [0.2]], [[[0.7], [0.5]], [[0.3], [0.5]]]]
parents = [[], [0], [0], [1, 2], [2, 3], [3], [3, 4]]
children = [[1, 2], [3], [3, 4], [4, 5, 6], [6], [], []]
convert = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6}
evidence = {}
query = {}
x = []
y = []

h1 = input().split('|')
h12 = h1[0].split(',')
for i in range(len(h12)):
    h121 = h12[i].strip().split('=')
    query[convert[h121[0]]] = int(h121[1])
h12 = h1[1].split(',')
for i in range(len(h12)):
    h121 = h12[i].strip().split('=')
    evidence[convert[h121[0]]] = int(h121[1])

exact = float(input())

counter = 0
for i in range(100, 1050, 50):
    g = gibbs(i)
    y.append((1-abs(g - exact))*100)
    x.append(i)
    if i > 500:
        counter += g

print(counter/10)
plt.plot(x, y)
plt.show()
