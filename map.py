
import sys
import csv
import StringIO

#input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    line = line.rstrip()
    csv_file = StringIO.StringIO(line)
    csv_reader = csv.reader(csv_file)
    for record in csv_reader:
        if len(record) == 91:
            key = record[5]
            s = [record[11],
            record[31],
            record[36],
            record[16],
            record[41],
            record[46],
            record[51],
            record[56],
            record[61],
            record[66]]
            val = ", ".join(str(e) for e in s)
            
        

            print ("%s\t%s"%(key, val))
    
