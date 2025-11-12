#  def_codegen_get_input_variable***
@app.route('/codegen_get_input_variable', methods=['GET'])
def codegen_get_input_variable():
    '''
    Created : 2025-09-22T07:47:39.000Z

    description : display formular for get input variable code generator
    '''
    route="/codegen_get_input_variable"
    env.level+='-'
    print('\n'+env.level,white('route codegen_get_input_variable() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route codegen_get_input_variable() in ***app.py*** : >')
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
        PAGE_DESTINATION="z_codegen_get_input_variable"
        page_name="z_codegen_get_input_variable.html"
        loguer(env.level+' route END OF codegen_get_input_variable() in ***app.py*** : >')
        # ===================================================================
        env.level=env.level[:-1]
        return render_template('main_index.html',route=route,USERNAME=session['user'],PAGE_DESTINATION=PAGE_DESTINATION,message1=message1,message2=message2,message3=message3,message4=message4,image=image,page_name=page_name)
        
