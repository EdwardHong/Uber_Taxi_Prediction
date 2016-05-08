#!/usr/bin/python
import sys
import re
import numpy as np

table1 = []
table2 = []
d = {}
#input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    line = line.strip()
    key,val=line.split('\t')
    val = val.strip()
    key =  key.strip()
    val = val.split(',')
    #x = [n.strip() for n in val]

    if key not in d:
        d[key] = val
    else:
        val = d[key] + val
    val = ','.join(val)
    print("%s\t%s" %(key,val))

