#  def_ok_move_function_to_system***
@app.route('/ok_move_function_to_system', methods=['GET'])
def ok_move_function_to_system():
    '''
    Created : 2025-06-10T14:46:18.000Z

    description : move function to system confirmed. Lets do it
    '''
    route="/ok_move_function_to_system"
    env.level+='-'
    print()
    print(env.level,white('route ok_move_function_to_system() in ***app.py*** : >',bold=True))
    loguer(env.level+' route ok_move_function_to_system() in ***app.py*** : >')
    print()
    global client_id
    global client_password
    global host
    global host_for_token
    global profil_name
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
        new_name=filepath.replace('code_app_functions','code_system_functions')
        print()
        print('new_name : ',new_name)
        print()        
       
        if os.path.exists(filepath):
            print(' ok move this file :',filepath,' to ',new_name)
            with open(filepath) as file:
                text_content=file.read()            
            with open(new_name,'w') as file:
                file.write(text_content)      
        scriptname=filepath.replace('./code_app_functions/','')    
        print()
        print('scriptname : ',scriptname)
        print()         
        function_file='./code_architecture/app_functions.txt'

        with open(function_file) as file:
            text_content=file.read()        
        text_content=text_content.replace(scriptname+'\n','')    
        with open(function_file,'w') as file:      
            file.write(text_content)

        with open('./code_architecture/system_functions.txt','a+') as file:      
            file.write(scriptname+'\n')
                        
        if os.path.exists(filepath):
            print(' ok delete',filepath)
            os.remove(filepath)            
        with open('./result/home_url.txt') as file:
            home_url=file.read()            
        html_output='<html><body><b><a href="'+home_url+'"><= back to home</b></a><br><br><h3>Ok function script had been moved to system</h3><a href="/stop">Click here to stop the App  </a></body></html>';             
    env.level=env.level[:-1]
    return html_output  
  
