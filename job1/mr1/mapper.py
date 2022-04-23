#!/usr/bin/python3
"""mapper.py"""

import sys
from datetime import datetime
for line in sys.stdin:
    line = line.strip("\\n")
    line = line.replace("\\n", "")
    columns = line.split(',')
    try:
        unixdate = columns[6]
        unixdate = unixdate.strip("\\n")
        unixdate = unixdate.replace("\\n", "")
        year = datetime.utcfromtimestamp(int(unixdate)).strftime('%Y')
        text = columns[7].split(" ")
        if len(text) >= 10:
            for word in text:
                word = word.strip("\\n")
                word = word.replace("\\n", "")
                print('%s\t%s' % (year, word))
    except ValueError:
        pass

