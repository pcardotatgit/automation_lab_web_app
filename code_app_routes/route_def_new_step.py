#  def_new_step***
@app.route('/new_step', methods=['GET'])
def new_step():
    '''
    Created : 2025-10-29T22:20:51.000Z

    description : display the add a new step in workflows formular
    '''
    route="/new_step"
    env.level+='-'
    print('\n'+env.level,white('route new_step() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route new_step() in ***app.py*** : >')
    global client_id
    global client_password
    global host
    global host_for_token
    global profil_name
    if not session.get('logged_in'):
        return render_template('login.html')
    else:   
        workflow_name="Automation Challenge"
        PAGE_DESTINATION="z_new_step"
        page_name="z_new_step.html"
        loguer(env.level+' route END OF new_step() in ***app.py*** : >')
        # ===================================================================
        env.level=env.level[:-1]
        return render_template('main_index.html',route=route,USERNAME=session['user'],PAGE_DESTINATION=PAGE_DESTINATION,page_name=page_name,workflow_name=workflow_name)
        
