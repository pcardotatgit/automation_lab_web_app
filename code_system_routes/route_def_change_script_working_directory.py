#  def_change_script_working_directory***
@app.route('/change_script_working_directory', methods=['GET'])
def change_script_working_directory():
    '''
    Created : 2025-06-07T14:25:35.000Z

    description : change the destination directory where to create the    script
    '''
    route="/change_script_working_directory"
    env.level+='-'
    print()
    print(env.level,white('route change_script_working_directory() in ***app.py*** : >',bold=True))
    loguer(env.level+' route change_script_working_directory() in ***app.py*** : >')
    print()
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        with open('./result/home_url.txt') as file:
            home_url=file.read()
        html_output='''<html><body><a href="'''+home_url+'''"><b><= back to home</b></a><br><br>
        <form action="/confirm_workingdir_change" method="GET">
        <b>Directory Name ( full path in disk ) : </b><input type="text"  id="directory" name="directory" /><br><br>
        <center><input type="submit" value="valid"/></center>
        </form>
        </body></html>
        ''';   
        env.level=env.level[:-1]
        return html_output
