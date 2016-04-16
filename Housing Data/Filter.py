import sys
import json
from datetime import datetime


FULL_JSON_FILE_NAME = "Json/MedianHousingPrices.json"


PRICE_THRESHOLD = 350000

with open(FULL_JSON_FILE_NAME) as f:
    json_data = json.loads(f.read())

    filtered_data = [x for x in json_data if x['median_price'] <= PRICE_THRESHOLD]




time =  datetime.now().strftime('%H-%M-%S')

with open("Json/FilterResult-"+time+".json", "w") as json_file:
    json_file.write(json.dumps(filtered_data))







