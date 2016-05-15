from __future__ import print_function

import sys
from operator import add

from pyspark import SparkContext


if __name__ == "__main__":
    
    day = list()
    sc = SparkContext()
    data = sc.textFile(sys.argv[1])
    transactions = data.map(lambda line: line.strip().split(','))
      
    results = transactions.collect()

    if line[5] and line[6]!=0:
	    for line in results[1:]:
	        date,time = line[1].strip().split(' ')
			date = str(date)
			date = date.replace('-','').strip("'")
			time = time.split(':')	
			del line[0]
	        del line[1:3]
	        del line[2:15]
	        line[0] = int(date)
	        line[1] = float(line[1])
	        line[2] = float(line[2])
	        #print ("%d %s:00:00,%.2f" % (line[0],str(time[0]),line[1]))
	        print ("%d %s:00:00" % (line[0],str(time[0])))

    sc.stop()
