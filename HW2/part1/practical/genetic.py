import random


def fitnessFunc(parent):
    sum = 0.0
    for i in range(n):
        sum += parent[i] * x[i]
    return 1.0 / abs(maximum - sum)


def select():
    max = 0
    fit = [float] * number
    sumFit = 0
    for i in range(number):
        fit[i] = fitnessFunc(startSample[i])
        sumFit += fit[i]
    for i in range(number):
        xS = 0
        x = random.uniform(0, 10)
        for j in range(number):
            if max < fit[j] / sumFit:
                max = fit[j] / sumFit
                maxprob[0:] = startSample[j][0:]
            if (x >= xS) & (x < (xS + (fit[j] / sumFit) * 10)):
                parents[i][0:] = startSample[j][0:]
            xS += (fit[j] / sumFit) * 10




def crossOver():
    for i in range(number//2):
        index = random.randrange(0, n) + 1
        swap1[0:index] = parents[2*i][0:index]
        swap1[index:] = parents[2*i + 1][index:]
        swap2[0:index] = parents[2*i + 1][0:index]
        swap2[index:] = parents[2*i][index:]
        parents[2*i][0:] = swap1[0:]
        parents[2*i + 1][0:] = swap2[0:]


def mutation():
    for i in range(number):
        tf = random.randrange(0,2)
        if tf == 1:
            index = random.randrange(0, n)
            parents[i][index] = random.uniform(-10, 10)



input()
Sx = input().split(',')
n = len(Sx)
number = 26
startSample = [list()] * number
parents = [list()] * number
swap1 = [float] * number
swap2 = [float] * number
maxprob = [] * n
x = [float] * n
maximum = 0
for i in range(n):
    x[i] = float(Sx[i])
    if x[i] > 0:
        maximum += x[i] * 10
    else:
        maximum += x[i] * (-10)
for i in range(number):
    startSample[i] = []
    parents[i] = []
    for j in range(n):
        startSample[i].append(random.uniform(-10, 10))

for i in range(1000):
    select()
    crossOver()
    if n != 999:
        mutation()
    startSample[0:] = parents[0:]
    print(maxprob)



