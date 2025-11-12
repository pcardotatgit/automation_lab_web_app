#  def_introduction***
@app.route('/introduction', methods=['GET'])
def introduction():
    '''
    Created : 2025-11-09T22:16:40.000Z

    description : challenge presentation
    '''
    route="/introduction"
    env.level+='-'
    print('\n'+env.level,white('route introduction() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route introduction() in ***app.py*** : >')
    global client_id
    global client_password
    global host
    global host_for_token
    global profil_name
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        # ===================================================================       
        '''
        # GET variable from calling web page
        profil_name='./profiles/'+request.args.get('profil_name')
        print()
        print('profil_name : ',profil_name)        
        # POST variable 
        keyword = request.form['keyword']
        print()
        print('keyword : ',keyword)
        
        # API TOKEN
        with open('ctr_token.txt','r') as file0:
            access_token=file0.read()
            
        action=request.args.get('action')
        print()
        print('action: ',action)
        print()
        if action=="copy":
            do something
            
        #CALL  A SUB FUNCTION
        print()   
        print(magenta('--> CALL  A SUB FUNCTION :',bold=True)) 
        '''        
        # Prepare the resulting Next Web Page
        result=1
        if result==1:        
            image="../static/images/ok.png" 
            message1="Title"
            message2="Connexion to XDR Tenant is Okay !"
            message3="#portfolio"
            message4="Button Message"            
        elif result==2:
            image="../static/images/ok.png" 
            message1="Title"
            message2="Connexion to XDR Tenant is Okay !"
            message3="#portfolio"
            message4="Button Message"              
        else:
            image="../static/images/ok.png" 
            message1="Title"
            message2="Connexion to XDR Tenant is Okay !"
            message3="#portfolio"
            message4="Button Message"              
        message1="Message 1 :"
        image="../static/images/toolbox.png" 
        message2="Message 2 :"
        message3="/Message 3"
        message4="Message 4 in button"
        PAGE_DESTINATION="z_introduction"
        page_name="z_introduction.html"
        loguer(env.level+' route END OF introduction() in ***app.py*** : >')
        # ===================================================================
        env.level=env.level[:-1]
        return render_template('main_index.html',route=route,USERNAME=session['user'],PAGE_DESTINATION=PAGE_DESTINATION,message1=message1,message2=message2,message3=message3,message4=message4,image=image,page_name=page_name)
        
