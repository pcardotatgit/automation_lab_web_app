#  def_select_api_call_and_send_it***
@app.route('/select_api_call_and_send_it', methods=['GET'])
def select_api_call_and_send_it(api_call_name):
    '''
    Created : 2025-11-03T10:27:03.000Z

    description : Select an API call in database by name, send it and save the result in ./result
    
    how to call it : result,response_txt=select_api_call_and_send_it(api_call_name)
    '''
    route="/select_api_call_and_send_it"
    env.level+='-'
    print('\n'+env.level,white('route select_api_call_and_send_it() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route select_api_call_and_send_it() in ***app.py*** : >')
    global use_simulator
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        database = "api_calls"
        '''
        database = os.getcwd()+'/z_bases/'+database
        database=database.replace("\\","/")   
        '''
        table = "api_calls"
        print("\ndatabase : ",database)
        table="api_calls"
        print("\ntable : ",table)
        where_clause=f'where name = "{api_call_name}"'
        entry_list=sqlite_db_select_entry(database,table,where_clause)
        print("\nentry_list : \n",entry_list)                    
        name=entry_list[0][1]
        print('\nname : ',yellow(name,bold=True))
        print()     
        base_url=entry_list[0][2]
        print('\nbase_url : ',yellow(base_url,bold=True))
        print()
        relative_url=entry_list[0][3]
        if '$' in relative_url:
            relative_url=replace_variable(relative_url)        
        print('relative_url : ',yellow(relative_url,bold=True))
        api_documentation=entry_list[0][4]
        print()
        print('api_documentation : ',yellow(api_documentation,bold=True))
        method=entry_list[0][5]
        print()
        print('method : ',yellow(method,bold=True))
        short_description=entry_list[0][6]
        print()
        print('short_description : ',yellow(short_description,bold=True))
        payload=entry_list[0][7]
        payload=payload.replace('\n','')
        payload=payload.replace('\r','')
        payload=payload.replace('  ',' ')
        payload=payload.replace('  ',' ')
        payload=payload.replace('  ',' ')
        payload=payload.replace('  ',' ')
        print()
        print('payload : ',yellow(payload,bold=True))
        header=entry_list[0][8]
        if '$' in header:
            header=replace_variable(header)        
        header=header.replace('\n','')
        header=header.replace('\r','')
        header=header.replace('  ',' ')
        header=header.replace('  ',' ')
        header=header.replace('  ',' ')
        header=header.replace('  ',' ')
        print()
        print('header : ',yellow(header,bold=True))
        body=entry_list[0][9]
        if '$' in body:
            body=replace_variable(body)          
        body=body.replace('\n','')
        body=body.replace('\r','')
        body=body.replace('  ',' ')
        body=body.replace('  ',' ')
        body=body.replace('  ',' ')
        body=body.replace('  ',' ')
        print()
        print('body : ',yellow(body,bold=True))
        params=entry_list[0][10]
        if '$' in params:
            params=replace_variable(params)             
        params=params.replace('\n','***')
        params=params.replace('\r','')
        params=params.replace('  ',' ')
        params=params.replace('  ',' ')
        params=params.replace('  ',' ')
        params=params.replace('  ',' ')
        print()
        print('params : ',yellow(params,bold=True))
        #custom_variables=entry_list[0][11]
        #print('custom_variables : ',yellow(custom_variables,bold=True))                
        parameters=entry_list[0][11]
        if '$' in parameters:
            parameters=replace_variable(parameters)            
        parameters=parameters.replace('\n','***')
        parameters=parameters.replace('\r','')
        parameters=parameters.replace('  ',' ')
        parameters=parameters.replace('  ',' ')
        parameters=parameters.replace('  ',' ')
        parameters=parameters.replace('  ',' ')
        print()
        print('parameters : ',yellow(parameters,bold=True))
        authentication_profile=entry_list[0][12]
        if authentication_profile==None:    
            authentication_profile=''
        print('authentication_profile : ',yellow(authentication_profile,bold=True))
        input_variables=entry_list[0][13]
        print('input_variables : ',yellow(input_variables,bold=True))    
        output_variables=entry_list[0][14]
        print('output_variables : ',yellow(output_variables,bold=True))   
    found=1
    print('\nFOUND (x114) = ' ,found)
    if found==1:
        print('\nauthentication_profile : ',yellow(authentication_profile,bold=True))
        print()   
        '''
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
        '''
        # Select Authentication Profile
        api_key=""
        if authentication_profile!="saved_token":
            if authentication_profile!="":
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
            print(red("\nOK SEND CALL (203): ",bold=True)) 
            result,response_txt=send_api_call_function(method,base_url,relative_url,additionnal_get_params,header,payload,body,params,parameters,api_key) # http://127.0.0.1:4000/code_edit?code=def_send_api_call_function.py&type=function
            result=1
    return result,response_txt