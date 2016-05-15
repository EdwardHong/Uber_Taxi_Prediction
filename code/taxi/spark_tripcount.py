#####################################################
# run the numtrip.py before running this spark file #
#													#
#####################################################

from __future__ import print_function
import sys
from operator import add

from pyspark import SparkContext


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: wordcount <file>", file=sys.stderr)
        exit(-1)
    sc = SparkContext(appName="PythonWordCount")
    lines = sc.textFile(sys.argv[1])
    counts = lines.map(lambda x: (x, 1)).reduceByKey(add)
    output = counts.collect()
    for (word, count) in output:
        print("%s: %i" % (word.encode('utf-8'), count))

    sc.stop()



# text_file = sc.textFile(sys.argv[1])
# counts = text_file.map(lambda word: (word.encode('utf-8'), 1)).reduceByKey(lambda a, b: a + b)
# counts.saveAsTextFile("test")
