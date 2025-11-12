#  def_umbrella_get_dns_activity***
@app.route('/umbrella_get_dns_activityb', methods=['GET'])
def umbrella_get_dns_activityb():
    '''
    Created : 2025-10-26T08:32:01.000Z

    description : Umbrella API v2 get DNS activity API
    '''
    route="/umbrella_get_dns_activity"
    env.level+='-'
    print('\n'+env.level,white('route umbrella_get_dns_activityb() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route umbrella_get_dns_activityb() in ***app.py*** : >')
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
        PAGE_DESTINATION="z_umbrella_get_dns_activity"
        page_name="z_umbrella_get_dns_activity.html"
        loguer(env.level+' route END OF umbrella_get_dns_activity() in ***app.py*** : >')
        # ===================================================================
        env.level=env.level[:-1]
        return render_template('main_index.html',route=route,USERNAME=session['user'],PAGE_DESTINATION=PAGE_DESTINATION,message1=message1,message2=message2,message3=message3,message4=message4,image=image,page_name=page_name)
        
