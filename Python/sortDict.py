import operator

dict1 = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

A_sortedbyValue = sorted(dict1.items(), key=operator.itemgetter(1))
D_sortedbyValue = sorted(
    dict1.items(), key=operator.itemgetter(1), reverse=True)

A_sortedbyKey = sorted(dict1.items(), key=operator.itemgetter(0))
D_sortedbyKey = sorted(dict1.items(), key=operator.itemgetter(0), reverse=True)

print("Sorting by Value")
print(A_sortedbyValue)
print(D_sortedbyValue)


print("Sorting by Key")
print(A_sortedbyKey)
print(D_sortedbyKey)

A_sortedbyValueL = sorted(dict1.items(), key=lambda x: x[1])
D_sortedbyValueL = sorted(dict1.items(), key=lambda x: x[1], reverse=True)

A_sortedbyKeyL = sorted(dict1.items(), key=lambda x: x[0])
D_sortedbyKeyL = sorted(dict1.items(), key=lambda x: x[0], reverse=True)

print("Sorting by Value")
print(A_sortedbyValueL)
print(D_sortedbyValueL)


print("Sorting by Key")
print(A_sortedbyKeyL)
print(D_sortedbyKeyL)
