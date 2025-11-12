#  def_cse_get_events***
@app.route('/cse_get_events', methods=['GET'])
def cse_get_events():
    '''
    Created : 2025-10-25T17:38:08.000Z

    description : CSE get events
    '''
    route="/cse_get_events"
    env.level+='-'
    print('\n'+env.level,white('route cse_get_events() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route cse_get_events() in ***app.py*** : >')
    global client_id
    global client_password
    global host
    global host_for_token
    global profil_name
    if not session.get('logged_in'):
        return render_template('login.html')
    else: 
        message1="Message 1 :"
        image="../static/images/toolbox.png" 
        message2="Message 2 :"
        message3="/Message 3"
        message4="Message 4 in button"
        PAGE_DESTINATION="z_cse_get_events"
        page_name="z_cse_get_events.html"
        loguer(env.level+' route END OF cse_get_events() in ***app.py*** : >')
        # ===================================================================
        env.level=env.level[:-1]
        return render_template('main_index.html',route=route,USERNAME=session['user'],PAGE_DESTINATION=PAGE_DESTINATION,message1=message1,message2=message2,message3=message3,message4=message4,image=image,page_name=page_name)
        
