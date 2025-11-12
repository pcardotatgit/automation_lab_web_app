#  def_list_files_in_sub_folder***
def list_files_in_sub_folder():
    '''
    MODIFIED : 2025-09-13T09:38:16.000Z
    description : list every image files into the ./input_images sub folder, extract QR codes and save them in resylt.txt in  ./output sub dir
    
    how to call it :
    '''
    route="/list_files_in_sub_folder"
    env.level+='-'
    print('\n'+env.level,white('def list_files_in_sub_folder() in app.py  : >\n',bold=True))
    loguer(env.level+' def list_files_in_sub_folder() in app.py  : > ')
    # ===================================================================    
    file_list0=glob.glob("./input_images/*.*")
    file_list=[]
    for fichier in file_list0:
        fichier2="./input_images/"+fichier.split('\\')[1]
        print(fichier2)
    # ===================================================================
    loguer(env.level+' def END OF list_files_in_sub_folder() in app.py  : > ')
    env.level=env.level[:-1]
    return 1
    

