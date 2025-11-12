#  def_remove_script_from_project***
@app.route('/remove_script_from_project', methods=['GET'])
def remove_script_from_project():
    '''
    Created : 2025-08-01T07:55:41.000Z

    description : remove selected script from project list
    '''
    route="/remove_script_from_project"
    env.level+='-'
    print('\n'+env.level,white('route remove_script_from_project() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route remove_script_from_project() in ***app.py*** : >')
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        script=request.args.get('script')
        print('\nscript name : ',script)   
        project=request.args.get('name')
        print('\nproject name : ',project)     
        with open('./code_projets/'+project+'.txt') as file:
            project_details=json.loads(file.read())            
        project_details['script_list'].remove(script)        
        with open('./code_projets/'+project+'.txt','w') as file:
            file.write(json.dumps(project_details,sort_keys=True,indent=4, separators=(',', ': ')))            
        with open('./result/home_url.txt') as file:
            home_url=file.read()
        html_output='''<html><body><a href="'''+home_url+'''"><b><= back to home</b></a><br><br>
        <center><h3>Script : '''+script+''' Removed Project : '''+project+'''</h3></center>
        <center><h3><a href="/project_details?name='''+project+'''">Back to project details</a></h3>
        </body></html>
        ''';                  
        env.level=env.level[:-1]
        return html_output 
