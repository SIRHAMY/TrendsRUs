import csv

class HousingDataParser(object):


    def __init__(self):
        self.csvFileName = "ZipCodeMedianHousingPrices.csv"



    def getZipCodePriceTuples(self):
        with open(self.csvFileName, "rb") as csvfile:
            reader = csv.reader(csvfile)

            print reader.next()







if __name__ == "__main__":
    parser = HousingDataParser()

    parser.getZipCodePriceTuples()



