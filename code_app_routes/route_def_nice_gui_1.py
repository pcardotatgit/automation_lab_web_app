#  def_nice_gui_1***
@app.route('/nice_gui_1', methods=['GET'])
def nice_gui_1():
    '''
    Created : 2025-07-31T15:38:40.000Z

    description : display the nice gui example 1
    '''
    route="/nice_gui_1"
    env.level+='-'
    print('\n'+env.level,white('route nice_gui_1() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route nice_gui_1() in ***app.py*** : >')
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
        PAGE_DESTINATION="z_nice_gui_1"
        page_name="z_nice_gui_1.html"
        # ===================================================================
        env.level=env.level[:-1]
        return render_template('main_index.html',route=route,USERNAME=session['user'],PAGE_DESTINATION=PAGE_DESTINATION,message1=message1,message2=message2,message3=message3,message4=message4,image=image,page_name=page_name)
        
