def valueiteration(rewards, ware, nofly):
    delta = 1
    n = len(rewards)
    v = [list] * n
    vf = []
    for i in range(n):
        v[i] = [0.0] * n
        for j in range(n):
            for yw in range(len(ware)):
                if (i == ware[yw][0]) & (j == ware[yw][1]):
                    v[i][j] = float(rewards[ware[yw][0]][ware[yw][1]])

            for yw in range(len(nofly)):
                if (i == nofly[yw][0]) & (j == nofly[yw][1]):
                    v[i][j] = float(rewards[nofly[yw][0]][nofly[yw][1]])
            if rewards[i][j] == 'None':
                v[i][j] = 'None'

    while delta > 0.00009:
        pol = []
        v2 = []

        for y in range(n):
            for x in range(n):

                check2 = 0
                check = 0
                for yw in range(len(ware)):
                    if (y == ware[yw][0]) & (x == ware[yw][1]):
                        check = 1
                for yw in range(len(nofly)):
                    if (y == nofly[yw][0]) & (x == nofly[yw][1]):
                        check = 1
                if rewards[y][x] == 'None':
                    v2.append('None')
                    pol.append('None')
                    check2 = 1
                if (check == 0) & (check2 == 0):
                    #up:
                    if ((y - 1) < 0) or (rewards[y-1][x] == 'None'):
                        r1 =float(rewards[y][x]) + 0.9 * v[y][x]
                    else:
                        r1 = float(rewards[y][x]) + 0.9 * v[y-1][x]
                    if ((x - 1) < 0) or (rewards[y][x-1] == 'None'):
                        r2 = float(rewards[y][x]) + 0.9 * v[y][x]
                    else:
                        r2 = float(rewards[y][x]) + 0.9 * v[y][x-1]
                    if ((x + 1) > (n - 1)) or (rewards[y][x+1] == 'None'):
                        r3 = float(rewards[y][x]) + 0.9 * v[y][x]
                    else:
                        r3 = float(rewards[y][x]) + 0.9 * v[y][x+1]
                    mU = 0.8 * (r1) + 0.1 * (r2) + 0.1 * (r3)
                    maximum = mU
                    p = 'N'
                    #down
                    if ((y + 1) > (n - 1)) or (rewards[y+1][x] == 'None'):
                        r1 = float(rewards[y][x]) + 0.9 * v[y][x]
                    else:
                        r1 = float(rewards[y][x]) + 0.9 * v[y+1][x]
                    if ((x - 1) < 0) or (rewards[y][x-1] == 'None'):
                        r2 = float(rewards[y][x]) + 0.9 * v[y][x]
                    else:
                        r2 = float(rewards[y][x]) + 0.9 * v[y][x-1]
                    if ((x + 1) > (n - 1)) or (rewards[y][x+1] == 'None'):
                        r3 = float(rewards[y][x]) + 0.9 * v[y][x]
                    else:
                        r3 = float(rewards[y][x]) + 0.9 * v[y][x+1]
                    mD = 0.8 * (r1) + 0.1 * (r2) + 0.1 * (r3)

                    if mD > maximum:
                        maximum = mD
                        p = 'S'

                    #left
                    if ((x-1) < 0) or (rewards[y][x-1] == 'None'):
                        r1 = float(rewards[y][x]) + 0.9 * v[y][x]
                    else:
                        r1 = float(rewards[y][x])+ 0.9 * v[y][x-1]
                    if ((y - 1) < 0) or (rewards[y-1][x] == 'None'):
                        r2 = float(rewards[y][x]) + 0.9 * v[y][x]
                    else:
                        r2 = float(rewards[y][x]) + 0.9 * v[y-1][x]
                    if ((y + 1) > (n - 1)) or (rewards[y+1][x] == 'None'):
                        r3 = float(rewards[y][x]) + 0.9 * v[y][x]
                    else:
                        r3 = float(rewards[y][x]) + 0.9 * v[y+1][x]
                    mL = 0.8 * (r1 ) + 0.1 * (r2) + 0.1 * (r3)

                    if mL > maximum:
                        maximum = mL
                        p = 'W'

                    #right
                    if ((x+1) > (n - 1)) or (rewards[y][x+1] == 'None'):
                        r1 = float(rewards[y][x]) + 0.9 * v[y][x]
                    else:
                        r1 = float(rewards[y][x]) + 0.9 * v[y][x+1]
                    if ((y - 1) < 0) or (rewards[y-1][x] == 'None'):
                        r2 = float(rewards[y][x]) + 0.9 * v[y][x]
                    else:
                        r2 = float(rewards[y][x]) + 0.9 * v[y-1][x]
                    if ((y + 1) > (n - 1)) or (rewards[y+1][x] == 'None'):
                        r3 = float(rewards[y][x]) + 0.9 * v[y][x]
                    else:
                        r3 = float(rewards[y][x]) + 0.9 * v[y+1][x]
                    mR = 0.8 * r1 + 0.1 * r2 + 0.1 * r3
                    if mR > maximum:
                        maximum = mR
                        p = 'E'

                    v2.append(maximum)
                    pol.append(p)
                elif check == 1:
                    v2.append(float(rewards[y][x]))
                    pol.append('None')
        maxi = -1
        for i in range(n):
            for j in range(n):
                x = abs(v[i][j] - v2[i*n+j])
                if x > maxi:
                    maxi = x
                v[i][j] = v2[i*n+j]

        delta = maxi
        vf.append(v2)
    return (vf, pol)


def policyiteration(rewards, ware, nofly):
    cont = 1
    n = len(rewards)
    v = [list] * n
    pol = [list] * n
    output = []
    for i in range(n):
        pol[i] = ['N'] * n
        for j in range(n):
            for yw in range(len(ware)):
                if (i == ware[yw][0]) & (j == ware[yw][1]):
                    pol[i][j] = 'None'

            for yw in range(len(nofly)):
                if (i == nofly[yw][0]) & (j == nofly[yw][1]):
                    pol[i][j] = 'None'
            if rewards[i][j] == 'None':
                pol[i][j] = 'None'
    temp = ['N'] * (n*n)
    for i in range(n):
        for j in range(n):
            temp[n*i + j] = pol[i][j]
    output.append(temp)
    while cont == 1:
        cont = 0
        delta2 = 1
        for i in range(n):
            v[i] = [0.0] * n
            for j in range(n):
                for yw in range(len(ware)):
                    if (i == ware[yw][0]) & (j == ware[yw][1]):
                        v[i][j] = float(rewards[ware[yw][0]][ware[yw][1]])

                for yw in range(len(nofly)):
                    if (i == nofly[yw][0]) & (j == nofly[yw][1]):
                        v[i][j] = float(rewards[nofly[yw][0]][nofly[yw][1]])
                if rewards[i][j] == 'None':
                    v[i][j] = 'None'
        while delta2 > 0.00009:
            v2 = []
            for y in range(n):
                for x in range(n):
                    check2 = 0
                    check = 0
                    for yw in range(len(ware)):
                        if (y == ware[yw][0]) & (x == ware[yw][1]):
                            check = 1
                            v2.append(float(rewards[y][x]))
                    for yw in range(len(nofly)):
                        if (y == nofly[yw][0]) & (x == nofly[yw][1]):
                            check = 1
                            v2.append(float(rewards[y][x]))
                    if rewards[y][x] == 'None':
                        v2.append('None')
                        check2 = 1
                    if (check == 0) & (check2 == 0):
                        if pol[y][x] == 'N':
                            if ((y - 1) < 0) or (rewards[y - 1][x] == 'None'):
                                r1 = float(rewards[y][x]) + 0.9 * v[y][x]
                            else:
                                r1 = float(rewards[y][x]) + 0.9 * v[y - 1][x]
                            if ((x - 1) < 0) or (rewards[y][x - 1] == 'None'):
                                r2 = float(rewards[y][x]) + 0.9 * v[y][x]
                            else:
                                r2 = float(rewards[y][x]) + 0.9 * v[y][x - 1]
                            if ((x + 1) > (n - 1)) or (rewards[y][x + 1] == 'None'):
                                r3 = float(rewards[y][x]) + 0.9 * v[y][x]
                            else:
                                r3 = float(rewards[y][x]) + 0.9 * v[y][x + 1]
                            v2.append(0.8 * (r1) + 0.1 * (r2) + 0.1 * (r3))
                        elif pol[y][x] == 'S':
                            if ((y + 1) > (n - 1)) or (rewards[y + 1][x] == 'None'):
                                r1 = float(rewards[y][x]) + 0.9 * v[y][x]
                            else:
                                r1 = float(rewards[y][x]) + 0.9 * v[y + 1][x]
                            if ((x - 1) < 0) or (rewards[y][x - 1] == 'None'):
                                r2 = float(rewards[y][x]) + 0.9 * v[y][x]
                            else:
                                r2 = float(rewards[y][x]) + 0.9 * v[y][x - 1]
                            if ((x + 1) > (n - 1)) or (rewards[y][x + 1] == 'None'):
                                r3 = float(rewards[y][x]) + 0.9 * v[y][x]
                            else:
                                r3 = float(rewards[y][x]) + 0.9 * v[y][x + 1]
                            v2.append(0.8 * (r1) + 0.1 * (r2) + 0.1 * (r3))
                        elif pol[y][x] == 'E':
                            if ((x + 1) > (n - 1)) or (rewards[y][x + 1] == 'None'):
                                r1 = float(rewards[y][x]) + 0.9 * v[y][x]
                            else:
                                r1 = float(rewards[y][x]) + 0.9 * v[y][x + 1]
                            if ((y - 1) < 0) or (rewards[y - 1][x] == 'None'):
                                r2 = float(rewards[y][x]) + 0.9 * v[y][x]
                            else:
                                r2 = float(rewards[y][x]) + 0.9 * v[y - 1][x]
                            if ((y + 1) > (n - 1)) or (rewards[y + 1][x] == 'None'):
                                r3 = float(rewards[y][x]) + 0.9 * v[y][x]
                            else:
                                r3 = float(rewards[y][x]) + 0.9 * v[y + 1][x]
                            v2.append(0.8 * r1 + 0.1 * r2 + 0.1 * r3)
                        elif pol[y][x] == 'W':
                            if ((x - 1) < 0) or (rewards[y][x - 1] == 'None'):
                                r1 = float(rewards[y][x]) + 0.9 * v[y][x]
                            else:
                                r1 = float(rewards[y][x]) + 0.9 * v[y][x - 1]
                            if ((y - 1) < 0) or (rewards[y - 1][x] == 'None'):
                                r2 = float(rewards[y][x]) + 0.9 * v[y][x]
                            else:
                                r2 = float(rewards[y][x]) + 0.9 * v[y - 1][x]
                            if ((y + 1) > (n - 1)) or (rewards[y + 1][x] == 'None'):
                                r3 = float(rewards[y][x]) + 0.9 * v[y][x]
                            else:
                                r3 = float(rewards[y][x]) + 0.9 * v[y + 1][x]
                            v2.append(0.8 * (r1) + 0.1 * (r2) + 0.1 * (r3))
            maxi = -1
            for i in range(n):
                for j in range(n):
                    x = abs(v[i][j] - v2[i * n + j])
                    if x > maxi:
                        maxi = x
                    v[i][j] = v2[i * n + j]
            delta2 = maxi
        polCheck = []
        for y in range(n):
            for x in range(n):
                check2 = 0
                check = 0
                for yw in range(len(ware)):
                    if (y == ware[yw][0]) & (x == ware[yw][1]):
                        check = 1
                for yw in range(len(nofly)):
                    if (y == nofly[yw][0]) & (x == nofly[yw][1]):
                        check = 1
                if rewards[y][x] == 'None':
                    v2.append('None')
                    polCheck.append('None')
                    check2 = 1
                if (check == 0) & (check2 == 0):
                    #up:
                    if ((y - 1) < 0) or (rewards[y-1][x] == 'None'):
                        r1 =float(rewards[y][x]) + 0.9 * v[y][x]
                    else:
                        r1 = float(rewards[y][x]) + 0.9 * v[y-1][x]
                    if ((x - 1) < 0) or (rewards[y][x-1] == 'None'):
                        r2 = float(rewards[y][x]) + 0.9 * v[y][x]
                    else:
                        r2 = float(rewards[y][x]) + 0.9 * v[y][x-1]
                    if ((x + 1) > (n - 1)) or (rewards[y][x+1] == 'None'):
                        r3 = float(rewards[y][x]) + 0.9 * v[y][x]
                    else:
                        r3 = float(rewards[y][x]) + 0.9 * v[y][x+1]
                    mU = 0.8 * (r1) + 0.1 * (r2) + 0.1 * (r3)
                    maximum = mU
                    p = 'N'
                    #down
                    if ((y + 1) > (n - 1)) or (rewards[y+1][x] == 'None'):
                        r1 = float(rewards[y][x]) + 0.9 * v[y][x]
                    else:
                        r1 = float(rewards[y][x]) + 0.9 * v[y+1][x]
                    if ((x - 1) < 0) or (rewards[y][x-1] == 'None'):
                        r2 = float(rewards[y][x]) + 0.9 * v[y][x]
                    else:
                        r2 = float(rewards[y][x]) + 0.9 * v[y][x-1]
                    if ((x + 1) > (n - 1)) or (rewards[y][x+1] == 'None'):
                        r3 = float(rewards[y][x]) + 0.9 * v[y][x]
                    else:
                        r3 = float(rewards[y][x]) + 0.9 * v[y][x+1]
                    mD = 0.8 * (r1) + 0.1 * (r2) + 0.1 * (r3)

                    if mD > maximum:
                        maximum = mD
                        p = 'S'

                    #left
                    if ((x-1) < 0) or (rewards[y][x-1] == 'None'):
                        r1 = float(rewards[y][x]) + 0.9 * v[y][x]
                    else:
                        r1 = float(rewards[y][x])+ 0.9 * v[y][x-1]
                    if ((y - 1) < 0) or (rewards[y-1][x] == 'None'):
                        r2 = float(rewards[y][x]) + 0.9 * v[y][x]
                    else:
                        r2 = float(rewards[y][x]) + 0.9 * v[y-1][x]
                    if ((y + 1) > (n - 1)) or (rewards[y+1][x] == 'None'):
                        r3 = float(rewards[y][x]) + 0.9 * v[y][x]
                    else:
                        r3 = float(rewards[y][x]) + 0.9 * v[y+1][x]
                    mL = 0.8 * (r1 ) + 0.1 * (r2) + 0.1 * (r3)

                    if mL > maximum:
                        maximum = mL
                        p = 'W'

                    #right
                    if ((x+1) > (n - 1)) or (rewards[y][x+1] == 'None'):
                        r1 = float(rewards[y][x]) + 0.9 * v[y][x]
                    else:
                        r1 = float(rewards[y][x]) + 0.9 * v[y][x+1]
                    if ((y - 1) < 0) or (rewards[y-1][x] == 'None'):
                        r2 = float(rewards[y][x]) + 0.9 * v[y][x]
                    else:
                        r2 = float(rewards[y][x]) + 0.9 * v[y-1][x]
                    if ((y + 1) > (n - 1)) or (rewards[y+1][x] == 'None'):
                        r3 = float(rewards[y][x]) + 0.9 * v[y][x]
                    else:
                        r3 = float(rewards[y][x]) + 0.9 * v[y+1][x]
                    mR = 0.8 * r1 + 0.1 * r2 + 0.1 * r3
                    if mR > maximum:
                        maximum = mR
                        p = 'E'

                    v2.append(maximum)
                    polCheck.append(p)
                elif check == 1:
                    v2.append(float(rewards[y][x]))
                    polCheck.append('None')
        for i in range(n):
            for j in range(n):
                if pol[i][j] != polCheck[i * n + j]:
                    cont = 1
                pol[i][j] = polCheck[i * n + j]
        output.append(polCheck)
    return output







#sample input
rewards= [['0', '-1'], ['0', '1']]
ware= [[1, 1]]
nofly= [[0, 1]]


print(valueiteration(rewards, ware, nofly))
print(policyiteration(rewards, ware, nofly))