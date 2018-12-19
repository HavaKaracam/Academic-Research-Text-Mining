import csv

class TfList:

    @staticmethod
    def createFile(fileName):
        csvFile =  open(fileName, "w")
        return csvFile


