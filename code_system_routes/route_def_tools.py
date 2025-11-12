# def_tools***
@app.route('/tools', methods=['GET'])
def tools():
    env.level+='-'
    print()
    print(env.level,white('route tools() : >',bold=True))
    loguer(env.level+' route tools() : >')
    print()
    route="/tools"
    global client_id
    global client_password
    global host
    global host_for_token
    global profil_name
    global access_token
    if not session.get('logged_in'):
        env.level=env.level[:-1]
        return render_template('login.html')
    else:
        print('client_id : ',client_id)
        print('client_password : ',client_password);
        print('host : ',host)
        if "https://private.intel.eu.amp.cisco.com" in host:
            host_for_token="https://visibility.eu.amp.cisco.com"
        elif "https://private.intel.amp.cisco.com" in host:
            host_for_token="https://visibility.amp.cisco.com"
        else:
            host_for_token="https://visibility.apjc.amp.cisco.com"
        print('host_for_token : ',host_for_token)
        print('profil_name : ',profil_name);
        #print("incidents : \n",yellow(result,bold=True))
        message1="Current XDR tenant profile : "+profil_name
        image="../static/images/toolbox.png" 
        message2="XDR Tool Library. Select the tool category you want to invoke"
        message3="/"
        message4="Select a tool Category"
        PAGE_DESTINATION="tools"  
        env.level=env.level[:-1]
        return render_template('main_index.html',route=route,USERNAME=session['user'],PAGE_DESTINATION=PAGE_DESTINATION,image=image,message1=message1,message2=message2,message3=message3,message4=message4)
        

