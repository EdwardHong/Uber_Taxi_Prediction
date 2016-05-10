#!/usr/bin/env python

import sys
import csv
import StringIO
# input comes from STDIN (standard input)
for line in sys.stdin:
# remove leading and trailing whitespace
	line = line.strip()
	csv_file = StringIO.StringIO(line)
	csv_reader = csv.reader(csv_file)
	for record in csv_reader:
	# split the line into words
		data = line.split(',')
		date_time = record[1]

		if (date_time!="Pickup_date"):
			date_time = date_time.split(' ')
			
			date = date_time[0]
			month_day_year = date.split('-')

			year = month_day_year[0]
			month = month_day_year[1]
			day = month_day_year[2]
			month = "{0:0>2}".format(month)
			day = "{0:0>2}".format(day)
			y = [year,month,day]
			date_formatted = ''.join(str(e) for e in y)

			time = date_time[1]
			hour_minute_second = time.split(':')
			hour = hour_minute_second[0]
			hour = "{0:0>2}".format(hour)
			minute = "00"
			second = "00"
			t = [hour,minute,second]
			time_formatted = ':'.join(str(e) for e in t)


			date_time_formatted = date_formatted + " " + time_formatted


			print ("%s\t%s"%(date_time_formatted,1))