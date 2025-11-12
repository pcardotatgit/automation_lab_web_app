#  def_move_route_to_system***
@app.route('/move_route_to_system', methods=['GET'])
def move_route_to_system():
    '''
    Created : 2025-06-10T12:05:09.000Z

    description : move route in app folder to the system folder
    '''
    route="/move_route_to_system"
    env.level+='-'
    print()
    print(env.level,white('route move_route_to_system() in ***app.py*** : >',bold=True))
    loguer(env.level+' route move_route_to_system() in ***app.py*** : >')
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
        html_output=f'<h3>Do you really want to promote route : <br><br>{filename} to system route </h3><br>in directory <b>[ {scriptdir} ]</b><br><hr>';
        html_output=html_output+f'<form action="/ok_move_route_to_system" method="GET"><input type="text" name="new_name" value="{filename}"><input type="hidden" name="filename" value="{filename}"><input type="hidden" name="scriptdir" value="{scriptdir}"><input type="submit" value="Move"></form>'
        env.level=env.level[:-1]
        return html_output  
