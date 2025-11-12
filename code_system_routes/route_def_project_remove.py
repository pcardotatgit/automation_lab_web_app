#  def_project_remove***
@app.route('/project_remove', methods=['GET'])
def project_remove():
    '''
    Created : 2025-09-14T13:27:26.000Z
    description : instruction for removing a project from the project list
    '''
    route="/project_remove"
    env.level+='-'
    print('\n'+env.level,white('route project_remove() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route project_remove() in ***app.py*** : >')
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        with open('./result/home_url.txt') as file:
            home_url=file.read()
        html_output='<html><body><a href="'+home_url+'"><b><= back to home</b></a><h2>For Now for deleting a project in the list :</h2><ul><li>Edit ./code_projets/project.txt and remove the project name</li><li>Delete the project subfolder</li></ul></body></html>';
        env.level=env.level[:-1]
        return html_output
