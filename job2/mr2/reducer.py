#!/usr/bin/env python3
"""reducer.py"""

import sys

userProducts = {}

for line in sys.stdin:
    userId, productId, score = line.split("\t")
    try:
        if userId not in userProducts:
            productsDict = {productId: score}
            userProducts[userId] = productsDict
        elif userId in userProducts:
            productsDict = userProducts[userId]
            productsDict[productId] = score
    except ValueError:
        pass
for user in userProducts:
    print("%s:" % user)
    productsDict = userProducts[user]
    sorted_dict = dict(sorted(productsDict.items(), key=lambda item: item[1], reverse=True))
    i = 0
    for product in sorted_dict:
        score = sorted_dict[product]
        if i > 5:
            break
        i = i + 1
        print("%s\t%s" % (product, score))
