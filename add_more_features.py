def add_more_features(attribute_list):
	enhanced_list=[]

	num_taxi = attribute_list[len(attribute_list)-1]
	num_uber = attribute_list[len(attribute_list)-2]

	temp_max = attribute_list[3]
	temp_min = attribute_list[4]
	prcp = attribute_list[1]
	snow = attribute_list[5]

	#New attributes

	temp_avg = (temp_max + temp_min)/2
	rain_flag = 0
	snow_flag = 0
	if (prcp > 0):
		rain_flag = 1
	if (snow > 0):
		snow_flag = 1 	

	for i in range(0, len(attribute_list)-2):
		enhanced_list.append(attribute_list[i])

	enhanced_list.append(temp_avg)
	enhanced_list.append(rain_flag)
	enhanced_list.append(snow_flag)
	enhanced_list.append(num_uber)
	enhanced_list.append(num_taxi)
	return enhanced_list

new_list = add_more_features([20150630.0, 0.04, 0.0, 82.0, 68.0, 0.0, 4.92, 170.0, 170.0, 14.1, 25.1, 1.0, 22.0, 5749.0, 22815.0])
print new_list