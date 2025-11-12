# def_new_script_to_import_create***
@app.route('/new_script_to_import_create', methods=['GET','POST'])
def new_script_to_import_create():
    env.level+='-'
    print()
    print(env.level,white('route new_script_to_import_create() : >',bold=True))
    loguer(env.level+' route new_script_to_import_create() : >')
    print()
    '''
    Modified : 20251001
    
    create a new external python script to import ase a resource to the main script
    '''    
    filename = request.args.get('name')
    if '.py' not in filename:
        filename=filename+'.py'
    filename=filename.replace('-','_')
    filename=filename.replace(' ','_')        
    description = request.args.get('description')
    print()
    print(' filename :\n',yellow(filename,bold=True))
    print()
    print(' description :\n',yellow(description,bold=True))
    print()
    with open('./code_architecture/imported_scripts.txt') as file:
        text_content=file.read()    
    if filename in text_content:
        print(filename+' already exists ! Choose another name')
        html_output='''<html><body>
        <center><h3>This script already exists ! choose another name</h3></center>
    <form action="/new_script_to_import_create" method="GET">
    <b>script name : </b><input type="text"  id="script_name" name="name" /><br><br>
    <b>script description</b><br>
    <textarea id="description" name="description" rows="5" cols="50"></textarea><br><br>
    <center><input type="submit" value="valid"/></center>
    </form>        
        </body></html>
        ''';        
    else:
        print(yellow(f'     {filename} does NOT exists. Let s create it',bold=True))
        with open('./code_architecture/imported_scripts.txt','a+') as file:
            file.write(filename+'\n')          
        # create a sub durectory
        subdir='./code_app_scripts_to_import/'+filename.replace('.py','')
        os.mkdir(subdir)
        os.mkdir(subdir+'/package_dev') 
        os.mkdir(subdir+'/package_dev/debug')      
        os.mkdir(subdir+'/package_dev/temp')        
        os.mkdir(subdir+'/package_dev/output')
        os.mkdir(subdir+'/package_dev/result')
        os.mkdir(subdir+'/package_prod')    
        os.mkdir(subdir+'/package_prod/debug')
        os.mkdir(subdir+'/package_prod/temp')
        os.mkdir(subdir+'/package_prod/output')      
        os.mkdir(subdir+'/package_prod/result')        
        with open(subdir+'/a_imports.txt','w') as file:
            line_out="import env as env\nfrom crayons import *\nfrom analyse_application_logs import loguer\n"
            file.write(line_out)
        with open(subdir+'/a_global_variables.txt','w') as file:
            file.write('')  
        with open(subdir+'/script_functions.txt','w') as file:
            file.write('')   
        with open(subdir+'/script_routes.txt','w') as file:
            file.write('')              
        with open(subdir+'/a_header.txt','w') as file:
            line_out="# -*- coding: UTF-8 -*-\n#!/usr/bin/env python\n'''\n    description : "
            line_out=line_out+description+"\n'''"
            file.write(line_out)             
        with open(subdir+'/a_main.txt','w') as file:
            line_out='if __name__=="__main__":\n    print(env.level,white("MAIN FUNCTION ( the application starts here ): >",bold=True))\n    with open("./debug/log.txt","w") as file:\n        pass\n    loguer(env.level+" APPLICATION STARTS")'    
            file.write(line_out)     
        with open(subdir+'/build_location.txt','w') as file:
            file.write(subdir+'/package_dev')     
 
        with open(subdir+'/package_dev/result/home_url.txt','w') as file:
            pass 
        with open(subdir+'/package_prod/result/home_url.txt','w') as file:
            pass 
        with open(subdir+'/package_dev/env.py','w') as file:
            file.write('level="["')
        with open(subdir+'/package_prod/env.py','w') as file:
            file.write('level="["')         
            
        with open('./result/home_url.txt') as file:
            home_url=file.read()
            print()
            print('home_url',home_url)
            print()
            
        with open("./analyse_application_logs.py") as file:
            text_content=file.read()
        text_content=text_content.replace("app.py",filename)
        with open(subdir+'/package_dev/analyse_application_logs.py','w') as file:
            file.write(text_content)
        with open(subdir+'/package_prod/analyse_application_logs.py','w') as file:
            file.write(text_content)        
            
        with open("./code_templates/z_init_appli.py") as file:
            text_content=file.read()
        text_content=text_content.replace("app.py",filename)
        with open(subdir+'/package_dev/z_init_appli.py','w') as file:
            file.write(text_content)
        with open(subdir+'/package_prod/z_init_appli.py','w') as file:
            file.write(text_content)     
        with open(subdir+'/package_dev/a.bat','w') as file:
            file.write("python -m venv venv")     
        with open(subdir+'/package_dev/b.bat','w') as file:
            file.write("venv\\scripts\\activate")    
        with open(subdir+'/package_dev/c.bat','w') as file:
            file.write("pip install -r requirements.txt")      
        with open(subdir+'/package_dev/d.bat','w') as file:
            file.write("venv\\scripts\\deactivate")    
        with open(subdir+'/package_dev/e.bat','w') as file:
            file.write("python z_init_appli.py")   
        with open(subdir+'/package_dev/requirements.txt','w') as file:
            file.write("crayons==0.4.0\nrequests==2.32.3")
        with open(subdir+'/package_prod/a.bat','w') as file:
            file.write("python -m venv venv")     
        with open(subdir+'/package_prod/b.bat','w') as file:
            file.write("venv\\scripts\\activate")    
        with open(subdir+'/package_prod/c.bat','w') as file:
            file.write("pip install -r requirements.txt")      
        with open(subdir+'/package_prod/d.bat','w') as file:
            file.write("venv\\scripts\\deactivate")    
        with open(subdir+'/package_prod/e.bat','w') as file:
            file.write("python z_init_appli.py")  
        with open(subdir+'/package_prod/requirements.txt','w') as file:
            file.write("crayons==0.4.0\nrequests==2.32.3")            
        html_output='<html><body><a href="'
        html_output=html_output+home_url
        html_output=html_output+'"><b><= back to home</b></a><br><br>\n<center><h3>script '
        html_output=html_output+filename
        html_output=html_output+' created</h3></center>\n </body></html>'             
    env.level=env.level[:-1]
    return html_output  
