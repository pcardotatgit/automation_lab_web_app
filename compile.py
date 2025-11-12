# a_core_imports.py***
'''
    modified : 20250725
'''
from crayons import *
import os
from datetime import datetime, timedelta
import shutil
import glob
import sys
import env as env


dateTime = datetime.now()

def delete_files_in_templates():
    env.level+='-'
    print()
    print(env.level,white('def delete_files_in_templates() : >',bold=True))
    print()
    file_list=glob.glob("./templates/*.html")
    for fichier in file_list:
        fichier=fichier.replace('\\','/')        
        if os.path.exists(fichier):
            print(' ok delete',fichier)
            os.remove(fichier)    
    env.level=env.level[:-1]
    return 1

def create_app_py():
    env.level+='-'
    route="/create_app_py"
    print()
    print(env.level,white('def create_app_py() : >',bold=True))
    print()
    text_content=''  
    '''
    with open('./app.py') as file:
            text_content=file.read()     
    with open('./code_backup/app_'+current_date_and_time()+'.py','w') as file:
            file.write(text_content) 
    '''
    print()
    print(green('   app.py backup = OK',bold=True))
    print()                
    with open('./app.py','w') as app:
        print()
        print(green('  Create header',bold=True))
        print()    
        text_content=''        
        with open('./code_system_main_blocs/a_core_header.py') as file:
            text_content=file.read() 
        app.write(text_content)
        app.write('\n')
        print(green('  - Create header = OK',bold=True))
        print()
        print(green('  Create Import section',bold=True))
        text_content=''        
        with open('./code_system_main_blocs/a_core_imports.py') as file:
            text_content=file.read() 
        app.write(text_content)
        app.write('\n')   
        print(green('  - Create Import section = OK',bold=True))
        print()
        print(green('  Create Global Variable Definition',bold=True))
        text_content=''        
        with open('./code_system_main_blocs/a_core_global_definitions.py') as file:
            text_content=file.read() 
        app.write(text_content)
        app.write('\n')
        app.write('\n')     
        print(green('  - Create Global Variable Definition = OK',bold=True))
        print()
        print(green('  Create system functions ',bold=True))      
        line_out='''
# here under FUNCTIONS ===========================   
 
'''
        app.write(line_out)          
        text_content=''        
        with open('./code_architecture/system_functions.txt') as file:
            text_content=file.read()
        lines=text_content.split('\n')
        for script_name in lines:
            print(script_name)
            if script_name.strip() !="":
                with open(f'./code_system_functions/{script_name}') as file2:
                    text_content2=file2.read() 
                app.write(text_content2)
                app.write('\n\n')
        print(green('  - Create system functions = OK',bold=True))
        print()  
        print(green('  Create application functions',bold=True))
        app.write(line_out)  
        text_content=''        
        with open('./code_architecture/app_functions.txt') as file:
            text_content=file.read()
        lines=text_content.split('\n')
        for script_name in lines:
            print(script_name)
            if script_name.strip() !="":
                with open(f'./code_app_functions/{script_name}') as file2:
                    text_content2=file2.read() 
                app.write(text_content2)
                app.write('\n\n')
        print(green('  - Create application functions = OK',bold=True))
        print()     
        print(green('  Create system routes ',bold=True))        
        line_out='''
# here under the flask routes part ===========================    

app = Flask(__name__)

'''
        app.write(line_out)            
        # On let's add the other system route
        text_content=''
        with open('./code_architecture/system_routes.txt') as file:
            text_content=file.read()
        lines=text_content.split('\n')
        for script_name in lines:
            print(script_name)
            if script_name.strip() !="":
                with open(f'./code_system_routes/{script_name}') as file2:
                    text_content2=file2.read() 
                app.write(text_content2)
                app.write('\n\n')                  
        print(green('  - Create system routes = OK',bold=True))
        print()           
        print(green('  Create application routes',bold=True))  
        text_content=''
        with open('./code_architecture/app_routes.txt') as file:
            text_content=file.read()
        lines=[]
        lines=text_content.split('\n')
        for script_name in lines:
            print(script_name)
            if script_name.strip() !="":
                text_content2=''
                with open(f'./code_app_routes/{script_name}') as file2:
                    text_content2=file2.read() 
                app.write(text_content2)
                app.write('\n\n')           
        print(green('  - Create Application routes = OK',bold=True))
        print()     
        print(green('  Create Main Function',bold=True))          
        text_content=''
        with open('./code_system_main_blocs/a_core_main.py') as file:
            text_content=file.read() 
        app.write('\n') 
        app.write(text_content)
        app.write('\n')         
        print(green('  - Create Main Function = OK',bold=True))     
      
    env.level=env.level[:-1]
    return 1
    
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

def copy_system_htmls():
    env.level+='-'
    print()
    print(env.level,white('def copy_system_htmls() : >',bold=True))
    print()
    file_list0=glob.glob("./code_system_html_templates/*.html")
    file_list=[]
    for fichier in file_list0:
        fichier2=fichier.split('\\')[1]
        print(fichier2)
        src='./code_system_html_templates/'+fichier2
        dst='./templates/'+fichier2
        shutil.copyfile(src, dst)
    env.level=env.level[:-1]
    return(file_list)
         
def copy_app_htmls():
    env.level+='-'
    print()
    print(env.level,white('def copy_app_htmls() : >',bold=True))
    print()
    file_list0=glob.glob("./code_app_html_templates/*.*")
    for fichier in file_list0:
        fichier2=fichier.split('\\')[1]
        print(fichier2)
        src='./code_app_html_templates/'+fichier2
        dst='./templates/'+fichier2
        mot='* '+fichier2+'***'
        with open(src) as inputfile:
            with open(dst,'w') as outfile:
                for line in inputfile:
                        outline=line.strip()
                        outline=outline.replace(mot,"")
                        if outline != "":
                            outfile.write(outline+'\n')
    env.level=env.level[:-1]
    return 1
    
    
def create_resource_files():
    with open('./result/home_url.txt','w') as file:
        line='/page_info?page=home.html&route=/'
        file.write(line)            
    return 1
    
def create_main_html():
    env.level+='-'
    print()
    print(env.level,white('def create_main_html() : >',bold=True))
    print()
    outlines='''{% if session['logged_in'] %}
    {% if PAGE_DESTINATION == "home"%}
    {% extends "home.html" %}
    {% endif %}   
    {% if PAGE_DESTINATION == "index"%}
    {% extends "index.html" %}
    {% endif %} 
    {% if PAGE_DESTINATION == "operation_done"%}
    {% extends "operation_done.html" %}
    {% endif %}
    {% if PAGE_DESTINATION == "under_construction"%}
    {% extends "under_construction.html" %}
    {% endif %}    
    {% if PAGE_DESTINATION == "create_app_py"%}
    {% extends "create_app_py.html" %}
    {% endif %} 
'''
    with open('./templates/main_index.html','w') as file:
        with open('./code_architecture/main_html.txt') as file2:
            text_content=file2.read()
        lines2=text_content.split('\n')        
        for line2 in lines2:
            if line2!='':
                line2B=line2.replace('.html','')
                out='''    {% if PAGE_DESTINATION == "'''+line2.replace('.html','')+'''"%}
    {% extends "'''+line2+'''" %}
    {% endif %}
'''
                outlines=outlines+out
        with open('./code_templates/main_base.html') as file2:
            text_content=file2.read() 
        outlines=outlines+text_content
        file.write(outlines)
    env.level=env.level[:-1]
    return 1    
    
def create_imported_scripts():
    env.level+='-'
    print()
    print(env.level,white('def create_imported_scripts() : >',bold=True))
    with open('./code_architecture/imported_scripts_to_import.txt') as file:
        nb=0
        for line in file:
            nb+=1
            line=line.strip()
            line=line.replace('\\n','')
            if line!="":
                print()
                print('imported script to create : ',line)
                print()
                scriptdir='./code_app_scripts_to_import/'+line.replace('.py','')+'/'    
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
                with open(scriptdir+'a_main.txt') as file:
                    text_content=file.read()+'\n'
                lines_out=lines_out+text_content            
                # create the script
                with open('./'+line,'w') as file4:
                    file4.write(lines_out)
    print()
    env.level=env.level[:-1]
    return 1
    
def update_port_number_in_code_edit_scripts():
    with open('./port.txt') as file:
        port=file.read()
    with open('./server_ip_address.txt') as file:
        ip_address=file.read()        
    with open('./code_system_html_templates/code_editor.html') as file:
        text_content=file.read()   
    lines=text_content.split('\n')
    text_content_out=''
    for line in lines:    
        if "fetch" in line:
            line='            fetch("http://'+ip_address+':'+port+'/save_code", {'
        text_content_out+=line+'\n'
    with open('./code_system_html_templates/code_editor.html','w') as file:
        file.write(text_content_out)
        
    with open('./code_system_html_templates/code_editor_B.html') as file:
        text_content=file.read()   
    lines=text_content.split('\n')
    text_content_out=''
    for line in lines:    
        if "fetch" in line:
            line='            fetch("http://'+ip_address+':'+port+'/save_code_B", {'
        text_content_out+=line+'\n'
    with open('./code_system_html_templates/code_editor_B.html','w') as file:
        file.write(text_content_out)        
    return 1
    
# a_core_main.py***
if __name__ == "__main__":
    print(cyan('\nupdate port number in code edit scripts : >\n',bold=True)) 
    update_port_number_in_code_edit_scripts()    
    print()
    print(white('MAIN FUNCTION : >',bold=True))
    print()
    print(cyan('DELETE HTML FILES IN TEMPLATES : >',bold=True))
    delete_files_in_templates()
    print(cyan(' - Ok Done >',bold=True))
    print()
    print(cyan('COPY SYSTEM HTML FILES IN TEMPLATES : >',bold=True))    
    copy_system_htmls()
    print(cyan(' - Ok Done >',bold=True))
    print()
    print(cyan('COPY APP HTML FILES IN TEMPLATES : >',bold=True))    
    copy_app_htmls()
    print(cyan(' - Ok Done >',bold=True)) 
    print()   
    print(cyan('create maint_html file in templates : >',bold=True))    
    create_main_html()
    print(cyan(' - Ok Done >',bold=True))
    print()   
    print(cyan('CREATE APP.PY : >',bold=True))     
    create_app_py()
    print()
    print(cyan('CREATE RESOURCES FILES : >',bold=True))     
    create_resource_files()
    print()    
    print(cyan('CREATE EXTERNAL IMPORTED_SCRIPTS : >',bold=True)) 
    create_imported_scripts()
    print()
    print(cyan('==========================================================================',bold=True))     
    print()
    print(cyan('OK DONE app.py was builted : >',bold=True))
    print()   
    print(cyan('Now let\' start the app : >',bold=True))
    print()      
    os.system("python app.py 1")    