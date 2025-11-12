#  def_check_connexion_to_tenant***
@app.route('/check_connexion_to_tenant', methods=['GET'])
def check_connexion_to_tenant():
    '''
    Created : 2025-05-27T15:49:39.000Z

    description : take API credential for the web formular and save into a text profile into the ./profiles subfolder. And test the Connection to the destination tenant
    '''
    route="/check_connexion_to_tenant"
    env.level+='-'
    print()
    print(env.level,white('route check_connexion_to_tenant() in ***app.py*** : >',bold=True))
    loguer(env.level+' route check_connexion_to_tenant() in ***app.py*** : >')
    print()
    global api_key
    global api_secret
    global host
    global orgID
    global profil_name
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        api_key=request.args.get('api_key')
        print('api_key : ',api_key)
        orgID=request.args.get('orgID')
        print('orgID : ',orgID);
        host=request.args.get('host')
        print()
        print('host : ',host)
        print()
        profil_name=request.args.get('profil_name')
        print('profil_name : ',profil_name);
        api_secret=request.args.get('api_secret')
        print()
        print('api_secret : ',api_secret)     
        print()
        with open('./keys/config.txt','w') as file:
            line_to_save='{\n'
            line_to_save+='profil_name='+profil_name+'\n'
            line_to_save+='api_key='+api_key+'\n'
            line_to_save+='api_secret='+api_secret+'\n'
            line_to_save+='host='+host+'\n'
            line_to_save+='orgID='+orgID+'\n'
            line_to_save+='}\n'
            file.write(line_to_save)
        profile_file_name='./profiles/'+profil_name.replace(' ','_')+'.txt'
        with open(profile_file_name,'w') as file2:
            file2.write(line_to_save)
        '''
        HERE CHECK THE CONNEXION TO THE DESTINATION TENANT
        print(magenta('--> CALL  A SUB FUNCTION :',bold=True))
        result=check_XDR_cnx(host_for_token,client_id,client_password)
        '''
        message1="Current loaded XDR profil is : "+profil_name
        result=1
        if result==1:        
            image="../static/images/ok.png" 
            message2="Connexion to XDR Tenant is Okay !"
            message3="#portfolio"
            message4="Select and Incident and create it" 
        elif result==2:
            image="../static/images/nok.png" 
            message2="Cannot get Token from XDR tenant"   
            message3="#api_client"
            message4="Configure XDR API Client"
        else:
            image="../static/images/nok.png" 
            message2="Connection to XDR tenant Failed"
            message3="#api_client"
            message4="Configure XDR API Client"
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
        with open('./keys/config.txt','r') as file:
            text_content=file.read()        
        api_key,api_secret,host,orgID,profil_name = parse_config(text_content)
        PAGE_DESTINATION="index"
        page_name="index.html"
        env.level=env.level[:-1]
        return render_template('main_index.html',USERNAME=session['user'],PAGE_DESTINATION=PAGE_DESTINATION,page_name=page_name,image=image,message1=message1,message2=message2,profiles_list=profiles_list,message3=message3,message4=message4,profil_name=profil_name,route=route) 

