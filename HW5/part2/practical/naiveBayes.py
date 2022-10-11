import csv
import random
text = csv.reader(open("bbc-text.csv", "r"))
train = list(text)
lenTest = len(train) // 10
test = []
train.pop(0)
while len(test) < lenTest:
    x = random.randrange(0, len(train))
    test.append(train.pop(x))

classes = {}
for i in range(len(train)):
    if train[i][0] not in classes:
        classes[train[i][0]] = []
train_words = {}
c = 0

for i in range(len(train)):
    train[i][1].replace('-', ' ')
    words = train[i][1].lower().split(" ")
    for x in words:
        if x == ',' or x == '.' or x == '?' or x == ';' or x == '!' or x == '&':
            continue
        if x == "the" or x == "am" or x == "is" or x == "are" or x == "with" or x == "in" or x == "I" or x == "as" \
                or x == "of" or x == "to" or x == "that" or x == "this" or x == "on":
            continue
        if x.endswith(',') or x.endswith('?') or x.endswith(';') or x.endswith('!') or x.endswith('.') or \
                x.endswith(')') or x.endswith('%') or x.endswith('s') or x.endswith('ed'):
            x = x[0:len(x) - 1]
        if x.startswith('(') or x.startswith('$'):
            x = x[1:]
        if x.startswith('Â£'):
            x = x[0:2]

        if x not in train_words:
            train_words[x] = c
            for keys in classes.keys():
                classes[keys] += [1]
            c += 1
            classes[train[i][0]][-1] += 1

        else:
            index = train_words.get(x)
            classes[train[i][0]][index] += 1
sumT = {}
for keys in classes.keys():
    sumT[keys] = sum(classes[keys])
results = []
for t in test:

    proper_words = []
    t[1].replace('-', ' ')
    whole_words = t[1].lower().split(" ")
    for x in whole_words:

        if x == ',' or x == '.' or x == '?' or x == ';' or x == '!' or x == '&':
            continue
        if x == "the" or x == "am" or x == "is" or x == "are" or x == "with" or x == "in" or x == "I" or x == "as" \
                or x == "of" or x == "to" or x == "that" or x == "this" or x == "on":
            continue
        if x.endswith(',') or x.endswith('?') or x.endswith(';') or x.endswith('!') or x.endswith('.') or \
                x.endswith(')') or x.endswith('%') or x.endswith('s') or x.endswith('ed'):
            x = x[0:len(x) - 1]
        if x.startswith('(') or x.startswith('$'):
            x = x[1:]
        if x.startswith('Â£'):
            x = x[0:2]

        proper_words += [x]
    p = {}
    for keys in classes.keys():
        p[keys] = 1
    for word in proper_words:
        if train_words.get(word):
            for keys in classes.keys():
                p[keys] *= (classes[keys][train_words.get(word)] / sumT[keys])
        s = 0
        for keys in p:
            s += p[keys]
        for keys in p:
            p[keys] = p[keys]/s

    maxT = -1
    for keys in p.keys():
        if p[keys] > maxT:
            maxT = p[keys]
            res = keys
    if t[0] == res:
        results += [1]
    else:
        results += [0]

print(round(sum(results) / len(results)*100))
