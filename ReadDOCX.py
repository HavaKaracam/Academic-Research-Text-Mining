from docx import Document


class ReadDOCX:

    @staticmethod
    def converToTxt(docName):
        newDoc = Document(docName)
        asd = docName
        for x in range(len(docName)):
            if x == ".":
                asd = docName[0:x]
        newTxt = open(str(asd) + ".txt", "w")
        for para in newDoc.paragraphs:
            newTxt.write(para.text)
        newTxt.close()
        newTxt = open(str(asd) + ".txt", "r")
        return newTxt