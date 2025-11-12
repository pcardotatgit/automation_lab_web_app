#  def_umbrella_apis***
@app.route('/umbrella_apis', methods=['GET'])
def umbrella_apis():
    '''
    Created : 2025-10-25T20:22:39.000Z

    description : display umbrella api choices
    '''
    route="/umbrella_apis"
    env.level+='-'
    print('\n'+env.level,white('route umbrella_apis() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route umbrella_apis() in ***app.py*** : >')
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
        PAGE_DESTINATION="z_umbrella_apis"
        page_name="z_umbrella_apis.html"
        loguer(env.level+' route END OF umbrella_apis() in ***app.py*** : >')
        # ===================================================================
        env.level=env.level[:-1]
        return render_template('main_index.html',route=route,USERNAME=session['user'],PAGE_DESTINATION=PAGE_DESTINATION,message1=message1,message2=message2,message3=message3,message4=message4,image=image,page_name=page_name)
        
