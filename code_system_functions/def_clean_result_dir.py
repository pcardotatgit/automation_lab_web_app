# def_clean_result_dir***
def clean_result_dir(dirPath):
    env.level+='-'
    print()
    print(env.level,white('def clean_result_dir() : >',bold=True))
    loguer(env.level+' def clean_result_dir() : >')
    print()
    files =[file for file in os.listdir(dirPath)]
    for file in files:
        print("file to delete : ",file)
        os.remove(dirPath+"/"+file)
    env.level=env.level[:-1]
    return 1

