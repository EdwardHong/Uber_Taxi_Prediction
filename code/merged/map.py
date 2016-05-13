
import sys
import csv
import StringIO
'''
0 STATION
1 STATION_NAME
2 DATE
3 PRCP
4 SNWD
5 SNOW
6 TMAX
7 TMIN
8 AWND
9 WDF2
10 WDF5
11 WSF2
12 WSF5
13 WT01
14 WT06
15 WT02
16 WT04
17 WT08
['DATE', 'PRCP', 'SNWD', 'TMAX', 'TMIN', 'SNOW',
                     'AWND', 'WDF2', 'WDF5', 'WSF2', 'WSF5', 'WT01', 'HOUR',
'''
#input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    line = line.rstrip()
    csv_file = StringIO.StringIO(line)
    csv_reader = csv.reader(csv_file)
    for record in csv_reader:
        if len(record) == 91:
            key = record[5]
            s = [record[6],
            record[11],
            record[31],
            record[36],
            record[16],
            record[41],
            record[46],
            record[51],
            record[56],
            record[61],
            record[66]]
        elif len(record)==3:
            key = record[0]
            s = [record[1].split(":")[0],record[2]]
        elif len(record) == 18:
            key = record[2]
            s = [
            record[3],
            record[4],

            record[6],
            record[7],
            record[5],
            record[8],
            record[9],
            record[10],
            record[12],
            record[13]]
        val = ", ".join(str(e) for e in s)
        print ("%s\t%s"%(key, val))
