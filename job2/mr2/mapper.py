#!/usr/bin/env python3
"""mapper.py"""

import sys

for line in sys.stdin:
    line = line.strip()
    columns = line.split(',')
    try:
        userId = columns[2]
        productId = columns[1]
        score = columns[4]
        print('%s\t%s\t%s' % (userId, productId, score))
    except ValueError:
        pass
