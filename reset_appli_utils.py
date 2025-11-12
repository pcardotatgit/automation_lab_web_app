import glob
import os
from crayons import *

ok_delete=1

                
def delete_files_in_profiles():
    print()
    print(yellow('def delete_files_in_profiles() : >',bold=True))
    print()
    file_list=glob.glob("./profiles/*.txt")
    for fichier in file_list:
        fichier=fichier.replace('\\','/')        
        if os.path.exists(fichier):
            print(' ok delete ',fichier)
            if ok_delete:
                os.remove(fichier)  
                print(green(f' ==> Done : {fichier}',bold=True))
                
                
def delete_notes_in_dtree():
    print()
    print(yellow('def delete_notes_in_dtree() : >',bold=True))
    print()
    file_list=glob.glob("./dtree/note_*.txt")
    for fichier in file_list:
        fichier=fichier.replace('\\','/')        
        if os.path.exists(fichier):
            print(' ok delete ',fichier)
            if ok_delete:
                os.remove(fichier)  
                print(green(f' ==> Done : {fichier}',bold=True))
    with open("./dtree/index.html '","w") as file:
        file.write('ok')
        
def delete_misc_files():
    print()
    print(yellow('def delete_misc_files() : >',bold=True))
    print()     
    fichier="./template/z_sightings_id_list_w_titles.txt"
    if os.path.exists(fichier):
        print(' ok delete ',fichier)
        if ok_delete:
            os.remove(fichier)  
            print(green(f' ==> Done : {fichier}',bold=True))
        
def clean_keys():
    print()
    print(yellow('def clean_keys() : >',bold=True))
    print()
    new_config='''{
profil_name=xxx
ctr_client_id=client-xxx
ctr_client_password=xxxx
host=https://private.intel.eu.amp.cisco.com
host_for_token=https://visibility.eu.amp.cisco.com
}
'''
    with open("./keys/config.txt","w") as file:
        file.write(new_config)
        
                
def delete_files_in_result():
    print()
    print(yellow('def delete_files_in_result() : >',bold=True))
    print()
    file_list=glob.glob("./result/*.*")
    for fichier in file_list:
        fichier=fichier.replace('\\','/')        
        if os.path.exists(fichier):
            print(' ok delete ',fichier)
            if ok_delete:
                os.remove(fichier)  
                print(green(f' ==> Done : {fichier}',bold=True))
    with open('./result/home_url.txt','w') as file:
        file.write('/page_info?page=home.html&route=/')

def delete_files_in_code_app_functions():
    print()
    print(yellow('def delete_files_in_code_app_functions() : >',bold=True))
    print()
    file_list=glob.glob("./code_app_functions/*.*")
    for fichier in file_list:
        fichier=fichier.replace('\\','/')        
        if os.path.exists(fichier):
            print(' ok delete ',fichier)
            if ok_delete:
                os.remove(fichier)  
                print(green(f' ==> Done : {fichier}',bold=True))
            
def delete_files_in_code_app_html_templates():
    print()
    print(yellow('def delete_files_in_code_app_html_templates() : >',bold=True))
    print()
    file_list=glob.glob("./code_app_html_templates/*.*")
    for fichier in file_list:
        fichier=fichier.replace('\\','/')        
        if os.path.exists(fichier):
            print(' ok delete ',fichier)
            if ok_delete:
                os.remove(fichier)  
                print(green(f' ==> Done : {fichier}',bold=True))
                
def delete_files_in_code_app_routes():
    print()
    print(yellow('def delete_files_in_code_app_routes() : >',bold=True))
    print()
    file_list=glob.glob("./code_app_routes/*.*")
    for fichier in file_list:
        fichier=fichier.replace('\\','/')        
        if os.path.exists(fichier):
            print(' ok delete ',fichier)
            if ok_delete:
                os.remove(fichier)  
                print(green(f' ==> Done : {fichier}',bold=True))
                
def delete_files_in_templates():
    print()
    print(yellow('def delete_files_in_templates() : >',bold=True))
    print()
    file_list=glob.glob("./templates/*.*")
    for fichier in file_list:
        fichier=fichier.replace('\\','/')        
        if os.path.exists(fichier):
            print(' ok delete ',fichier)
            if ok_delete:
                os.remove(fichier)  
                print(green(f' ==> Done : {fichier}',bold=True))

def delete_files_in_code_backup():
    print()
    print(yellow('def delete_files_in_code_backup() : >',bold=True))
    print()
    file_list=glob.glob("./code_backup/*.*")
    for fichier in file_list:
        fichier=fichier.replace('\\','/')        
        if os.path.exists(fichier):
            print(' ok delete ',fichier)
            if ok_delete:
                os.remove(fichier)  
                print(green(f' ==> Done : {fichier}',bold=True))
                
def reset_code_architecture():
    print()
    print(yellow('def reset_code_architecture() : >',bold=True))
    print()
    with open('./code_architecture/app_functions.txt','w') as file:
        file.write('def_parse_config.py\n')
        print('ok')
    with open('./code_architecture/app_routes.txt','w') as file:
        file.write('route_def_index.py\n')    
        file.write('route_def_check_connexion_to_tenant.py\n')         
    with open('./code_architecture/imported_scripts.txt','w') as file:
        #file.write('') 
        print('ok')        
    with open('./code_architecture/main_html.txt','w') as file:
        #file.write('')  
        print('ok')        
    # copy route_def_index.py into ./code_app_route  because this is the landing page ( the application starts here ) and we are supposed to be able to modify it,then it is declared into the app routes
    with open('./code_system_routes/route_def_index.py') as file:
        text_content=file.read()  
    with open('./code_app_routes/route_def_index.py','w') as file:
        file.write(text_content)    
    # copy route_def_check_connexion_to_tenant.py into ./code_app_route  because we want to be able to modify it,then we declare it into the app routes
    with open('./code_system_routes/route_def_check_connexion_to_tenant.py') as file:
        text_content=file.read()  
    with open('./code_app_routes/route_def_check_connexion_to_tenant.py','w') as file:
        file.write(text_content)      
    # copy def_parse_config.py into ./code_app_function  because we want to be able to modify it,then it is declare it into the app functions
    with open('./code_system_functions/def_parse_config.py') as file:
        text_content=file.read()  
    with open('./code_app_functions/def_parse_config.py','w') as file:
        file.write(text_content)            
    # copy home.html to app index.html
    with open('./code_system_html_templates/home.html') as file:
        text_content=file.read()  
    with open('./code_app_html_templates/index.html','w') as file:
        file.write(text_content)    

def init_appli():
    with open('./venv/Scripts/activate.bat','w') as file:
        line_out='''@echo off

rem This file is UTF-8 encoded, so we need to update the current code page while executing it
for /f "tokens=2 delims=:." %%a in ('"%SystemRoot%\System32\chcp.com"') do (
    set _OLD_CODEPAGE=%%a
)
if defined _OLD_CODEPAGE (
    "%SystemRoot%\System32\chcp.com" 65001 > nul
)

set VIRTUAL_ENV=C:\patrick\Python_DEV\current_dev\python\z_poc_simplification\venv

if not defined PROMPT set PROMPT=$P$G

if defined _OLD_VIRTUAL_PROMPT set PROMPT=%_OLD_VIRTUAL_PROMPT%
if defined _OLD_VIRTUAL_PYTHONHOME set PYTHONHOME=%_OLD_VIRTUAL_PYTHONHOME%

set _OLD_VIRTUAL_PROMPT=%PROMPT%
set PROMPT=(venv) %PROMPT%

if defined PYTHONHOME set _OLD_VIRTUAL_PYTHONHOME=%PYTHONHOME%
set PYTHONHOME=

if defined _OLD_VIRTUAL_PATH set PATH=%_OLD_VIRTUAL_PATH%
if not defined _OLD_VIRTUAL_PATH set _OLD_VIRTUAL_PATH=%PATH%

set PATH=%VIRTUAL_ENV%\Scripts;%PATH%
set VIRTUAL_ENV_PROMPT=(venv) 
python compile.py
:END
if defined _OLD_CODEPAGE (
    "%SystemRoot%\System32\chcp.com" %_OLD_CODEPAGE% > nul
    set _OLD_CODEPAGE=
)

        '''
        file.write(line_out)    
    os.remove("a.bat")
    os.remove("b.bat")
    os.remove("c.bat")
    os.remove("d.bat")
    with open('a.bat','w') as file:
        file.write('venv\\scripts\\activate')    
    with open('b.bat','w') as file:
        file.write('python compile.py')       
                
if __name__=="__main__":
    delete_notes_in_dtree()
    delete_files_in_result()
    delete_files_in_code_backup()
    delete_files_in_code_app_functions()
    delete_files_in_code_app_html_templates()
    delete_files_in_code_app_routes()
    delete_files_in_templates()
    reset_code_architecture()
    clean_keys()
    delete_misc_files()
    print()
    a=input('DELETE Profiles ? YES or anything else: ')
    if a=="YES":
        delete_files_in_profiles()