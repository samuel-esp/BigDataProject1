#!/usr/bin/env python3
"""reducer.py"""

import sys

userProducts = {}
resultTuplesList = []

for line in sys.stdin:
    userId, productId = line.split("\t")
    try:
        if userId not in userProducts:
            productList = [productId]
            userProducts[userId] = productList
        elif userId in userProducts:
            productList = userProducts[userId]
            productList.append(productId)
    except ValueError:
        pass
for user1 in userProducts:
    productListU1 = userProducts[user1]
    for user2 in userProducts:
        if user1 != user2:
            productListU2 = userProducts[user2]
            commonProductsCount = len(list(set(productListU1).intersection(productListU2)))
            if commonProductsCount >= 3:
                commonProducts = list(set(productListU1).intersection(productListU2))
                resultTuplesList.append((user1, user2, commonProducts))

# clean duplicates
cleanTuplesList, seen = [], set()
for i in resultTuplesList:
    item = (i[0], i[1], tuple(i[2]))
    if (item[0], item[1], item[2]) not in seen and (item[1], item[0], item[2]) not in seen:
        seen.add(item)
        cleanTuplesList.append(item)

# sort tuples to print result
sortedResultTuplesList = sorted(cleanTuplesList, key=lambda tup: tup[0])  # sort tuples
for t in sortedResultTuplesList:
    print("User1 ID: %s User2 ID: %s Common Products:" % (t[0], t[1]))
    for commonProduct in t[2]:
        print("%s:" % commonProduct)
