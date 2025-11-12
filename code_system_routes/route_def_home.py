# def_home***
@app.route('/')
def home():
    env.level='[-'
    print()
    print(env.level,white('route home() : >',bold=True))
    loguer(env.level+' route home() : >')
    print()
    route="/"
    global client_id
    global client_password
    global host
    global host_for_token
    global profil_name
    if not session.get('logged_in'):
        env.level=env.level[:-1]
        return render_template('login.html')
    else:
        print()
        print(yellow("- OK Logged In",bold=True))
        print()
        result=1
        if result==1:        
            image="../static/images/ok.png" 
            message1="message1"            
            message2="message2"
            message3="#message3"
            message4="message4"            
        elif result==2:
            image="../static/images/nok.png" 
            message1="message1"            
            message2="message2"
            message3="#message3"
            message4="message4"            
        else:
            image="../static/images/nok.png" 
            message1="message1"            
            message2="message2"
            message3="#message3"
            message4="message4"                 
        PAGE_DESTINATION="home"
        page_name="home.html"
        #env.level=env.level[:-1]
        return render_template('main_index.html',USERNAME=session['user'],PAGE_DESTINATION=PAGE_DESTINATION,image=image,message1=message1,message2=message2,message3=message3,message4=message4,page_name=page_name,route=route)       

        
