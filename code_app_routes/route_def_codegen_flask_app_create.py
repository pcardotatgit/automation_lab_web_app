#  def_codegen_flask_app_create***
@app.route('/codegen_flask_app_create', methods=['GET'])
def codegen_flask_app_create():
    '''
    Created : 2025-09-29
    description : Create the Flask Application Structure as an imported script
    '''
    route="/codegen_flask_app_create"
    env.level+='-'
    print('\n'+env.level,white('route codegen_flask_app_create() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route codegen_flask_app_create() in ***app.py*** : >')
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        # ===================================================================
        # GET variable from calling web page
        name=request.args.get("name")
        print("\nname : ",name)
        name=name.replace(' ','_')
        description=request.args.get("description")
        print("\ndescription : ",description)
        filename = request.args.get('name')
        port=request.args.get("port")
        print("\nport : ",port) 
        protocol=request.args.get("protocol")
        print("\nprotocol : ",protocol)         
        if '.py' not in filename:
            filename=filename+'.py'
        description = request.args.get('description')
        print()
        print(' filename :\n',yellow(filename,bold=True))
        print()
        print(' description :\n',yellow(description,bold=True))
        print()
        with open('./code_architecture/imported_scripts.txt') as file:
            text_content=file.read()
        name_list=text_content.split('\n')
        good=1
        for item in name_list:
            if filename==item:
                good=0
        if good==0:
            print(filename+' already exists ! Choose another name')
            message1="Name already Exist"
            image="../static/images/nok.png"
            message2="Choose another name"
            message3="/codegen_flask_app"
            message4="Create a Flask App"
            PAGE_DESTINATION="operation_done"
            page_name="operation_done.html"
            loguer(env.level+' route END OF codegen_flask_app_create() in ***app.py*** : >')
            # ===================================================================
            env.level=env.level[:-1]
            return render_template('main_index.html',route=route,USERNAME=session['user'],PAGE_DESTINATION=PAGE_DESTINATION,message1=message1,message2=message2,message3=message3,message4=message4,image=image,page_name=page_name)
                
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
            os.mkdir(subdir+'/package_dev/templates')              
            os.mkdir(subdir+'/package_prod')
            os.mkdir(subdir+'/package_prod/debug')
            os.mkdir(subdir+'/package_prod/temp')
            os.mkdir(subdir+'/package_prod/output')
            os.mkdir(subdir+'/package_prod/result')
            os.mkdir(subdir+'/package_prod/templates')            
            with open(subdir+'/a_imports.txt','w') as file:
                line_out='''from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
import os
import sys
from crayons import *
from werkzeug.utils import secure_filename
import random
from datetime import datetime, timedelta
import socket
import webbrowser
import threading
import time
import glob
import signal
import requests
import json
import hashlib
from pathlib import Path
from inspect import currentframe
import subprocess
import shutil
import env as env
#import sqlalchemy
#from sqlalchemy.orm import sessionmaker
#from tabledef import *
#import sqlite3
#import struct
#import csv
#import pandas as pd
#from pandas import DataFrame
'''                
                file.write(line_out)
            with open(subdir+'/a_global_variables.txt','w') as file:
                file.write('app = Flask(__name__)\n')
            with open(subdir+'/script_functions.txt','w') as file:
                file.write('def_loguer.py\ndef_open_browser_tab.py\n')
            with open(subdir+'/script_routes.txt','w') as file:
                file.write('')
            with open(subdir+'/a_header.txt','w') as file:
                line_out="# -*- coding: UTF-8 -*-\n#!/usr/bin/env python\n'''\n    description : "
                line_out=line_out+description+"\n'''"
                file.write(line_out)
            with open(subdir+'/a_main.txt','w') as file:
                line_out='''
@app.route(\'/\', methods=[\'GET\'])
def index():
    \'\'\'
    version:

    description : index page
    \'\'\'
    route="/index"
    env.level+=\'-\'
    print(\'\\n\'+env.level,white(\'route index() in ***app.py*** : >\\n\',bold=True))
    loguer(env.level+\' route index() in ***app.py*** : >\')
    # ===================================================================
    env.level=env.level[:-1]
    return render_template(\'index.html\')
  
    
if __name__=="__main__":
    print(env.level,white("MAIN FUNCTION ( the application starts here ): >",bold=True))
    with open("./debug/log.txt","w") as file:
        pass
    loguer(env.level+" APPLICATION STARTS")
'''
                if protocol=="http":
                    line_out=line_out+'''    host="127.0.0.1"
    open_browser_tab(host,'''+port+''')
    app.secret_key = os.urandom(12)
    app.run(debug=False,host='0.0.0.0', port='''+port+''')
    '''
                else:
                    line_out=line_out+'''    host="127.0.0.1"
    #open_browser_tab(host,'''+port+''')
    app.secret_key = os.urandom(12)
        app.run(debug=True,host='0.0.0.0',port='''+port+''',ssl_context='adhoc')
    '''    
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
                file.write("crayons==0.4.0\nrequests==2.32.3\nflask\nsqlalchemy\npandas\nijson")
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
                file.write("crayons==0.4.0\nrequests==2.32.3\nflask\nsqlalchemy\npandas\nijson")
        file_types='*.*'
        src_directory='./static'
        dst_directory=subdir+'/package_dev/static'        
        copy_dir(src_directory,dst_directory,file_types)
        src_directory='./static/img'
        dst_directory=subdir+'/package_dev/static/img'        
        copy_dir(src_directory,dst_directory,file_types)        
        src_directory='./static/assets'
        dst_directory=subdir+'/package_dev/static/assets'        
        copy_dir(src_directory,dst_directory,file_types) 
        src_directory='./static/assets/css'
        dst_directory=subdir+'/package_dev/static/assets/css'        
        copy_dir(src_directory,dst_directory,file_types)
        src_directory='./static/assets/css/images'
        dst_directory=subdir+'/package_dev/static/assets/css/images'        
        copy_dir(src_directory,dst_directory,file_types)
        src_directory='./static/assets/css/images/ie'
        dst_directory=subdir+'/package_dev/static/assets/css/images/ie'        
        copy_dir(src_directory,dst_directory,file_types)
        src_directory='./static/assets/js'
        dst_directory=subdir+'/package_dev/static/assets/js'        
        copy_dir(src_directory,dst_directory,file_types)
        src_directory='./static/assets/sass'
        dst_directory=subdir+'/package_dev/static/assets/sass'        
        copy_dir(src_directory,dst_directory,file_types)
        src_directory='./static/assets/sass/libs'
        dst_directory=subdir+'/package_dev/static/assets/sass/libs'        
        copy_dir(src_directory,dst_directory,file_types)
        src_directory='./static/assets/webfonts'
        dst_directory=subdir+'/package_dev/static/assets/webfonts'        
        copy_dir(src_directory,dst_directory,file_types)     
        src_directory='./static/images'
        dst_directory=subdir+'/package_dev/static/images'        
        copy_dir(src_directory,dst_directory,file_types)    
        src_directory='./static'
        dst_directory=subdir+'/package_prod/static'        
        copy_dir(src_directory,dst_directory,file_types)
        src_directory='./static/img'
        dst_directory=subdir+'/package_prod/static/img'        
        copy_dir(src_directory,dst_directory,file_types)        
        src_directory='./static/assets'
        dst_directory=subdir+'/package_prod/static/assets'        
        copy_dir(src_directory,dst_directory,file_types) 
        src_directory='./static/assets/css'
        dst_directory=subdir+'/package_prod/static/assets/css'        
        copy_dir(src_directory,dst_directory,file_types)
        src_directory='./static/assets/css/images'
        dst_directory=subdir+'/package_prod/static/assets/css/images'        
        copy_dir(src_directory,dst_directory,file_types)
        src_directory='./static/assets/css/images/ie'
        dst_directory=subdir+'/package_prod/static/assets/css/images/ie'        
        copy_dir(src_directory,dst_directory,file_types)
        src_directory='./static/assets/js'
        dst_directory=subdir+'/package_prod/static/assets/js'        
        copy_dir(src_directory,dst_directory,file_types)
        src_directory='./static/assets/sass'
        dst_directory=subdir+'/package_prod/static/assets/sass'        
        copy_dir(src_directory,dst_directory,file_types)
        src_directory='./static/assets/sass/libs'
        dst_directory=subdir+'/package_prod/static/assets/sass/libs'        
        copy_dir(src_directory,dst_directory,file_types)
        src_directory='./static/assets/webfonts'
        dst_directory=subdir+'/package_prod/static/assets/webfonts'        
        copy_dir(src_directory,dst_directory,file_types)     
        src_directory='./static/images'
        dst_directory=subdir+'/package_prod/static/images'        
        copy_dir(src_directory,dst_directory,file_types)   
        shutil.copyfile('./code_templates/index.html', './'+subdir+'/package_dev/templates/index.html')
        shutil.copyfile('./code_templates/index.html', './'+subdir+'/package_prod/templates/index.html')        
        shutil.copyfile('./code_central_functions/def_loguer_v2025-09-29.py', './'+subdir+'/def_loguer.py')     
        shutil.copyfile('./code_central_functions/def_open_browser_tab_v2025-09-29.py', './'+subdir+'/def_open_browser_tab.py')         
        # ###########################################
        message1="Flask App Created"
        image="../static/images/ok.png"
        message2="Edit the APP in the imported scripts"
        message3="/goto_script_B?script="+name+".py&type=route"
        message4="Edit the Flask APP"
        PAGE_DESTINATION="z_codegen_flask_app_create"
        page_name="z_codegen_flask_app_create.html"
        loguer(env.level+' route END OF codegen_flask_app_create() in ***app.py*** : >')
        # ===================================================================
        env.level=env.level[:-1]
        return render_template('main_index.html',route=route,USERNAME=session['user'],PAGE_DESTINATION=PAGE_DESTINATION,message1=message1,message2=message2,message3=message3,message4=message4,image=image,page_name=page_name)
        
