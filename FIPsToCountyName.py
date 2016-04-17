import csv
import json

class CSVFetcher():
    def __init__(self, fileName):
        self.fileName = fileName + '.csv'


    def fetch(self):
        print("fetcher.fetch")
        with open(self.fileName, 'rb') as f:
            reader = csv.reader(f)
            for line in reader:
                yield line

if __name__ == "__main__":

	fipsCodeReader = CSVFetcher("/resources/fipscounty.csv");
	fipsCodes = {}

	#Place fipsCodes in dict
	for row in fipsCodeReader.fetch():
		rowArray = row.split(",");

		fipsCodes[str(rowArray[1]) + str(rowArray[2])] = rowArray[3]

	#Compare county codes with fips
	rawJson = json.load("/resources/USCounties.json")
	for county in rawJson['counties']:
		