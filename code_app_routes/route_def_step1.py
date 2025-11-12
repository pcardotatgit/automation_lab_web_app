#  def_step1***
@app.route('/step1', methods=['GET'])
def step1():
    '''
    Created : 2025-10-25T14:03:52.000Z

    description : STEP 1 Get computers
    '''
    route="/step1"
    env.level+='-'
    print('\n'+env.level,white('route step1() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route step1() in ***app.py*** : >')
    global client_id
    global client_password
    global host
    global host_for_token
    global profil_name
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        image="../static/images/toolbox.png" 
        message2="Message 2 :"
        message3="/Message 3"
        message4="Message 4 in button"
        PAGE_DESTINATION="z_step1"
        page_name="z_step1.html"
        loguer(env.level+' route END OF step1() in ***app.py*** : >')
        # ===================================================================
        env.level=env.level[:-1]
        return render_template('main_index.html',route=route,USERNAME=session['user'],PAGE_DESTINATION=PAGE_DESTINATION,message1=message1,message2=message2,message3=message3,message4=message4,image=image,page_name=page_name)
        
