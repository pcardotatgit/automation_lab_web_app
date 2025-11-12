#  def_xdr_get_token***
@app.route('/xdr_get_token', methods=['GET'])
def xdr_get_token():
    '''
    Created : 2025-11-05T18:18:14.000Z

    description : display XDR Get token API information
    '''
    route="/xdr_get_token"
    env.level+='-'
    print('\n'+env.level,white('route xdr_get_token() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route xdr_get_token() in ***app.py*** : >')
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
        PAGE_DESTINATION="z_xdr_get_token"
        page_name="z_xdr_get_token.html"
        loguer(env.level+' route END OF xdr_get_token() in ***app.py*** : >')
        # ===================================================================
        env.level=env.level[:-1]
        return render_template('main_index.html',route=route,USERNAME=session['user'],PAGE_DESTINATION=PAGE_DESTINATION,message1=message1,message2=message2,message3=message3,message4=message4,image=image,page_name=page_name)
        
