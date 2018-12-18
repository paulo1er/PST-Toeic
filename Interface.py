from tkFileDialog import *

def interface():
    filepath = askopenfilename(title="Choisir le pdf",filetypes=[('pdf files', '.pdf')])
    return(filepath)

#print(interface())
