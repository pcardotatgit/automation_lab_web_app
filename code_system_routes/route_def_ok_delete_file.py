#  def_ok_delete_file***
@app.route('/ok_delete_file', methods=['GET'])
def ok_delete_file():
    '''
    Created : 2025-07-25

    description : Delete script as confirmation had been given
    '''
    route="/ok_delete_file"
    env.level+='-'
    print()
    print(env.level,white('route ok_delete_file() in ***app.py*** : >',bold=True))
    loguer(env.level+' route ok_delete_file() in ***app.py*** : >')
    print()
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        filename=request.args.get('filename')       
        print()
        print('filename path : ',filename)  
        print()          
        scriptdir=request.args.get('scriptdir')
        print()
        print('scriptdir : ',scriptdir)
        print()    
        if os.path.exists(filename):
            print(' ok delete',filename)
            os.remove(filename)            
        if scriptdir=='code_app_routes':
            filename=filename.replace('./code_app_routes/','')        
            print()
            print('filename : ',filename)  
            print()          
            function_file='./code_architecture/app_routes.txt'
        elif scriptdir=='code_app_functions':
            filename=filename.replace('./code_app_functions/','')        
            print()
            print('filename : ',filename)  
            print()           
            function_file='./code_architecture/app_functions.txt'         
        elif scriptdir=='code_app_html_templates':
            filename=filename.replace('./code_app_html_templates/','')        
            print()
            print('filename : ',filename)  
            print()           
            function_file='./code_architecture/main_html.txt'            
        else:
            chemin='./code_app_scripts_to_import/'+scriptdir+'/'
            filename=filename.replace(chemin,'')        
            print()
            print('filename : ',filename)  
            print()          
            if 'route_def' in filename:            
                function_file='./code_app_scripts_to_import/'+scriptdir+'/script_routes.txt'
            else:
                function_file='./code_app_scripts_to_import/'+scriptdir+'/script_functions.txt'            
        print()
        print('architecture file to update : ',function_file)  
        print()
        with open(function_file) as file:
            text_content=file.read()        
        text_content=text_content.replace(filename,'')    
        text_content=text_content.replace('\n\n','\n')
        with open(function_file,'w') as file:      
            file.write(text_content)
        with open('./result/home_url.txt') as file:
            home_url=file.read()            
        html_output='<html><body><b><a href="'+home_url+'"><= back to home</b></a><br><br><h3>Script : '+filename+' Deleted</h3><a href="/stop">Click here to stop the App  </a></body></html>';             
    env.level=env.level[:-1]
    return html_output  
        

