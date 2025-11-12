#  def_duplicate_script***
@app.route('/duplicate_script', methods=['GET'])
def duplicate_script():
    '''
    Created : 2025-08-22

    description : duplicate a function in an imported script
    '''
    route="/duplicate_script"
    env.level+='-'
    print('\n'+env.level,white('route duplicate_script() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route duplicate_script() in ***app.py*** : >')
    print('\n'+env.level,white('route duplicate_route() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route duplicate_route() in ***app.py*** : >')
    global client_id
    global client_password
    global host
    global host_for_token
    global profil_name
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        type=request.args.get('type')
        print('\ntype : ',type)       
        scriptdir=request.args.get('scriptdir')
        print('\nscriptdir : ',scriptdir)       
        filename=request.args.get('filename')
        print('\nfilename : ',filename)       
        mot=filename.replace('.py','')
        if type=="route":
               mot=mot.replace('route_def_','')
        else:
            mot=mot.replace('def_','')  
        filename2=filename.replace('.py','_COPY_.py')
        print('\nmot : ',mot+'\n')
        with open('./code_app_scripts_to_import/'+scriptdir+'/'+filename) as file:
            code=file.read()
            code=code.replace(mot,mot+'_COPY_')    
        new_filename='./code_app_scripts_to_import/'+scriptdir+'/'+filename2
        with open(new_filename,'w') as file:
              file.write(code)   
        if type=="route":
            with open('./code_architecture/script_routes.txt','a+') as file: 
                file.write(filename2+'\n')
            with open('./code_app_scripts_to_import/'+scriptdir+'/script_routes.txt','a+') as file: 
                file.write(filename2+'\n')                
        else:
            with open('./code_architecture/script_functions.txt','a+') as file: 
                file.write(filename2+'\n')    
            with open('./code_app_scripts_to_import/'+scriptdir+'/script_functions.txt','a+') as file: 
                file.write(filename2+'\n')                                
        with open('./result/home_url.txt') as file:
            home_url=file.read()
        html_output='''<html><body><a href="'''+home_url+'''"><b><= back to home</b></a><br><br>
        <center><h3>route copied as '''+filename+'''_COPY_.py</h3></center>
        </body></html>
        ''';       
    '''    
    with open('./result/current_edited_script.txt',"w") as file:
        file.write(filename2)          
    '''
    env.level=env.level[:-1]
    return html_output 
  