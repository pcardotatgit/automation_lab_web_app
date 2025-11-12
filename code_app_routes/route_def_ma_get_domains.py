#  def_ma_get_domains***
@app.route('/ma_get_domains', methods=['GET'])
def ma_get_domains():
    '''
    Created : 2025-10-25T19:59:59.000Z

    description : Malware Analytics Get domains attached to a sh256
    '''
    route="/ma_get_domains"
    env.level+='-'
    print('\n'+env.level,white('route ma_get_domains() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route ma_get_domains() in ***app.py*** : >')
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
        PAGE_DESTINATION="z_ma_get_domains"
        page_name="z_ma_get_domains.html"
        loguer(env.level+' route END OF ma_get_domains() in ***app.py*** : >')
        # ===================================================================
        env.level=env.level[:-1]
        return render_template('main_index.html',route=route,USERNAME=session['user'],PAGE_DESTINATION=PAGE_DESTINATION,message1=message1,message2=message2,message3=message3,message4=message4,image=image,page_name=page_name)
        
