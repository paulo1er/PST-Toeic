from tkFileDialog import *

def interface(string):
    filepath = askopenfilename(title=string,filetypes=[('pdf files', '.pdf')])
    return(filepath)

#print(interface())
