#  def_copy_function_to_central_B***
@app.route('/copy_function_to_central_B', methods=['GET'])
def copy_function_to_central_B():
    '''
    Created : 2025-08-22

    description : copy a function script from an imported script to central library
    '''
    route="/copy_function_to_central_B"
    env.level+='-'
    print()
    print(env.level,white('route copy_function_to_central_B() in ***app.py*** : >',bold=True))
    loguer(env.level+' route copy_function_to_central_B() in ***app.py*** : >')
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
        new_name=filepath.replace('code_app_scripts_to_import/'+scriptdir,'code_central_functions')
        script_date = datetime.utcnow().strftime("%Y-%m-%d")
        new_name=new_name.replace('.py','_v'+script_date+'.py')
        print()
        print('new_name : ',new_name)
        print()        
        print(' ok copy this file :',filepath,' to ',new_name+'.py')
   
        with open(filepath) as file:
            text_content=file.read()
        lines=text_content.split('\n')
        output_lines=''
        for line in lines:
            print('line :' ,cyan(line,bold=True))
            if "print(env.level,white(" in line or "print('\\n'+env.level,white(" in line:
                print('line :',red(line,bold=True))
                chunks=line.split(') in ')
                line=chunks[0]+") in app.py  : >\\n',bold=True))"
                print('TO line :',green(line,bold=True))
            if "loguer(env.level+" in line:
                print('line :',red(line,bold=True))
                chunks=line.split(') in ')
                line=chunks[0]+") in app.py  : > ')"
                print('TO line :',green(line,bold=True))                
            output_lines=output_lines+line+'\n'
        with open(new_name,'w') as file:
            file.write(output_lines)      
        scriptname=filepath.replace('./code_app_scripts_to_import/'+scriptdir+'/','') 
        print()
        print('scriptname : ',scriptname)
        print()         
        function_file='./code_central_functions/central_functions.txt'

        if '.py' in scriptname:
            pass
        else:
            scriptname=scriptname+'.py'
        if os.path.exists(function_file):
            with open(function_file) as file:
                text_content=file.read()        
            if  scriptname not in text_content:            
                with open(function_file,'a+') as file:      
                    file.write(scriptname+'\n')
        else:
            with open(function_file,'w') as file:      
                file.write(scriptname+'\n')  
        
        with open('./result/home_url.txt') as file:
            home_url=file.read()            
        html_output='<html><body><b><a href="'+home_url+'"><= back to home</b></a><br><br><h3>Ok function script had been Copied to cenral library</h3><a href="/stop">Click here to stop the App  </a></body></html>';             
    env.level=env.level[:-1]
    return html_output  
  
