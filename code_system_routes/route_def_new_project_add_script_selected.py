#  def_new_project_add_script_selected***
@app.route('/new_project_add_script_selected', methods=['GET'])
def new_project_add_script_selected():
    '''
    Created : 2025-08-01T07:33:26.000Z

    description : add selected script to selected project 
    '''
    route="/new_project_add_script_selected"
    env.level+='-'
    print('\n'+env.level,white('route new_project_add_script_selected() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route new_project_add_script_selected() in ***app.py*** : >')
    global client_id
    global client_password
    global host
    global host_for_token
    global profil_name
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        script=request.args.get('script')
        print('\nscript name : ',script)   
        project=request.args.get('project')
        print('\nproject name : ',project)     
        with open('./code_projets/'+project+'.txt') as file:
            project_details=json.loads(file.read()) 
        project_details['script_list'].append(script)        
        with open('./code_projets/'+project+'.txt','w') as file:
            file.write(json.dumps(project_details,sort_keys=True,indent=4, separators=(',', ': ')))            
        with open('./result/home_url.txt') as file:
            home_url=file.read()
        html_output='''<html><body><a href="'''+home_url+'''"><b><= back to home</b></a><br><br>
        <center><h3>Script : '''+script+''' Added to Project : '''+project+'''</h3></center>
        <center><h3><a href="/project_details?name='''+project+'''">Back to project details</a></h3>
        </body></html>
        ''';                  
        env.level=env.level[:-1]
        return html_output 
