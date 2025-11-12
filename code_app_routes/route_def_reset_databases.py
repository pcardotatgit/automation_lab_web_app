#  def_reset_databases***
@app.route('/reset_databases', methods=['GET'])
def reset_databases():
    '''
    Created : 2025-11-11T08:02:29.000Z

    description : reset every databases
    '''
    route="/reset_databases"
    env.level+='-'
    print('\n'+env.level,white('route reset_databases() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route reset_databases() in ***app.py*** : >')
    global client_id
    global client_password
    global host
    global host_for_token
    global profil_name
    if not session.get('logged_in'):
        return render_template('login.html')
    else:    
        result=reset_every_databases()
        message1="Databases Reseted"
        image="../static/images/ok.png" 
        message2="Every databases have been reseted"
        message3="/"
        message4="Home"
        PAGE_DESTINATION="operation_done"
        page_name="operation_done.html"
        loguer(env.level+' route END OF reset_databases() in ***app.py*** : >')
        # ===================================================================
        env.level=env.level[:-1]
        return render_template('main_index.html',route=route,USERNAME=session['user'],PAGE_DESTINATION=PAGE_DESTINATION,message1=message1,message2=message2,message3=message3,message4=message4,image=image,page_name=page_name)
        
