# a_core_imports.py***
'''
    modified : 2025091329ate a package which is a complete backup of the application. It is ready to run
    how to call it : from a main  ptyhon script. run an external python script          os.system("backup_app_system_code.py 1") 
'''
from crayons import *
import os
from datetime import datetime, timedelta
import shutil
import glob
import sys
import env as env
import zipfile


dateTime = datetime.now()

# def_current_date_and_time***
def current_date_and_time():  
    env.level+='-'
    print()
    print(env.level,white('def current_date_and_time() : >',bold=True))
    print() 
    '''
        current time + nb days in the YYYYmmddHMSformat
    '''
    current_time = datetime.utcnow()
    timestampStr = current_time.strftime("%Y%m%d%H%M%S")
    env.level=env.level[:-1]
    return(timestampStr)  
    
def backup_code_imported_scripts(subdir):
    env.level+='-'
    print()
    print(env.level,white('def backup_imported_scripts() : >',bold=True))
    print()
    with open('./code_architecture/imported_scripts.txt') as file:
        text_content=file.read()
    directorys=text_content.split('\n')
    for directory in directorys:
        if directory!='':
            print('IMPORTED SCRIPT :',cyan(directory,bold=True))
            directory2=directory.replace('.py','')
            os.mkdir(subdir+"./code_app_scripts_to_import/"+directory2)             
            file_list0=glob.glob("./code_app_scripts_to_import/"+directory2+'/*.*')
            file_list=[]
            for fichier in file_list0:
                fichier2=fichier.split('\\')[1]
                print('file in sub directory',green(fichier2,bold=True))
                src="./code_app_scripts_to_import/"+directory2+"/"+fichier2
                dst=subdir+"/code_app_scripts_to_import/"+directory2+"/"+fichier2
                shutil.copyfile(src, dst)
    env.level=env.level[:-1]
    return 1
    
def backup_code_app_html_templates(subdir):
    env.level+='-'
    print()
    print(env.level,white('def backup_app_html_templates() : >',bold=True))
    print()
    file_list0=glob.glob("./code_app_html_templates/*.html")
    file_list=[]
    for fichier in file_list0:
        fichier2=fichier.split('\\')[1]
        print(fichier2)
        src='./code_app_html_templates/'+fichier2
        dst='./'+subdir+'/code_app_html_templates/'+fichier2
        shutil.copyfile(src, dst)
    env.level=env.level[:-1]
    return 1

def backup_code_app_routes(subdir):
    env.level+='-'
    print()
    print(env.level,white('def backup_code_app_routes() : >',bold=True))
    print()
    file_list0=glob.glob("./code_app_routes/*.py")
    file_list=[]
    for fichier in file_list0:
        fichier2=fichier.split('\\')[1]
        print(fichier2)
        src='./code_app_routes/'+fichier2
        dst='./'+subdir+'/code_app_routes/'+fichier2
        shutil.copyfile(src, dst)
    env.level=env.level[:-1]
    return 1

def backup_code_app_functions(subdir):
    env.level+='-'
    print()
    print(env.level,white('def backup_code_app_functions() : >',bold=True))
    print()
    file_list0=glob.glob("./code_app_functions/*.py")
    file_list=[]
    for fichier in file_list0:
        fichier2=fichier.split('\\')[1]
        print(fichier2)
        src='./code_app_functions/'+fichier2
        dst='./'+subdir+'/code_app_functions/'+fichier2
        shutil.copyfile(src, dst)
    env.level=env.level[:-1]
    return 1

def backup_code_architecture(subdir):
    env.level+='-'
    print()
    print(env.level,white('def backup_code_architecture() : >',bold=True))
    print()
    file_list0=glob.glob("./code_architecture/*.txt")
    file_list=[]
    for fichier in file_list0:
        fichier2=fichier.split('\\')[1]
        print(fichier2)
        src='./code_architecture/'+fichier2
        dst='./'+subdir+'/code_architecture/'+fichier2
        shutil.copyfile(src, dst)
    env.level=env.level[:-1]
    return 1
    
def backup_code(subdir,code_directory,file_types):
    env.level+='-'
    print()
    print(env.level,white('def backup_code() : >',bold=True))
    print('subdir in backup folder',yellow(subdir,bold=True))
    print('Directory to backup ;',yellow(subdir+'/'+code_directory,bold=True))
    os.mkdir(subdir+'/'+code_directory)
    file_list0=glob.glob("./"+code_directory+"/"+file_types)
    file_list=[]
    for fichier in file_list0:
        fichier2=fichier.split('\\')[1]
        fichier2=fichier2.strip()
        print(fichier2)
        src='.'+code_directory+'/'+fichier2
        print('src :',cyan(src,bold=True))        
        dst=subdir+'/'+code_directory+'/'+fichier2
        print('dst :',red(dst,bold=True))        
        if fichier2!='':
            shutil.copyfile(src, dst)
    env.level=env.level[:-1]
    return 1

def backup_application_package(subdir):     
    os.mkdir(subdir+'/code_backup')
    with open(subdir+'/code_backup/a_STORE_HERE_APPLICATION_BACKUP.txt','w') as file:
        pass     
    backup_code(subdir,'/code_central_functions','*.*')
    backup_code(subdir,'/code_central_routes','*.*')
    backup_code(subdir,'/code_snippets','*.*')    
    backup_code(subdir,'/code_system_functions','*.*')
    backup_code(subdir,'/code_system_html_templates','*.*')
    backup_code(subdir,'/code_system_main_blocs','*.*')  
    backup_code(subdir,'/code_system_routes','*.*') 
    backup_code(subdir,'/code_templates','*.*') 
    backup_code(subdir,'/debug','*.*') 
    with open(subdir+'/debug/log.txt','w') as file:
        pass        
    backup_code(subdir,'/dtree','*.*') 
    backup_code(subdir,'/dtree/img','*.*')     
    os.mkdir(subdir+'/result')       
    with open(subdir+'/result/current_edited_function.txt','w') as file:
        pass     
    with open(subdir+'/result/a_THIS_FOLDER_STORE_RESULTING_FILES_USED_BY_APP_SCRIPTS.txt','w') as file:
        pass        
    with open(subdir+'/result/current_edited_imported_script.txt','w') as file:
        pass        
    with open(subdir+'/result/current_edited_route.txt','w') as file:
        pass         
    with open(subdir+'/result/current_edited_script.txt','w') as file:
        pass       
    with open(subdir+'/result/function_list.txt','w') as file:
        pass     
    with open(subdir+'/result/selected_script.txt','w') as file:
        pass       
    with open(subdir+'/result/selected_script_working_dir.txt','w') as file:
        pass        
    os.mkdir(subdir+'/temp')     
    with open(subdir+'/temp/a_FOR_STORING_TEMP_FILES.txt','w') as file:
        pass     
    backup_code(subdir,'/code_projets','*.*')         
    backup_code(subdir,'/templates','*.*')        
    backup_code(subdir,'/templates/img','*.*')      
    backup_code(subdir,'/static','*.*')    
    backup_code(subdir,'/static/img','*.*')     
    backup_code(subdir,'/static/assets','*.*')   
    backup_code(subdir,'/static/assets/css','*.*')    
    backup_code(subdir,'/static/assets/css/images','*.*')     
    backup_code(subdir,'/static/assets/css/images/ie','*.*')    
    backup_code(subdir,'/static/assets/js','*.*')    
    backup_code(subdir,'/static/assets/sass','*.*') 
    backup_code(subdir,'/static/assets/sass/libs','*.*')     
    backup_code(subdir,'/static/assets/webfonts','*.*')        
    backup_code(subdir,'/static/images','*.*')          
    backup_code(subdir,'/keys','*.*')   
    #backup_code(subdir,'/profiles','*.*')        
    shutil.copyfile('./users.db', './'+subdir+'/users.db')   
    shutil.copyfile('./port.txt', './'+subdir+'/port.txt')     
    shutil.copyfile('./requirements.txt', './'+subdir+'/requirements.txt')        
    shutil.copyfile('./requirements_with_versions.txt', './'+subdir+'/requirements_with_versions.txt') 
    shutil.copyfile('./server_ip_address.txt', './'+subdir+'/server_ip_address.txt') 
    shutil.copyfile('./TODO.txt', './'+subdir+'/TODO.txt') 
    shutil.copyfile('./compile.py', './'+subdir+'/compile.py') 
    shutil.copyfile('./backup_app_system_code.py', './'+subdir+'/backup_app_system_code.py')     
    shutil.copyfile('./compile_script.py', './'+subdir+'/compile_script.py') 
    shutil.copyfile('./create_some_admins.py', './'+subdir+'/create_some_admins.py') 
    shutil.copyfile('./env.py', './'+subdir+'/env.py') 
    shutil.copyfile('./reset_appli_utils.py', './'+subdir+'/reset_appli_utils.py') 
    shutil.copyfile('./tabledef.py', './'+subdir+'/tabledef.py') 
    shutil.copyfile('./z_init_appli.py', './'+subdir+'/z_init_appli.py')     
    with open(subdir+'/a.bat','w') as file:
        file.write('python -m venv venv')
    with open(subdir+'/b.bat','w') as file:
        file.write('venv\\scripts\\activate')      
    with open(subdir+'/c.bat','w') as file:
        file.write('pip install -r requirements.txt')     
    with open(subdir+'/d.bat','w') as file:
        file.write('venv\\scripts\\deactivate')         
    with open(subdir+'/e.bat','w') as file:
        file.write('python z_init_appli.py')         
    return 1

def zip_dir(path, zip_handler):
    for root, dirs, files in os.walk(path):
        for file in files:
            zip_handler.write(os.path.join(root, file))
            
# a_core_main.py***
if __name__ == "__main__":
    subdir='./code_backup/'+current_date_and_time()
    os.mkdir(subdir)
    with open('./code_architecture/application_subfolders.txt') as file:
        text_content=file.read()
    subdir_list=text_content.split('\n')
    subdir_list.append('code_app_html_templates')
    subdir_list.append('code_app_scripts_to_import')
    subdir_list.append('code_app_routes')
    subdir_list.append('code_app_functions')
    subdir_list.append('code_architecture')
    print('subdir_list:',cyan(subdir_list,bold=True))
    for repertoire in subdir_list:
        repertoire =repertoire.strip()
        if repertoire!='':
            os.mkdir(subdir+'/'+repertoire )       
    print(cyan('BACKUP Imported Script Codes : >',bold=True))    
    backup_code_imported_scripts(subdir)
    print(cyan(' - Ok Done >',bold=True))   
    print(cyan('BACKUP CODE ARCHITECTURE : >',bold=True))    
    backup_code_architecture(subdir)
    print(cyan(' - Ok Done >',bold=True))     
    print(cyan('BACKUP CODE APP ROUTES : >',bold=True))    
    backup_code_app_routes(subdir)
    print(cyan(' - Ok Done >',bold=True))       
    print(cyan('BACKUP CODE APP FUNCTIONS : >',bold=True))    
    backup_code_app_functions(subdir)
    print(cyan(' - Ok Done >',bold=True))        
    print(cyan('BACKUP CODE app_html_templates : >',bold=True))    
    backup_code_app_html_templates(subdir)
    # to be customized here under
    print(cyan('BACKUP ALL THE REST OF THE APPLICATION AND CREATE A FULL PACKAGE >',bold=True))    
    backup_application_package(subdir)    
    print(cyan(' - Ok Done >',bold=True))    
    print(cyan('ZIP THE BACKUP >',bold=True))  
    zip_file_name=subdir+'.zip'
    zip_file = zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED)
    zip_dir(subdir, zip_file)
    zip_file.close()
    print(f'File Saved as {zip_file_name}')    
    print(cyan(' - Ok Done >',bold=True))     
    print(cyan('OK APPLICATION CODE BACKUP DONE >',bold=True))
  