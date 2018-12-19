import csv

class TfList:

    @staticmethod
    def createFile(fileName):
        csvFile =  open(fileName, "w")
        csvWriter = csv.writer(csvFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        return csvWriter


