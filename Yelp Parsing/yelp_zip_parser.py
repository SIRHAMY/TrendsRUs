#<-- Thomas Barnes -->
import json, urllib2

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
		strzip = str(restaurantList[i]['zip'])
		jumble = urllib2.urlopen('http://www.zip-info.com/cgi-local/zipsrch.exe?cnty=cnty&zip='+strzip+'&Go=Go').read()
		#for i in range(0,30):
		ind = jumble.find("<td align=center>"+strzip)
		newjumble = jumble[ind+51:]
		ind = newjumble.find("</font>")
		county = newjumble[0:ind]
		if len(county) > 30:
			county = None
		stars_dict[str(restaurantList[i]['zip'])] = [restaurantList[i]['stars'], 1, restaurantList[i]['stars'], county]


with open('yelp_zip_codes_info.json','w') as outfile:
	json.dump(restaurantList, outfile)
with open('yelp_avg_rating_by_zip.json','w') as outfile:
	json.dump(stars_dict, outfile)