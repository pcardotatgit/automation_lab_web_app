#  def_page_test***
@app.route('/page_test', methods=['GET'])
def page_test():
    '''
    Created : 2025-07-31T15:38:40.000Z

    description : 
    '''
    route="/page_test"
    env.level+='-'
    print('\n'+env.level,white('route page_test() in app.py  : >\n',bold=True))
    loguer(env.level+' route page_test() in app.py  : > ')
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
        PAGE_DESTINATION="z_page_test"
        page_name="z_page_test.html"
        # ===================================================================
        env.level=env.level[:-1]
        return render_template('main_index.html',route=route,USERNAME=session['user'],PAGE_DESTINATION=PAGE_DESTINATION,message1=message1,message2=message2,message3=message3,message4=message4,image=image,page_name=page_name)
        

