#  def_list_pdf_files***
def list_pdf_files():
    '''
    MODIFIED : 2025-06-07T08:49:50.000Z

    description : list pdfs files into the PDFs subfolder
    '''
    route="/list_pdf_files"
    env.level+='-'
    print()
    print(env.level,white('def list_pdf_files() in app.py  : >\n',bold=True))
    print()
    pdfFiles = [] # list of PDF files

    file_list=glob.glob("./PDFs/*.pdf")
    for fichier in file_list:
        #fichier=fichier.replace('\\','/')
        fichier=fichier.replace('./','.\\')  
        print()
        print('fichier :',white(fichier,bold=True))
        print()        
        pdfFiles.append(fichier)

    # Sorting the files by forcing everything to lower case.
    pdfFiles.sort(key=str.lower)

    print()
    print('pdfFiles : \n',cyan(pdfFiles,bold=True))
    env.level=env.level[:-1]
    return pdfFiles
    

