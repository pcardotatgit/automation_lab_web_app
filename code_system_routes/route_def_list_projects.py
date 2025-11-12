#  def_list_projects***
@app.route('/list_projects', methods=['GET'])
def list_projects():
    '''
    Created : 2025-09-14

    description : list current scripts project in projects library
    '''
    route="/list_projects"
    env.level+='-'
    print('\n'+env.level,white('route list_projects() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route list_projects() in ***app.py*** : >')
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        with open('./result/home_url.txt') as file:
            home_url=file.read()
        html_output='<html><body><a href="'+home_url+'"><b><= back to home</b></a><br>';        

        html_output=html_output+'<h4>Projects :</h4><table border="1"><tbody>';
        with open('./code_projets/projets.txt') as file:
            text_content=file.read()            
        files =text_content.split('\n')  
        for file in files:
            if file!='':
                # print(' file : ',yellow(file,bold=True)) 
                with open('./code_projets/'+file+'.txt') as file2:
                    projet_details=json.loads(file2.read())
                #description=projet_details['description']
                html_output=html_output+'<tr><td><li><b><a href="/project_details?name='+file+'">'+file+'</a></b></li></td><td><li>'+projet_details['description']+'</li></td><td><a href="/project_remove">REMOVE</a></td></tr>'    
        html_output=html_output+'</tbody></table><br><a href="/stop">Click here to stop the App  </a></body></html>';            
        env.level=env.level[:-1]
        return html_output
