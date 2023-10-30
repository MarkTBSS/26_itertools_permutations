""" result = []

for i in range(len(word)):
    firstElement = word[i]
    #print(firstElement)
    #print(word[:i])
    #print(word[i+1:])
    #print("==========1===========")
    charForntAndBack = word[:i] + word[i+1:]
    #print(charForntAndBack)
    #print("==========2===========")
    for j in charForntAndBack:
        result.append(firstElement + j)

    #print(result)

for k in result:
    print(k) """

import itertools

word = "HACK"
result = list(itertools.permutations(word, 2))
#print(result)
sortResult = sorted(result)
#print(sortResult)

for item in sortResult:
    print("".join(item))
