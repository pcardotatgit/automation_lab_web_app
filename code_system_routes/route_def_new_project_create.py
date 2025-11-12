#  def_new_project_create***
@app.route('/new_project_create', methods=['GET'])
def new_project_create():
    '''
    Created : 2025-07-31T08:27:03.000Z

    description : add the new project into the project files
    '''
    route="/new_project_create"
    env.level+='-'
    print('\n'+env.level,white('route new_project_create() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route new_project_create() in ***app.py*** : >')
    global client_id
    global client_password
    global host
    global host_for_token
    global profil_name
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        name=request.args.get('name')
        name=name.replace('-','_')
        name=name.replace(' ','_')       
        print('\n name : ',name)         
        description=request.args.get('description')
        print('\n description : ',description)         
        working_dir=request.args.get('working_dir')
        print('\n working_dir : ',working_dir)            
        name=name.replace(' ','_')
        script_details={'name': name,'description' : description,"package_dir" : working_dir, "script_list":[] }
        with open('./code_projets/projets.txt','a+') as file:
              file.write(name+'\n')
        with open('./code_projets/'+name+'.txt','w') as file:
              file.write(json.dumps(script_details,sort_keys=True,indent=4, separators=(',', ': ')))     
        with open('./result/home_url.txt') as file:
            home_url=file.read()
        html_output='''<html><body><a href="'''+home_url+'''"><b><= back to home</b></a><br><br>
        <center><h3>OK NEW PROJECT ADDED TO LIST</h3></center>
        </body></html>
        ''';   
        env.level=env.level[:-1]
        return html_output 
