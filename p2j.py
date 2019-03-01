
from pdf2image import convert_from_path
import os


def pdf2image(inputPath):
    directory = "run"
    if not os.path.exists(directory):
        os.makedirs(directory)

    pages = convert_from_path(inputPath, 200)

    i=0
    for page in pages:
        page.save(directory+'/out'+str(i)+'.jpg', 'JPEG')
        i += 1
    return i

#pdf2image("Toeic_scan.pdf")
