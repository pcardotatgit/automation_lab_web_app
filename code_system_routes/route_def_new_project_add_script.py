#  def_new_project_add_script***
@app.route('/new_project_add_script', methods=['GET'])
def new_project_add_script():
    '''
    Created : 2025-08-01T07:16:51.000Z

    description : select a script from library and add it to project
    '''
    route="/new_project_add_script"
    env.level+='-'
    print('\n'+env.level,white('route new_project_add_script() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route new_project_add_script() in ***app.py*** : >')
    global client_id
    global client_password
    global host
    global host_for_token
    global profil_name
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        with open('./result/home_url.txt') as file:
            home_url=file.read()
        name=request.args.get('name')
        print('\n name : ',name)  
        html_output='<html><body><a href="'+home_url+'"><b><= back to home</b></a><h3>Select a script to add to project:</h3><ul>';
        with open('./code_architecture/imported_scripts.txt') as file:
            for line in file:
                # print(' file : ',yellow(line,bold=True)) 
                html_output=html_output+'<li><b><a href="/new_project_add_script_selected?script='+line+'&project='+name+'">'+line+'</a></b></li>'
        env.level=env.level[:-1]
        html_output=html_output+'\n</ul></body><html>'
        return html_output
           