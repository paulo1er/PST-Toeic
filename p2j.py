
from pdf2jpg import pdf2jpg

inputpath = r"Toeic_scan.pdf"
outputpath = r"Img"


result = pdf2jpg.convert_pdf2jpg(inputpath, outputpath, pages="ALL")
print(result)