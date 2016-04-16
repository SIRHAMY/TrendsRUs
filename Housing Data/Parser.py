import csv
import json

class HousingDataParser(object):


    def __init__(self):
        self.csvFileName = "ZipCodeMedianHousingPrices.csv"



    def getZipCodePriceTuples(self):
        with open(self.csvFileName, "rb") as csvfile:
            reader = csv.reader(csvfile)

            fields = list(reader.next())   #store column names
            yearIndexStart = fields.index("1996-04")    #This is the first year data is available

            data = []
            f=1
            for row in reader:
                zip_code = row[fields.index("ZipCode")]
                prices = row[yearIndexStart:]      #grabs all price rows (even empty ones)
                nonEmptyYearsAndPrices = [(fields[i+yearIndexStart],p) for i,p in enumerate(prices) if p]  #filter out any data where there is no price for a given year
                mostRecentYear, mostRecentPrice = nonEmptyYearsAndPrices[-1]        

                year, month = self._parseYearString(mostRecentYear)
                 
                data.append({
                    "zip_code" : int(zip_code),
                    "median_price" : float(mostRecentPrice), 
                    "year" : year, 
                    "month": month})


        return data

 
    

    def getJSONFormatString(self, data):
        return json.dumps(data, sort_keys = True, indent = 4)


    def _parseYearString(self, year_string):
        year_str, month_str = year_string.split('-')
        return (int(year_str), int(month_str))


    


if __name__ == "__main__":
    parser = HousingDataParser()

    data = parser.getZipCodePriceTuples()

    json_data = parser.getJSONFormatString(data)

    with open("MedianHousingPrices.json", "w") as f:
        f.write(json_data)
        


