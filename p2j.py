
from pdf2image import convert_from_path
import os
import shutil
from PyPDF2 import PdfFileWriter, PdfFileReader


def splitPdf(inputPath):
    inputpdf = PdfFileReader(open(inputPath, "rb"))
    nbPages=inputpdf.numPages
    for i in range(nbPages):
        output = PdfFileWriter()
        output.addPage(inputpdf.getPage(i))
        with open("run\document-page%s.pdf" % i, "wb") as outputStream:
            output.write(outputStream)
    return nbPages



def pageToImage(directory,i):
    path = directory + "\document-page%s.pdf" % i
    pages = convert_from_path(path, 200)

    pathOut = directory + "\out%s.jpg" % i
    pages[0].save(pathOut, 'JPEG')
    os.remove(directory + "\document-page%s.pdf" % i)
    return 0



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


if __name__ == '__main__':
    
    """
    import cProfile
    pr = cProfile.Profile()
    pr.enable()
    """
    pdf2image("Scan test\Toeic Test 3.pdf")#"Scan test\merged 252.pdf"
    """
    pr.disable()
    pr.print_stats(sort='cumtime')
    """

