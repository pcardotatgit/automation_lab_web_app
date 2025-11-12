#  def_analyse_logs***
@app.route('/analyse_logs', methods=['GET'])
def analyse_logs():
    '''
    Created : 2025-07-19T19:56:25.000Z

    description : read log and create a dtree vie
    '''
    route="/analyse_logs"
    env.level+='-'
    print('\n'+env.level,white('route analyse_logs() in ***app.py*** : >\n',bold=True))
    #loguer(env.level+' route analyse_logs() in ***app.py*** : >')
    global client_id
    global client_password
    global host
    global host_for_token
    global profil_name
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        subprocess.run(["python", "analyse_application_logs.py"])
        with open('./templates/log.html') as file:
            html_output=file.read()
        env.level=env.level[:-1]
        return html_output
