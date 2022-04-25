#!/usr/bin/env python3
"""mapper.py"""

import sys

for line in sys.stdin:
    line = line.strip()
    columns = line.split(',')
    try:
        userId = columns[2]
        productId = columns[1]
        score = int(columns[4])
        if score >= 4:
            print('%s\t%s' % (userId, productId))
    except ValueError:
        pass
