#  def_copy_route_into_project***
@app.route('/copy_route_into_project', methods=['GET'])
def copy_route_into_project():
    '''
    Created : 2025-06-14T08:00:50.000Z

    description : copy selected script from library to project app scripts
    '''
    route="/copy_route_into_project"
    env.level+='-'
    print()
    print(env.level,white('route copy_route_into_project() in ***app.py*** : >',bold=True))
    loguer(env.level+' route copy_route_into_project() in ***app.py*** : >')
    print()
    global client_id
    global client_password
    global host
    global host_for_token
    global profil_name
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        script=request.args.get('script')
        print()
        print('script : ',script)
        source_filename='./code_central_routes/'+script
        destination_filename='./code_app_routes/'+script
        print(' ok copy this file :',source_filename,' to ',destination_filename)
        with open(source_filename) as file:
            text_content=file.read()            
        with open(destination_filename,'w') as file:
            file.write(text_content)             
        function_file='./code_architecture/app_routes.txt'
        if '.py' in script:
            pass
        else:
            script=script+'.py'
        if os.path.exists(function_file):
            with open(function_file) as file:
                text_content=file.read()        
            if  script not in text_content:            
                with open(function_file,'a+') as file:      
                    file.write(script+'\n')
        else:
            with open(function_file,'w') as file:      
                file.write(script+'\n')            
        with open('./result/home_url.txt') as file:
            home_url=file.read()            
        html_output='<html><body><b><a href="'+home_url+'"><= back to home</b></a><br><br><h3>Route Script :<br><br>'+script+'<br><br>Copied into project</h3><a href="/new_route_from_library">Copy / Link another route script </a><br><br><a href="/stop">Click here to stop the App  </a></body></html>';             
    env.level=env.level[:-1]
    return html_output         
