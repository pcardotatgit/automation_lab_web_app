# def_list_files_in_temp***
def list_files_in_temp():
    env.level+='-'
    print()
    print(env.level,white('def list_files_in_temp() : >',bold=True))
    loguer(env.level+' def list_files_in_temp() : >')
    print()
    file_list0=glob.glob("./temp/*.txt")
    file_list=[]
    for fichier in file_list0:
        fichier2=fichier.split('\\')[1]
        #file_list.append(fichier.replace('\\','/'))
        file_list.append(fichier2)
    env.level=env.level[:-1]
    return(file_list)
     

