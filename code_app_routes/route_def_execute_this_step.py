#  def_execute_this_step***
@app.route('/execute_this_step', methods=['GET'])
def execute_this_step():
    '''
    Created : 2025-11-03

    description : execute the step
    '''
    route="/execute_this_step"
    env.level+='-'
    print('\n'+env.level,white('route execute_this_step() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route execute_this_step() in ***app.py*** : >')
    global client_id
    global client_password
    global host
    global host_for_token
    global profil_name
    if not session.get('logged_in'):
        return render_template('login.html')
    else:          
        global use_simulator
        with open('./json_results/json_result.json','w') as file:  
            file.write('{}')
        with open('./result/step.txt') as file:
            step=file.read()
        current_index=step.split(' ')[1]
        next_step=int(current_index)+1
        if next_step==1:
            str_next_step='Step 01'
        elif next_step==2:
            str_next_step='Step 02'    
        elif next_step==3:
            str_next_step='Step 03' 
        elif next_step==3:
            str_next_step='Step 03' 
        elif next_step==4:
            str_next_step='Step 04' 
        elif next_step==5:
            str_next_step='Step 05' 
        elif next_step==6:
            str_next_step='Step 06' 
        elif next_step==7:
            str_next_step='Step 07' 
        elif next_step==8:
            str_next_step='Step 08'     
        elif next_step==9:
            str_next_step='Step 09'             
        else:
            str_next_step='Step '+str(next_step)
        database="workflows"
        print("\ndatabase : ",database)
        table="workflows"
        print("\ntable : ",table)
        where_clause=f'where step = "{step}"'
        entry_list=sqlite_db_select_entry(database,table,where_clause)
        print("\nentry_list : \n",entry_list)
        row=entry_list[0][0]
        workflow_name=entry_list[0][1]
        #step=entry_list[0][2]
        step_name=entry_list[0][3]         
        step_input=entry_list[0][4]
        step_input_list=step_input.split(',')
        '''
        if "{" in input or "[" in input:
            input
        '''
        step_output=entry_list[0][5]
        step_output_list=step_output.split(',')
        comment=entry_list[0][6]
        # ############################################
        # search for API calls
        use_function=1
        if use_function==1:
            db_name = "api_calls.db"
            table_name = "api_calls"
            engine = sqlalchemy.create_engine("sqlite:///z_bases/%s" % db_name, execution_options={"sqlite_raw_colnames": True})
            df = pd.read_sql_table(table_name, engine)
            out_df = df[['index','name','fqdn','relative_url','documentation','method','description','payload','header','body','query_params','custom_variables','authentication_profile','inputs_variables','output_variables']]
            df = DataFrame(out_df)
            #print (' df :',cyan(df,bold=True))
            res = df.values.tolist()
            authentication_profile=''
            found=0
            for item in res:
                api_call_name=item[1]
                print (' api call name :',cyan(api_call_name,bold=True))
                if ' <=> ' in step_name:
                    step_name=step_name.split(' <=> ')[1]                
                print (' step_name :',cyan(step_name,bold=True))
                if step_name==api_call_name:    
                    found=1
                    print('\n API Call found in Database :',cyan(item,bold=True))
                    api_call_name=item[1]        
                    result,response_txt=select_api_call_and_send_it(api_call_name)
            if found==0:
                # #################################################
                # #########  THEN SEARCH IN FUNCTIONS DATABASE
                response_txt=""
                keyword=step_name
                print("\nkeyword : ",keyword)      
                database = os.getcwd()+'/z_bases/functions.db'
                database=database.replace("\\","/")
                print('database is :',database)
                db_name = "functions.db"
                table_name = "functions"
                engine = sqlalchemy.create_engine("sqlite:///z_bases/%s" % db_name, execution_options={"sqlite_raw_colnames": True})
                df = pd.read_sql_table(table_name, engine)
                out_df = df[['index','name','environment_name','description','called_function','input_variables','output_variables','comment']]
                df = DataFrame(out_df)
                #print (df)
                select_options=''
                res = df.values.tolist()
                found=0
                for item in res:
                    if keyword in item:
                        found=1
                        print('FUNCTION FOUND THEN RUN IT')
                        print(item)
                        called_function=item[4]
                        print('called function : ',called_function)                   
                        print('input variables : ',item[5])
                        print('output variables : ',item[6])
                        print('Step input variables list : ',step_input_list)
                        print('Step output variables list : ',step_output_list)  
                        step_input_variable_list=[]
                        database="variables"
                        #database = os.getcwd()+'/z_bases/'+database+'.db'
                        #database=database.replace("\\","/")                    
                        print("\ndatabase : ",database)
                        table="variables"
                        print("\ntable : ",table)                    
                        for item in step_input_list:
                            where_clause=f'where name = "{item}"'
                            entry_list=sqlite_db_select_entry(database,table,where_clause)
                            #print("\nentry_list : \n",entry_list)
                            step_input_variable_list.append(entry_list[0][3])   
                        print('Step input variables list : ',yellow(step_input_variable_list,bold=True))
                        if called_function=='parse_result_of_cse_get_computers':
                            guid=parse_result_of_cse_get_computers(step_input_variable_list[0],step_input_variable_list[1])
                            if "xxxx" not in guid:
                                response_txt=guid
                                result=variables_sqlite_update_value(step_output,guid)
                                result=1
                                with open('./result/step.txt','w') as file:
                                    file.write(str_next_step)                               
                            else:
                                result=0
                        elif called_function=='cse_id_of_event_type_name':
                            event_type_id=cse_id_of_event_type_name(step_input_variable_list[0])
                            if "xxxx" not in event_type_id:
                                response_txt=event_type_id
                                result=variables_sqlite_update_value(step_output,event_type_id)
                                result=1
                                with open('./result/step.txt','w') as file:
                                    file.write(str_next_step)                               
                            else:
                                result=0    
                        elif called_function=='cse_check_for_events_in_host':
                            idlist=step_input_variable_list[2].split(',')     
                            host_events="xxxxxx"
                            host_events=cse_check_for_events_in_host(step_input_variable_list[0],step_input_variable_list[1],idlist)
                            host_events_txt=json.dumps(host_events)
                            with open('./json_results/json_result.json','w') as file:
                                file.write(host_events_txt)                        
                            #print('\nstep_output : ',red(step_output,bold=True))
                            #print()                              
                            if "xxxx" not in host_events:
                                response_txt=host_events
                                print('\nstep_output : ',red(step_output,bold=True))
                                print()                                
                                result=variables_sqlite_update_value(step_output,host_events_txt)
                                result=1
                                with open('./result/step.txt','w') as file:
                                    file.write(str_next_step)                               
                            else:
                                result=0      
                        elif called_function=='get_sha256_from_cse_event':
                            sha256="xxxxxx"
                            sha256,filename=get_sha256_from_cse_event(step_input_variable_list[0])
                            sha256_txt='{"sha256":"'+sha256+'"}'
                            with open('./json_results/json_result.json','w') as file:
                                file.write(sha256_txt)                        
                            #print('\nstep_output : ',red(step_output,bold=True))
                            #print()                              
                            if "xxxx" not in sha256:
                                response_txt=sha256_txt
                                #print('\nstep_output : ',red(step_output,bold=True))
                                #print()                                
                                variables_sqlite_update_value('CSE_malicious_file_sha256',sha256)
                                variables_sqlite_update_value('CSE_malicious_file_name',filename)
                                result=1
                                with open('./result/step.txt','w') as file:
                                    file.write(str_next_step)                               
                            else:
                                result=0         
                        elif called_function=='parse_result_of_ma_search_submission':
                            sample_id_txt="xxxxxx"
                            sample_id=parse_result_of_ma_search_submission(step_input_variable_list[0])
                            sample_id_txt='{"sample_id":"'+str(sample_id)+'"}'
                            with open('./json_results/json_result.json','w') as file:
                                file.write(sample_id_txt)                        
                            #print('\nstep_output : ',red(step_output,bold=True))
                            #print()                              
                            if "xxxx" not in sample_id_txt:
                                response_txt=sample_id_txt
                                #print('\nstep_output : ',red(step_output,bold=True))
                                #print()                                
                                variables_sqlite_update_value('Malware_Analytics_sample_ID',str(sample_id))
                                result=1
                                with open('./result/step.txt','w') as file:
                                    file.write(str_next_step)                               
                            else:
                                result=0     
                        elif called_function=='parse_umbrella_result_for_token':
                            token_txt="xxxxxx"
                            token_txt=parse_umbrella_result_for_token(step_input_variable_list[0])
                            with open('./json_results/json_result.json','w') as file:
                                file.write(token_txt)                        
                            #print('\nstep_output : ',red(step_output,bold=True))
                            #print()                              
                            if "xxxx" not in token_txt:
                                response_txt=token_txt
                                #print('\nstep_output : ',red(step_output,bold=True))
                                #print()                                
                                variables_sqlite_update_value('umbrella_v2_api_token',token_txt)
                                result=1
                                with open('./result/step.txt','w') as file:
                                    file.write(str_next_step)                               
                            else:
                                result=0            
                        elif called_function=='parse_result_of_ma_get_domains':
                            domain="xxxxxx"
                            domain,domain_ip=parse_result_of_ma_get_domains(step_input_variable_list[0])
                            result_txt="{'domain':'"+domain+"','domain_ip':'"+domain_ip+"'}"
                            with open('./json_results/json_result.json','w') as file:
                                file.write(result_txt)                        
                            #print('\nstep_output : ',red(step_output,bold=True))
                            #print()                              
                            if "xxxx" not in domain:
                                response_txt=result_txt
                                #print('\nstep_output : ',red(step_output,bold=True))
                                #print()                                
                                variables_sqlite_update_value('malicious_domain_ip',domain_ip)
                                variables_sqlite_update_value('domain',domain)
                                result=1
                                with open('./result/step.txt','w') as file:
                                    file.write(str_next_step)                               
                            else:
                                result=0      
                        elif called_function=='parse_result_of_dns_activity':
                            ip_list=["xxxxxx"]
                            ip_list=parse_result_of_dns_activity(step_input_variable_list[0],step_input_variable_list[1])
                            result_txt=json.dumps(ip_list)
                            with open('./json_results/json_result.json','w') as file:
                                file.write(result_txt)                        
                            #print('\nstep_output : ',red(step_output,bold=True))
                            #print()                              
                            if "xxxx" not in ip_list:
                                response_txt=result_txt
                                #print('\nstep_output : ',red(step_output,bold=True))
                                #print()                                
                                #variables_sqlite_update_value('malicious_domain_ip',domain_ip)
                                #variables_sqlite_update_value('domain',domain)
                                index=1
                                for ip_addr in ip_list:
                                    variable_name='internal_infected_ip_address_'+str(index)
                                    index+=1
                                    variables_sqlite_update_value(variable_name,ip_addr)
                                result=1
                                with open('./result/step.txt','w') as file:
                                    file.write(str_next_step)                               
                            else:
                                result=0              
                        elif called_function=='parse_xdr_result_for_token':
                            token_txt="xxxxxx"
                            token_txt=parse_xdr_result_for_token(step_input_variable_list[0])
                            with open('./json_results/json_result.json','w') as file:
                                file.write(token_txt)                        
                            #print('\nstep_output : ',red(step_output,bold=True))
                            #print()                              
                            if "xxxx" not in token_txt:
                                response_txt=token_txt
                                print('\nstep_output : ',red(step_output,bold=True))
                                print()                                
                                variables_sqlite_update_value(step_output,token_txt)
                                result=1
                                with open('./result/step.txt','w') as file:
                                    file.write(str_next_step)                               
                            else:
                                result=0           
                        elif called_function=='set_observable_type_to_domain':
                            response_txt="{'status':'success'}"
                            set_observable_type_to_domain()
                            with open('./json_results/json_result.json','w') as file:
                                file.write(response_txt)                        
                            result=1
                            with open('./result/step.txt','w') as file:
                                file.write(str_next_step)           
                        elif called_function=='update_variables_from_json_inputs':
                            response_txt="{'status':'success'}"
                            update_variables_from_json_inputs(step_input_variable_list[0])
                            with open('./json_results/json_result.json','w') as file:
                                file.write(response_txt)                        
                            result=1
                            with open('./result/step.txt','w') as file:
                                file.write(str_next_step)                                   
                        else:
                            result=0
                            image="../static/images/nok.png"
                            message1="Operation Failed"
                            message2="No Function to call was found"
                            message3="/"
                            message4="Home"
                            PAGE_DESTINATION="operation_done"
                            page_name="operation_done.html"
                            env.level=env.level[:-1]
                            return render_template('main_index.html',route=route,USERNAME=session['user'],PAGE_DESTINATION=PAGE_DESTINATION,message1=message1,message2=message2,message3=message3,message4=message4,image=image,page_name=page_name)
                                 
                if result==1:
                    image="../static/images/ok.png"
                    message1=response_txt
                    message2="Okay !"
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
                    env.level=env.level[:-1]
                    return render_template('main_index.html',route=route,USERNAME=session['user'],PAGE_DESTINATION=PAGE_DESTINATION,message1=message1,message2=message2,message3=message3,message4=message4,image=image,page_name=page_name)
            
                # #################################################"
                if found==0:
                    image="../static/images/nok.png"
                    message1="Operation Failed"
                    message2="API call or Function not found"
                    message3="/"
                    message4="Home"
                    PAGE_DESTINATION="operation_done"
                    page_name="operation_done.html"
                    env.level=env.level[:-1]
                    return render_template('main_index.html',route=route,USERNAME=session['user'],PAGE_DESTINATION=PAGE_DESTINATION,message1=message1,message2=message2,message3=message3,message4=message4,image=image,page_name=page_name)
            else:
                with open('./json_results/json_result.json') as file:
                    call_result=file.read()
                variables_sqlite_update_value(step_output,call_result)    
                lines=call_result.split('\n')
                #print('  lines : \n',lines)
                print('\ncall_result : \n',green(call_result,bold=True)) 
                ii=0
                for line in lines:
                    response_txt=response_txt+line+'\n'
                    ii+=1
                    if ii>200:
                        response_txt=response_txt+'..... Rest of response is not shown... it was too long \n\n=> You can click on the [ Display in Tree Graph ] button  to see the entire content'
                        break
                # #########################################################
                if result==1:
                    with open('./result/step.txt','w') as file:
                        file.write(str_next_step)                   
                    image="../static/images/ok.png"
                    message1=response_txt
                    message2="Okay !"
                    message3="#"
                    message4=""
                    PAGE_DESTINATION="z_api_call_result"
                    page_name="z_api_call_result.html"
                    env.level=env.level[:-1]
                    return render_template('main_index.html',route=route,USERNAME=session['user'],PAGE_DESTINATION=PAGE_DESTINATION,message1=message1,message2=message2,message3=message3,message4=message4,image=image,page_name=page_name)           
        else:
            # DELETE THIS BRANCH IF IT WORKS
            db_name = "api_calls.db"
            table_name = "api_calls"
            engine = sqlalchemy.create_engine("sqlite:///z_bases/%s" % db_name, execution_options={"sqlite_raw_colnames": True})
            df = pd.read_sql_table(table_name, engine)
            out_df = df[['index','name','fqdn','relative_url','documentation','method','description','payload','header','body','query_params','custom_variables','authentication_profile','inputs_variables','output_variables']]
            df = DataFrame(out_df)
            #print (' df :',cyan(df,bold=True))
            res = df.values.tolist()
            authentication_profile=''
            found=0
            for item in res:
                api_call_name=item[1]
                print (' api call name :',cyan(api_call_name,bold=True))
                if ' <=> ' in step_name:
                    step_name=step_name.split(' <=> ')[1]                
                print (' step_name :',cyan(step_name,bold=True))
                if step_name==api_call_name:    
                    found=1
                    print('\n API Call found in Database :',cyan(item,bold=True))
                    name=item[1]
                    print('\nname : ',yellow(name,bold=True))
                    print()     
                    base_url=item[2]
                    print('\nbase_url : ',yellow(base_url,bold=True))
                    print()
                    relative_url=item[3]
                    print('relative_url : ',yellow(relative_url,bold=True))
                    api_documentation=item[4]
                    print()
                    print('api_documentation : ',yellow(api_documentation,bold=True))
                    method=item[5]
                    print()
                    print('method : ',yellow(method,bold=True))
                    short_description=item[6]
                    print()
                    print('short_description : ',yellow(short_description,bold=True))
                    payload=item[7]
                    payload=payload.replace('\n','')
                    payload=payload.replace('\r','')
                    payload=payload.replace('  ',' ')
                    payload=payload.replace('  ',' ')
                    payload=payload.replace('  ',' ')
                    payload=payload.replace('  ',' ')
                    print()
                    print('payload : ',yellow(payload,bold=True))
                    header=item[7]
                    header=header.replace('\n','')
                    header=header.replace('\r','')
                    header=header.replace('  ',' ')
                    header=header.replace('  ',' ')
                    header=header.replace('  ',' ')
                    header=header.replace('  ',' ')
                    print()
                    print('header : ',yellow(header,bold=True))
                    body=item[8]
                    body=body.replace('\n','')
                    body=body.replace('\r','')
                    body=body.replace('  ',' ')
                    body=body.replace('  ',' ')
                    body=body.replace('  ',' ')
                    body=body.replace('  ',' ')
                    print()
                    print('body : ',yellow(body,bold=True))
                    params=item[9]
                    params=params.replace('\n','***')
                    params=params.replace('\r','')
                    params=params.replace('  ',' ')
                    params=params.replace('  ',' ')
                    params=params.replace('  ',' ')
                    params=params.replace('  ',' ')
                    print()
                    print('params : ',yellow(params,bold=True))
                    custom_variables=item[10]
                    print('custom_variables : ',yellow(custom_variables,bold=True))                
                    parameters=item[11]
                    parameters=parameters.replace('\n','***')
                    parameters=parameters.replace('\r','')
                    parameters=parameters.replace('  ',' ')
                    parameters=parameters.replace('  ',' ')
                    parameters=parameters.replace('  ',' ')
                    parameters=parameters.replace('  ',' ')
                    print()
                    print('parameters : ',yellow(parameters,bold=True))
                    authentication_profile=item[12]
                    if authentication_profile==None:    
                        authentication_profile=''
                    print('authentication_profile : ',yellow(authentication_profile,bold=True))
                    input_variables=item[13]
                    print('input_variables : ',yellow(input_variables,bold=True))    
                    output_variables=item[10]
                    print('output_variables : ',yellow(output_variables,bold=True))   
            print('FOUND = ' ,found)
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
                    print("\nOK SEND CALL : ") 
                    result,response_txt=send_api_call_function(method,base_url,relative_url,additionnal_get_params,header,payload,body,parameters,api_key) # http://127.0.0.1:4000/code_edit?code=def_send_api_call_function.py&type=function

                # read the first 200 lines of the JSON result
                with open('./result/step.txt','w') as file:
                    file.write(str_next_step)   
                
                with open('./json_results/json_result.json') as file:
                    call_result=file.read()
                lines=call_result.split('\n')
                #print('  lines : \n',lines)
                print('\ncall_result : \n',cyan(call_result,bold=True))
                # update SQLite DB variables
                result=variables_sqlite_update_value(step_output,call_result)
                
                # ##################################
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
                    env.level=env.level[:-1]
                    return render_template('main_index.html',route=route,USERNAME=session['user'],PAGE_DESTINATION=PAGE_DESTINATION,message1=message1,message2=message2,message3=message3,message4=message4,image=image,page_name=page_name)

                                                                   