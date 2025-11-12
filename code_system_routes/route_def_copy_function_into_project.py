#  def_copy_function_into_project***
@app.route('/copy_function_into_project', methods=['GET'])
def copy_function_into_project():
    '''
    Created : 2025-08-23

    description : copy function from central library to app functions
    '''
    route="/copy_function_into_project"
    env.level+='-'
    print()
    print(env.level,white('route copy_function_into_project() in ***app.py*** : >',bold=True))
    loguer(env.level+' route copy_function_into_project() in ***app.py*** : >')
    print()
    global client_id
    global client_password
    global host
    global host_for_token
    global profil_name
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        '''
        script_project=request.args.get('scriptdir')+'.py'
        print()
        print('script_project : ',scriptdir)  
        '''
        script=request.args.get('script')
        print()
        print('script to add into project : ',script)
        source_filename='./code_central_functions/'+script
        if '_v20' in script:
            script_destination=script.split('_v')[0]+'.py'
        else:
            script_destination=script
        destination_filename='./code_app_functions/'+script_destination
        print(' ok copy this file :',source_filename,' to ',destination_filename)
        with open(source_filename) as file:
            text_content=file.read()         
        #text_content=text_content.replace('app.py',script_project)
        with open(destination_filename,'w') as file:
            file.write(text_content)             
        function_file='./code_architecture/app_functions.txt'
        if '.py' in script_destination:
            pass
        else:
            script_destination=script_destination+'.py'
        if os.path.exists(function_file):
            with open(function_file) as file:
                text_content=file.read()        
            if  script_destination not in text_content:            
                with open(function_file,'a+') as file:      
                    file.write(script_destination+'\n')
        else:
            with open(function_file,'w') as file:      
                file.write(script_destination+'\n')            
        with open('./result/home_url.txt') as file:
            home_url=file.read()            
        html_output='<html><body><b><a href="'+home_url+'"><= back to home</b></a><br><br><h3>Function Script :<br><br>'+script+'<br><br>Copied into project</h3><a href="/new_function_from_library">Copy / Link another function script </a><br><br><a href="/stop">Click here to stop the App  </a></body></html>';             
    env.level=env.level[:-1]
    return html_output         
  
