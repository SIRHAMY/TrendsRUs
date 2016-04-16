import sys
import json
from datetime import datetime


FULL_JSON_FILE_NAME = "Json/CountyMedianHousingPrices.json"


PRICE_THRESHOLD = 350000

with open(FULL_JSON_FILE_NAME) as f:
    json_data = json.loads(f.read())

    filtered_data = [x for x in json_data if x['median_price'] <= PRICE_THRESHOLD and x['state'] == 'GA']




time =  datetime.now().strftime('%H-%M-%S')

with open("Json/FilterResult-"+time+".json", "w") as json_file:
    json_file.write(json.dumps(filtered_data, sort_keys = True, indent = 4))







