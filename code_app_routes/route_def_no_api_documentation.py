#  def_no_api_documentation***
@app.route('/no_api_documentation', methods=['GET'])
def no_api_documentation():
    '''
    Created : 2025-10-29T15:29:59.000Z

    description : display the NO API documentation available page
    '''
    route="/no_api_documentation"
    env.level+='-'
    print('\n'+env.level,white('route no_api_documentation() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route no_api_documentation() in ***app.py*** : >')
    global client_id
    global client_password
    global host
    global host_for_token
    global profil_name
    if not session.get('logged_in'):
        return render_template('login.html')
    else:       
        message1="NO API Documentation !"
        image="../static/images/nok.png" 
        message2="API Documentation is not public"
        message3="/"
        message4="Home"
        PAGE_DESTINATION="z_no_api_documentation for this product"
        page_name="z_no_api_documentation.html"
        loguer(env.level+' route END OF no_api_documentation() in ***app.py*** : >')
        # ===================================================================
        env.level=env.level[:-1]
        return render_template('main_index.html',route=route,USERNAME=session['user'],PAGE_DESTINATION=PAGE_DESTINATION,message1=message1,message2=message2,message3=message3,message4=message4,image=image,page_name=page_name)
        
