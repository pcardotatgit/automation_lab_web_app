#  def_backup_application***
@app.route('/backup_application', methods=['GET'])
def backup_application():
    '''
    Created : 2025-09-11T14:57:16.000Z
    description : trigger an application code backup
    '''
    route="/backup_application"
    env.level+='-'
    print('\n'+env.level,white('route backup_application() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route backup_application() in ***app.py*** : >')
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        os.system("python backup_app_system_code.py 1")
        with open('./result/home_url.txt') as file:
            home_url=file.read()
        html_output='''<html><body><br><a href="'''+home_url+'''"><b><= back to home</b></a><br><br>
        <center><h3>APPLICATION CODE BACKUP DONE check ./code_backup </h3></center>
        <center><h3>A directory structure PLUS a zip file had been created</h3></center>
        </body></html>
            ''';
    env.level=env.level[:-1]
    return html_output 
  
