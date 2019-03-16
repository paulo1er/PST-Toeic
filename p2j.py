

import os
import shutil
from pdf2image import convert_from_path
from PyPDF2 import PdfFileWriter, PdfFileReader


"""
This file contains functions to extract the pdf into multiple jpg images

"""


# split the pdf into multiple 1-page pdfs
def splitPdf(inputPath):
    inputpdf = PdfFileReader(open(inputPath, "rb"))
    nbPages=inputpdf.numPages
    for i in range(nbPages):
        output = PdfFileWriter()
        output.addPage(inputpdf.getPage(i))
        with open("run\document-page%s.pdf" % i, "wb") as outputStream:
            output.write(outputStream)
    return nbPages


# transforms a 1-page pdf into a jpg image and delete the pdf
def pageToImage(directory,i):
    path = directory + "\document-page%s.pdf" % i
    pages = convert_from_path(path, 200)

    pathOut = directory + "\out%s.jpg" % i
    pages[0].save(pathOut, 'JPEG')
    os.remove(directory + "\document-page%s.pdf" % i)
    return 0


# main function : transforms a pdf into multiple jpg, saved in the "run" directory
def pdf2image(inputPath):
    directory = "run"
    try:
        shutil.rmtree(directory)
    except:
        print "aucun dossier run"
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    nbPages = splitPdf(inputPath)

    for i in range(nbPages):
        pageToImage(directory,i)
    return nbPages

# only for testing
if __name__ == '__main__':
    
    """
    import cProfile
    pr = cProfile.Profile()
    pr.enable()
    """
    pdf2image("Scan test\Toeic Test 3.pdf")
    """
    pr.disable()
    pr.print_stats(sort='cumtime')
    """

