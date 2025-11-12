#  def_ok_rename_file***
@app.route('/ok_rename_file', methods=['GET'])
def ok_rename_file():
    '''
    Created : 2025-08-01

    description : Rename the selected script as it was confirmed prior
    '''
    route="/ok_rename_file"
    env.level+='-'
    print()
    print(env.level,white('route ok_rename_file() in ***app.py*** : >',bold=True))
    loguer(env.level+' route ok_rename_file() in ***app.py*** : >')
    print()
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        filepath=request.args.get('filename')       
        print()
        print('filename path : ',filepath)  
        print()          
        scriptdir=request.args.get('scriptdir')
        print()
        print('scriptdir : ',scriptdir)
        print()    
        new_name=request.args.get('new_name')
        if scriptdir=='code_app_html_templates':        
            if 'z_' not in new_name:
                new_name='z_'+new_name       
            if '.html' not in new_name:
                new_name=new_name+'.html'         
        print()
        print('new_name : ',new_name)
        print()     
        if '.py' in new_name:
            new_name=new_name.replace('.py','')           
        if scriptdir=='code_app_routes':
            filename=filepath.replace('./code_app_routes/','')        
            print()
            print('app route filename : ',filename)  
            print()          
            if os.path.exists(filepath):
                print(' ok rewrite this file :',filepath,' to ',new_name+'.py')
                with open(filepath) as file:
                    text_content=file.read()
                mot=filename.replace('.py','')
                mot=mot.replace('route_def_','')
                print()
                print('replace : ',mot, ' by ',new_name)  
                print()                   
                text_content=text_content.replace(mot,new_name)
                new_name2='route_def_'+new_name+'.py'
                new_name3=new_name       
                print('name3 : ',cyan(new_name3+'\n',bold=True))
                with open('./code_app_routes/'+new_name2,'w') as file:
                    file.write(text_content)             
            function_file='./code_architecture/app_routes.txt'
        elif scriptdir=='code_app_functions':
            filename=filepath.replace('./code_app_functions/','')        
            print()
            print('app function filename : ',filename)  
            print()     
            if os.path.exists(filepath):
                print(' ok rewrite this file :',filepath,' to ',new_name+'.py')
                with open(filepath) as file:
                    text_content=file.read()
                mot=filename.replace('.py','')
                mot=mot.replace('def_','')
                print()
                print('replace : ',mot, ' by ',new_name)  
                print()                 
                text_content=text_content.replace(mot,new_name)
                new_name2='def_'+new_name+'.py'
                new_name3=new_name
                with open('./code_app_functions/'+new_name2,'w') as file:
                    file.write(text_content)             
            function_file='./code_architecture/app_functions.txt'         
        elif scriptdir=='code_app_html_templates':
            filename=filepath.replace('./code_app_html_templates/','')    
            print()
            print('html page filename to rename : ',filename)  
            print()     
            if os.path.exists(filepath):
                print(' ok rewrite this file :',filename,' to ',new_name+'.html')
                with open(filepath) as file:
                    text_content=file.read()
                print()
                print('replace : ',filename, ' by ',new_name)  
                print()                 
                text_content=text_content.replace(filename,new_name)
                new_name2=new_name # needed for architecture file update
                with open('./code_app_html_templates/'+new_name,'w') as file:
                    file.write(text_content)             
            function_file='./code_architecture/main_html.txt'    
            mot=filename            
        else:
            chemin='./code_app_scripts_to_import/'+scriptdir+'/'
            filename=filepath.replace(chemin,'')                     
            if 'route_def' in filename:     
                print()
                print('script route filename : ',filename)  
                print()              
                if os.path.exists(filepath):
                    print(' ok rewrite this file :',filepath,' to ',new_name+'.py')
                    with open(filepath) as file:
                        text_content=file.read()
                    mot=filename.replace('.py','')
                    mot=mot.replace('route_def_','')
                    print()
                    print('replace : ',mot, ' by ',new_name)  
                    print()                       
                    text_content=text_content.replace(mot,new_name)
                    new_name2='route_def_'+new_name+'.py'
                    new_name3=new_name                    
                    with open('./code_app_scripts_to_import/'+scriptdir+'/'+new_name2,'w') as file:
                        file.write(text_content)                
                function_file='./code_app_scripts_to_import/'+scriptdir+'/script_routes.txt'
            else:
                print()
                print('script function filename : ',filename)  
                print()             
                if os.path.exists(filepath):
                    print(' ok rewrite this file :',filepath,' to ',new_name+'.py')
                    with open(filepath) as file:
                        text_content=file.read()
                    mot=filename.replace('.py','')
                    mot=mot.replace('def_','')
                    print()
                    print('replace : ',mot, ' by ',new_name)  
                    print()                                           
                    text_content=text_content.replace(mot,new_name)
                    new_name2='def_'+new_name+'.py'
                    new_name3=new_name
                    with open('./code_app_scripts_to_import/'+scriptdir+'/'+new_name2,'w') as file:
                        file.write(text_content)               
                function_file='./code_app_scripts_to_import/'+scriptdir+'/script_functions.txt'                     
        print()
        print('architecture file : ',function_file)  
        print()
        with open(function_file) as file:
            text_content=file.read()        
        text_content=text_content.replace(mot,new_name3)    
        text_content=text_content.replace('\n\n','\n')
        with open(function_file,'w') as file:      
            file.write(text_content)
        if os.path.exists(filepath):
            print(' ok delete',filepath)
            os.remove(filepath)            
        with open('./result/home_url.txt') as file:
            home_url=file.read()            
        html_output='<html><body><b><a href="'+home_url+'"><= back to home</b></a><br><br><h3>Script : '+filename+' Renamed to '+new_name+'.py</h3><a href="/stop">Click here to stop the App  </a></body></html>';             
    env.level=env.level[:-1]
    return html_output  
        

