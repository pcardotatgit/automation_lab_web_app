'''
    versoin : 20250930
    create the external python script seleted into ./result/selected_script.txt only
'''
# a_core_imports.py***
from crayons import *
import os
from datetime import datetime, timedelta
import shutil
import glob
import sys
import env as env

dateTime = datetime.now()
    
def create_scripts(filename,workingdir):
    env.level+='-'
    print()
    print(env.level,white('def create_scripts() : >',bold=True))
    workingdir=workingdir.replace('\\','/')
    print()
    print('workingdir : ',workingdir)
    print()    
    if filename!="":
        print()
        print('imported script to create : ',filename)
        print()
        scriptdir='./code_app_scripts_to_import/'+filename.replace('.py','')+'/'    
        lines_out=''            
        with open(scriptdir+'a_header.txt') as file:
            text_content=file.read()+'\n'
        lines_out=lines_out+text_content
        with open(scriptdir+'a_imports.txt') as file:
            text_content=file.read()+'\n'
        lines_out=lines_out+text_content        
        with open(scriptdir+'a_global_variables.txt') as file:
            text_content=file.read()+'\n'
        lines_out=lines_out+text_content 
        # ADD Script functions here under
        print(yellow('\nADD Script functions here under,',bold=True))        
        with open(scriptdir+'script_functions.txt') as file2:
            text_content=file2.read()
        text_content=text_content.replace(' ','')
        print('script list : \n',yellow(text_content,bold=True))
        print()   
        scripts=text_content.split('\n')
        print('scripts : \n',yellow(scripts,bold=True))
        print()             
        for script in scripts:
            if script!='':
                print('script : \n',yellow(scriptdir+script,bold=True))
                print()            
                with open(scriptdir+script) as file3:
                    text_content=file3.read()+'\n'                    
                lines_out=lines_out+text_content    
        # Add Script route here under
        print(yellow('\nAdd Script route here under ,',bold=True))
        with open(scriptdir+'script_routes.txt') as file2:
            text_content=file2.read()
        text_content=text_content.replace(' ','')
        print('script list : \n',yellow(text_content,bold=True))
        print()   
        scripts=text_content.split('\n')
        print('scripts : \n',yellow(scripts,bold=True))
        print()             
        for script in scripts:
            if script!='':
                print('script : \n',yellow(scriptdir+script,bold=True))
                print()            
                with open(scriptdir+script) as file3:
                    text_content=file3.read()+'\n'                    
                lines_out=lines_out+text_content                          
        with open(scriptdir+'a_main.txt') as file:
            text_content=file.read()+'\n'
        lines_out=lines_out+text_content            
        # create the script
        with open(workingdir+'/'+filename,'w') as file4:
            file4.write(lines_out)
        fichier=workingdir+'/env.py'
        if os.path.exists(fichier):
            print(' Create env.py',fichier)
            with open(fichier,'w') as file4:
                file4.write('level="["')         
    print()
    env.level=env.level[:-1]
    return 1
    
# a_core_main.py***
if __name__ == "__main__":
    print()    
    print(cyan('CREATE EXTERNAL SCRIPT : >',bold=True)) 
    with open('./result/selected_script.txt') as file:
        filename=file.read()
    with open('./result/selected_script_working_dir.txt') as file:
        workingdir=file.read()        
    print()
    print(cyan(f'Script to create : {filename}',bold=True))
    print()
    print()
    print(cyan(f'In workingdir : {workingdir}',bold=True))
    print()    
    create_scripts(filename,workingdir)
    print()
    print(cyan('OK DONE script was builted : >',bold=True))
    print()   
    '''
    print(cyan('Now let\' start the app : >',bold=True))
    print()      
    os.system("python app.py 1")    
    '''