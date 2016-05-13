#!/usr/bin/python
import sys
import re
import numpy as np

table1 = []
table2 = []
d = {}
# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    line = line.strip()
    key, val = line.split('\t')
    val = val.strip()
    key = key.strip()
    val = val.split(',')

    key = (key, val[-2])
    val.pop(-2)

    if key not in d:
        d[key] = val
    else:
        newVal = d[key]
        newKey = key[0]
        val = [key[1]] + val + newVal
        val = ','.join(val)
        print("%s\t%s" % (newKey, val))
