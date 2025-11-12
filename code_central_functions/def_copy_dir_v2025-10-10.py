#  def_copy_dir***
def copy_dir(src_directory,dst_directory,file_types):
    '''
    MODIFIED : 2025-09-28T06:44:45.000Z

    description : copy a director to another directory
    
    how to call it : copy_dir(src_directory,dst_directory,file_types) 
        file_types : ex : *.*  or *.txt
    '''
    route="/copy_dir"
    env.level+='-'
    print('\n'+env.level,white('def copy_dir() in app.py  : >\n',bold=True))
    loguer(env.level+' def copy_dir() in app.py  : > ')
    # ===================================================================    
    print('dst_directory in backup folder',yellow(dst_directory,bold=True))
    print('Directory to backup ;',yellow(src_directory,bold=True))
    if './' not in dst_directory:
        dst_directory='./'+dst_directory
    os.mkdir(dst_directory)
    file_list0=glob.glob("./"+src_directory+"/"+file_types)
    file_list=[]
    for fichier in file_list0:
        fichier2=fichier.split('\\')[1]
        fichier2=fichier2.strip()
        print(fichier2)
        if './' not in src_directory:
            src='./'+src_directory+'/'+fichier2
        else:
            src=src_directory+'/'+fichier2
        print('src :',cyan(src,bold=True))        
        dst=dst_directory+'/'+fichier2
        print('dst :',red(dst,bold=True))        
        if fichier2!='':
            shutil.copyfile(src, dst)
    # ===================================================================
    loguer(env.level+' def END OF copy_dir() in app.py  : > ')
    env.level=env.level[:-1]
    return 1
    

