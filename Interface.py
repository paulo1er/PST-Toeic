import tkFileDialog



def interface(string):
    #pour cacher l'autre fenetre
    #root = Tkinter.Tk()
    #root.withdraw()
    
    filepath = tkFileDialog.askopenfilename(title=string,filetypes=[('pdf files', '.pdf')])
    return(filepath)



if __name__ == '__main__':
    a=interface("test")
    print(a)
