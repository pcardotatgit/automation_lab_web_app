#  def_send_api_call***
@app.route('/send_api_call', methods=['GET'])
def send_api_call():
    '''
    Created : 2025-11-06
    description : Send the API call to URL Endpoint with the passed data
    '''
    route="/send_api_call"
    env.level+='-'
    print()
    print(env.level,white('route send_api_call() in app.py  : >\n',bold=True))
    loguer(env.level+' route send_api_call() in app.py  : > ')
    print()
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        global use_simulator
        base_url=request.args.get('base_url')
        print('\nbase_url : ',yellow(base_url,bold=True))
        name=request.args.get('name')
        print()
        print('name : ',yellow(name,bold=True))
        relative_url=request.args.get('relative_url')
        print()
        print('relative_url : ',yellow(relative_url,bold=True))
        api_documentation=request.args.get('api_docummentation')
        print()
        print('api_documentation : ',yellow(api_documentation,bold=True))
        method=request.args.get('method')
        print()
        print('method : ',yellow(method,bold=True))
        short_description=request.args.get('short_description')
        print()
        print('short_description : ',yellow(short_description,bold=True))
        payload=request.args.get('payload')
        payload=payload.replace('\n','')
        payload=payload.replace('\r','')
        payload=payload.replace('  ',' ')
        payload=payload.replace('  ',' ')
        payload=payload.replace('  ',' ')
        payload=payload.replace('  ',' ')
        print()
        print('payload : ',yellow(payload,bold=True))
        header=request.args.get('header')
        header=header.replace('\n','')
        header=header.replace('\r','')
        header=header.replace('  ',' ')
        header=header.replace('  ',' ')
        header=header.replace('  ',' ')
        header=header.replace('  ',' ')
        print()
        print('header : ',yellow(header,bold=True))
        body=request.args.get('body')
        body=body.replace('\n','')
        body=body.replace('\r','')
        body=body.replace('  ',' ')
        body=body.replace('  ',' ')
        body=body.replace('  ',' ')
        body=body.replace('  ',' ')
        print()
        print('body : ',yellow(body,bold=True))
        params=request.args.get('params')
        params=params.replace('\n','***')
        params=params.replace('\r','')
        params=params.replace('  ',' ')
        params=params.replace('  ',' ')
        params=params.replace('  ',' ')
        params=params.replace('  ',' ')
        print()
        print('params : ',yellow(params,bold=True))
        
        parameters=request.args.get('parameters')
        parameters=parameters.replace('\n','***')
        parameters=parameters.replace('\r','')
        parameters=parameters.replace('  ',' ')
        parameters=parameters.replace('  ',' ')
        parameters=parameters.replace('  ',' ')
        parameters=parameters.replace('  ',' ')
        print()
        print('parameters : ',yellow(parameters,bold=True))
        authentication_profile=request.args.get('authentication_profile')
        print()
        print('authentication_profile : ',yellow(authentication_profile,bold=True))
        filename='./api_calls_history/'+name+'_'+date_time_for_file_name()+'.txt'  # http://127.0.0.1:4000/code_edit?code=def_date_time_for_file_name.py&type=function
        with open(filename,'w') as file:
            file.write('name=:'+name+'\n')
            file.write('base_url=:'+base_url+'\n')
            file.write('relative_url=:'+relative_url+'\n')
            file.write('api_documentation=:'+api_documentation+'\n')
            file.write('method=:'+method+'\n')
            file.write('short_description=:'+short_description+'\n')
            file.write('payload=:'+payload+'\n')
            file.write('header=:'+header+'\n')
            file.write('body=:'+body+'\n')
            file.write('params=:'+params+'\n')
            file.write('parameters=:'+parameters+'\n')
            file.write('authentication_profile=:'+authentication_profile+'\n')
        with open('./result/last_api_call.txt','w') as file:
            file.write(filename)
        # Select Authentication Profile
        #api_key=''
        if authentication_profile!="saved_token":
            username,password,api_key=select_profile_function(authentication_profile) 
            
            authentication_dict={
                'username':username,
                'password':password,
                'api_key':api_key
            }
            print("\nauthentication_dict : ",yellow(authentication_dict,bold=True))  
        else:
            with open('./profiles/saved_token.txt') as file:
                api_key=file.read()
        if "@" in base_url:
            chunks=base_url.split('@')
            i=0
            new_chunks=[]
            for chunk in chunks:
                if 'https' in chunk or 'HTTPS' in chunk:
                    chunk=chunk.replace('https://','')
                    chunk=chunk.replace('HTTPS://','')
                    protocol='https'
                else:
                    chunk=chunk.replace('http://','')
                    chunk=chunk.replace('HTTP://','')      
                    protocol='http'                    
                print(chunk)    
                if i==0:
                    creds=chunk.split(':')
                    ii=0
                    new_cred_words=[]
                    for cred_word in creds:
                        if '$$' in cred_word:
                            mot=cred_word.replace('$$','')
                            mot=mot.replace('***','')                        
                        print(cyan(mot,bold=True))
                        new_cred_words.append(authentication_dict[mot])
                        ii+=1
                    print(yellow(new_cred_words,bold=True))
                    new_chunks.append(protocol+'://'+new_cred_words[0]+':'+new_cred_words[1]+'@')
                elif i==1:
                   new_chunks.append(chunk)
                i+=1
            if use_simulator==1:
                base_url=new_chunks[0].replace('https:','http:')+'localhost:4000'
            else:
                base_url=new_chunks[0]+new_chunks[1]
        else:
            if use_simulator==1:
                base_url='http://localhost:4000'

        print()
        print('final base_url to use : ',cyan(base_url,bold=True))                      
        additionnal_get_params='' # parameters at the end of the URL ?parm1=xxx?param2=yyy
        if body=='':
            body_json={}
        else:
            body_json=json.loads(body)
        if body_json == {"grant_type": "client_credentials"}:
            header_json=json.loads(header)
            result,response_txt=send_api_call_for_oauth_token(base_url,relative_url,client_id,client_password,header_json,body_json) # http://127.0.0.1:4000/code_edit?code=def_send_api_call_for_oauth_token.py&type=function
        elif payload == {"grant_type": "client_credentials"}:
            header_json=json.loads(header)
            result,response_txt=send_api_call_for_oauth_token(base_url,relative_url,client_id,client_password,header_json,body_json) # http://127.0.0.1:4000/code_edit?code=def_send_api_call_for_oauth_token.py&type=function
        else:
            print("\nOK SEND CALL (x166): ") 
            if api_key==None:
                api_key='xxx'
            print('api_key :',red(api_key,bold=True))       
            result,response_txt=send_api_call_function(method,base_url,relative_url,additionnal_get_params,header,payload,body,params,parameters,api_key) # http://127.0.0.1:4000/code_edit?code=def_send_api_call_function.py&type=function
        # read the first 200 lines of the JSON result
        with open('./json_results/json_result.json') as file:
            lines=file.read().split('\n')
        print('  lines : \n',lines)
        response_txt=''
        ii=0
        for line in lines:
            response_txt=response_txt+line+'\n'
            ii+=1
            if ii>200:
                response_txt=response_txt+'..... Rest of response is not shown... it was too long \n\n=> You can click on the [ Display in Tree Graph ] button  to see the entire content'
                break
        # #########################################################
        if result==1:
            image="../static/images/ok.png"
            message1=response_txt
            message2="Connexion to XDR Tenant is Okay !"
            message3="#portfolio"
            message4="Button Message"
            PAGE_DESTINATION="z_api_call_result"
            page_name="z_api_call_result.html"
            env.level=env.level[:-1]
            return render_template('main_index.html',route=route,USERNAME=session['user'],PAGE_DESTINATION=PAGE_DESTINATION,message1=message1,message2=message2,message3=message3,message4=message4,image=image,page_name=page_name)
        else:
            image="../static/images/nok.png"
            message1="Operation Failed"
            message2="An Error Occured"
            message3="/"
            message4="Home"
            PAGE_DESTINATION="operation_done"
            page_name="operation_done.html"
            loguer(env.level+' route send_api_call() in app.py  : > ')
            env.level=env.level[:-1]
            return render_template('main_index.html',route=route,USERNAME=session['user'],PAGE_DESTINATION=PAGE_DESTINATION,message1=message1,message2=message2,message3=message3,message4=message4,image=image,page_name=page_name)
        

