#<-- Thomas Barnes -->
import json

restaurantList = []
with open('yelp_academic_dataset_business.json') as f:
	for line in f:
		data = json.loads(line)
		zip_code = data['full_address'][::-1][0:5][::-1]
		try:
			zip_code = int(zip_code)
		except:
			continue
		restaurant = {}
		restaurant['name'] = data['name']
		restaurant['zip'] = zip_code
		restaurant['latitude'] = float(data['latitude'])
		restaurant['longitude'] = float(data['longitude'])
		restaurant['stars'] = float(data['stars'])
		restaurantList.append(restaurant)

#print tally, total, float(tally)/total * 100
'''for i in range(0,len(restaurantList)):
	if restaurantList[i]['zip'] == 85009:
		print restaurantList[i]'''

stars_dict = {}
for i in range(0,len(restaurantList)):
	try:
		temp = stars_dict[str(restaurantList[i]['zip'])]
		temp[0] += restaurantList[i]['stars']
		temp[1] += 1
		temp[2] = round(float(temp[0]) / temp[1],3)
		stars_dict[str(restaurantList[i]['zip'])] = temp
	except:
		stars_dict[str(restaurantList[i]['zip'])] = [restaurantList[i]['stars'], 1, restaurantList[i]['stars']]
with open('yelp_zip_codes_info.json','w') as outfile:
	json.dump(restaurantList, outfile)
with open('yelp_avg_rating_by_zip.json','w') as outfile:
	json.dump(stars_dict, outfile)