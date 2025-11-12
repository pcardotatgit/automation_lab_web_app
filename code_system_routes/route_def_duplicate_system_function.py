#  def_duplicate_system_function***
@app.route('/duplicate_system_function', methods=['GET'])
def duplicate_system_function():
    '''
    Created : 2025-10-29

    description : duplicate a system function in app functions
    '''
    route="/duplicate_system_function"
    env.level+='-'
    print('\n'+env.level,white('route duplicate_system_function() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route duplicate_system_function() in ***app.py*** : >')
    global client_id
    global client_password
    global host
    global host_for_token
    global profil_name
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        filename=request.args.get('filename')
        print('\nfilename : ',filename)       
        mot=filename.replace('.py','')
        mot=mot.replace('def_','')
        filename2=filename.replace('.py','_COPY_.py')
        print('\nmot : ',mot+'\n')
        with open('./code_system_functions/'+filename) as file:
            code=file.read()
            code=code.replace(mot,mot+'_COPY_')    
        new_filename='./code_app_functions/'+filename2
        with open(new_filename,'w') as file:
              file.write(code)            
        with open('./code_architecture/app_functions.txt','a+') as file: 
            file.write(filename2+'\n')
        with open('./result/home_url.txt') as file:
            home_url=file.read()
        html_output='''<html><body><a href="'''+home_url+'''"><b><= back to home</b></a><br><br>
        <center><h3>function copied as '''+filename+'''_COPY_.py</h3></center>
        </body></html>
        ''';       
    '''    
    with open('./result/current_edited_script.txt',"w") as file:
        file.write(filename2)          
    '''
    env.level=env.level[:-1]
    return html_output 
  