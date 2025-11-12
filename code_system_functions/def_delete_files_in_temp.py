# def_delete_files_in_temp***
def delete_files_in_temp():
    env.level+='-'
    print()
    print(env.level,white('def delete_files_in_temp() : >',bold=True))
    loguer(env.level+' def delete_files_in_temp() : >')
    print()
    file_list=glob.glob("./temp/*.txt")
    for fichier in file_list:
        fichier=fichier.replace('\\','/')        
        if os.path.exists(fichier):
            print(' ok delete ',fichier)
            os.remove(fichier)    
    env.level=env.level[:-1]
    return 1


