#  def_rename_file***
@app.route('/rename_file', methods=['GET'])
def rename_file():
    '''
    Created : 2025-06-05T13:50:52.000Z

    description : got to rename script formular
    '''
    route="/rename_file"
    env.level+='-'
    print()
    print(env.level,white('route rename_file() in ***app.py*** : >',bold=True))
    loguer(env.level+' route rename_file() in ***app.py*** : >')
    print()
    global client_id
    global client_password
    global host
    global host_for_token
    global profil_name
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        filename=request.args.get('filename')
        filename=filename.replace('../','./')
        print()
        print('filename : ',filename)
        print()
        scriptdir=request.args.get('scriptdir')
        print()
        print('scriptdir : ',scriptdir)
        print()        
        html_output=f'<h3>Do you really want to rename : <br><br>{filename}</h3><br>in directory <b>[ {scriptdir} ]</b><br><hr>';
        html_output=html_output+f'<form action="/ok_rename_file" method="GET"><input type="text" name="new_name"><input type="hidden" name="filename" value="{filename}"><input type="hidden" name="scriptdir" value="{scriptdir}"><input type="submit" value="Rename"></form>'
        env.level=env.level[:-1]
        return html_output     
