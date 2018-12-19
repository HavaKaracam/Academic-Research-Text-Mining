class ReadTXT:

    @staticmethod
    def readTxt(txtName):
        txtFile = open(str(txtName), "r")
        return txtFile
