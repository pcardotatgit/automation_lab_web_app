# def_index***
@app.route('/', methods=['GET'])
def index():
    '''
    Created : 2025-05-25T14:52:34.000Z

    description : for displaying the landing page where users land just after login
    '''
    route="/"
    env.level+='-'
    print()
    print(env.level,white('route index() in ***app.py*** : >',bold=True))
    loguer(env.level+' route index() in ***app.py*** : >')
    print()
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
        if method=="config.txt":
            with open('./keys/config.txt','r') as file:
                text_content=file.read()
            api_key,network_id,host,orgID,profil_name = parse_config(text_content)        
        files =[file for file in os.listdir('./profiles')]
        profiles_dict={}
        profiles_list=[]
        description_list=[]
        print()
        for file in files:
            print(file) 
            if file !='.txt':
                profiles_list.append(file)        
        print(yellow(profiles_list,bold=True))        
        result=1
        if result==1:        
            image="../static/images/ok.png" 
            message1="message1 to customize in def index()"            
            message2="message2 to customize in def index()"
            message3="/route_to_call"
            message4="message4 to customize in def index()"             
        elif result==2:
            image="../static/images/nok.png" 
            message1="message1"            
            message2="message2"
            message3="#message3"
            message4="message4"            
        else:
            image="../static/images/nok.png" 
            message1="message1 to customize in def index()"            
            message2="message2 to customize in def index()"
            message3="/route_to_call"
            message4="message4 to customize in def index()"                 
        PAGE_DESTINATION="index"
        page_name="index.html"
        #env.level=env.level[:-1]
        return render_template('main_index.html',USERNAME=session['user'],PAGE_DESTINATION=PAGE_DESTINATION,image=image,message1=message1,message2=message2,message3=message3,message4=message4,page_name=page_name,route=route,profiles_list=profiles_list,profil_name=profil_name)       


