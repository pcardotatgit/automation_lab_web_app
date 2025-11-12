#  def_project_details***
@app.route('/project_details', methods=['GET'])
def project_details():
    '''
    Created : 2025-08-01T06:24:48.000Z

    description : display project details
    '''
    route="/project_details"
    env.level+='-'
    print('\n'+env.level,white('route project_details() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route project_details() in ***app.py*** : >')
    global client_id
    global client_password
    global host
    global host_for_token
    global profil_name
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        name=request.args.get('name')
        print('\nproject name : ',name)       
        with open('./result/home_url.txt') as file:
            home_url=file.read()
        with open('./code_projets/'+name+'.txt') as file:
            project_details=json.loads(file.read())
        
        html_output='''<html><body><a href="'''+home_url+'''"><b><= back to home</b></a><br><br>
        <form action="/new_project_update" method="GET">
        <b>Projectname : </b><input type="text"  id="route_name" name="name" value="'''+project_details['name']+'''"/><br><br>
        <b>package directory location : </b><input type="text"  id="working_dir" name="working_dir" size= "80" value="'''+project_details['package_dir']+'''"/><br><br>
        <b>Project description</b><br>
        <textarea id="description" name="description" rows="5" cols="50">'''+project_details['description']+'''</textarea><br>
        </form>'''
        html_output=html_output+'<h4>project scripts :</h4><table border="1"><tbody>';
        for script in project_details['script_list']:
            html_output=html_output+'<tr><td><li><b><a href="/goto_script_B?script='+script+'&type=route">'+script+'</a></b></li></b></td><td><li><b><a href="/remove_script_from_project?script='+script+'&name='+name+'">Remove</a></b></li></td></tr>'
        html_output=html_output+''
        html_output=html_output+'</tbody></table><br><form action="/new_project_add_script" method="get"><input type="hidden" name="name" value="'+name+'"><input type="submit" value="Add a new script to project"><br><br><b><a href="/stop">Click here to stop the App  </a></b></body><html>'''    
        env.level=env.level[:-1]
        return html_output 