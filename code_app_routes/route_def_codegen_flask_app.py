#  def_codegen_flask_app***
@app.route('/codegen_flask_app', methods=['GET'])
def codegen_flask_app():
    '''
    Created : 2025-09-22T07:21:17.000Z

    description : display the SQLITE DB Formular
    '''
    route="/codegen_flask_app"
    env.level+='-'
    print('\n'+env.level,white('route codegen_flask_app() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route codegen_flask_app() in ***app.py*** : >')
    global client_id
    global client_password
    global host
    global host_for_token
    global profil_name
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        PAGE_DESTINATION="z_codegen_flask_app"
        page_name="z_codegen_flask_app.html"
        loguer(env.level+' route END OF codegen_flask_app() in ***app.py*** : >')
        # ===================================================================
        env.level=env.level[:-1]
        return render_template('main_index.html',route=route,USERNAME=session['user'],PAGE_DESTINATION=PAGE_DESTINATION,page_name=page_name)
        
