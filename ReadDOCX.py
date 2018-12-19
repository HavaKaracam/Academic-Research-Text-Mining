from idlelib.iomenu import encoding

from docx.shared import Pt
from docx import Document
from pip._internal.utils import encoding

newDoc = Document("osreport.docx")
newDoc.save("newww.docx")
newTxt = open("asd.txt", "w")
for para in newDoc.paragraphs:
    print(para.text)
    newTxt.write(para.text)
