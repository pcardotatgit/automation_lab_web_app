#  def_ma_apis***
@app.route('/ma_apis', methods=['GET'])
def ma_apis():
    '''
    Created : 2025-10-25T19:49:26.000Z

    description : display malware analytics APIs
    '''
    route="/ma_apis"
    env.level+='-'
    print('\n'+env.level,white('route ma_apis() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route ma_apis() in ***app.py*** : >')
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
        PAGE_DESTINATION="z_ma_apis"
        page_name="z_ma_apis.html"
        loguer(env.level+' route END OF ma_apis() in ***app.py*** : >')
        # ===================================================================
        env.level=env.level[:-1]
        return render_template('main_index.html',route=route,USERNAME=session['user'],PAGE_DESTINATION=PAGE_DESTINATION,message1=message1,message2=message2,message3=message3,message4=message4,image=image,page_name=page_name)
        
