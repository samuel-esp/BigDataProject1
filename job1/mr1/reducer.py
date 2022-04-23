#!/usr/bin/python3
"""reducer.py"""

import sys

yearWords = {}
for line in sys.stdin:
    year, word = line.split("\t")
    try:
        if year not in yearWords:
            wordsCount = {word: 1}  # ciao: 1
            yearWords[year] = wordsCount  # 2010: {ciao: 1}
        elif year in yearWords:
            wordsCount = yearWords[year]  # 2010: {ciao: 1}
            if word not in wordsCount:
                wordsCount[word] = 1
            else:
                wordsCount[word] = wordsCount[word] + 1
    except ValueError:
        pass
for year in yearWords:
    print("%s:" % year)
    wordsDict = yearWords[year]
    sorted_dict = dict(sorted(wordsDict.items(), key=lambda item: item[1], reverse=True))
    i = 0
    for word in sorted_dict:
        count = sorted_dict[word]
        if i > 10:
            break
        i = i + 1
        print("%s\t%i" % (word, count))
