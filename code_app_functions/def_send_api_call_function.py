#  def_send_api_call_function***
def send_api_call_function(method,base_url,relative_url,additionnal_get_params,headers,payload,body,params,parameters,api_key):
    '''
    MODIFIED : 2025-11-06
    description : send_the_api call to the destination REST service
    
    how to call it : result,json_txt_result=send_api_call_function(method,base_url,relative_url,additionnal_get_params,headers,payload,body,parameters,api_key)
    '''
    route="/send_api_call_function"
    env.level+='-'
    print()
    print(env.level,white('def send_api_call_function() in app.py  : >\n',bold=True))
    loguer(env.level+' def send_api_call_function() in app.py  : > ')
    print()
    #global api_key
    global orgID
    global host
    global client_id
    global client_password
    global custom1
    global custom2
    global profil_name
    # ===================================================================    
    print('base_url :',cyan(base_url,bold=True))
    print()        
    print('relative_url :',cyan(relative_url,bold=True))
    print()  
    print('method :',cyan(method,bold=True))
    print()       
    print('payload :',cyan(payload,bold=True))
    print()    
    print('headers :',cyan(headers,bold=True))
    print()      
    print('body :',cyan(body,bold=True))
    print()
    print('params :',cyan(params,bold=True))    
    print()
    print('parameters :',cyan(parameters,bold=True))
    print('\napi_key :',cyan(api_key,bold=True))          
    config_dict={}
    if api_key !='' and api_key !='no_key':    
        config_dict['api_key']=api_key  
    config_dict['host']=host 
    '''
    if client_id !='':    
        config_dict['client_id']=client_id 
    if client_password !='':    
        config_dict['client_password']=client_password        
    '''        
    if parameters !='':
        parameter_list=parameters.split("***")    
        for param in parameter_list:
            params=param.split('=')
            config_dict[params[0]]=params[1]
    print('config_dict :\n',yellow(config_dict,bold=True))
    print()      
    saved_token='xxx'
    if '$SAVED_TOKEN' in relative_url:
        relative_url=relative_url.replace('$SAVED_TOKEN',saved_token)      
    if '$SAVED_TOKEN' in payload:
        payload=payload.replace('$SAVED_TOKEN',saved_token)      
    if '$SAVED_TOKEN' in headers:
        headers=headers.replace('$SAVED_TOKEN',saved_token)        
    if '$SAVED_TOKEN' in body:
        body=body.replace('$SAVED_TOKEN',saved_token) 
        
    if '$' in relative_url:
        relative_url=replace_variable(relative_url)
    print('relative_url :',yellow(relative_url,bold=True))
    print()
    if payload!='':
        if '$' in payload:
           payload=replace_variable(payload)  
    else:
        payload={}
    payload=json.loads(payload)         
    if headers!='':
        if '$' in headers:
            headers=replace_variable(headers) 
    else:
        headers=''    
    if body !='':
        if '$' in body:
            body=replace_variable(body)         
    else:
        body={}                  
    api_url = f"{base_url}{relative_url}{additionnal_get_params}"          
    print(magenta('--> API CALL details here under :',bold=True))
    print('api_url : ',yellow(api_url,bold=True))
    print()     
    print('method : ',yellow(method,bold=True))
    print()     
    print('payload :',yellow(payload,bold=True))
    print() 
    print('headers :',yellow(headers,bold=True))
    print()    
    print('body :',yellow(body,bold=True))
    print()     
    print('parameters :',yellow(parameters,bold=True))
    print()
    #if headers!={}:
    headers=json.loads(headers)  
    if body=="{}":
        body=json.loads(body)  
    response = requests.request(method, api_url, headers=headers, data = payload, params=params)
    print('response :',yellow(response,bold=True))
    print('response content :',yellow(response.content,bold=True))
    print()  
    if 'Route NOT FOUND' not in response.content.decode('UTF-8'):
        if response.status_code==401:
            print()
            print(red('INVALID API CREDENTIALS >',bold=True))
            print()      
            # renew the token
            #access_token=get_ctr_token(host_for_token,client_id,client_password)
            #response = requests.request(method, api_url, headers=headers, data = payload)
            result=0
            json_txt_result=''
        elif response.status_code==403:
            print()
            print(red('ACCESS FORBIDEN >',bold=True))
            print()      
            # renew the token
            result=0
            json_txt_result=response.content       
        else:
            result=1
            if '</title>' not in response.text:
                json_txt_result = json.dumps(response.json(),indent=4,sort_keys=True, separators=(',', ': '))
                print()
                print('json_txt_result  : \n',green(json_txt_result,bold=True))       
                with open('./json_results/json_result.json','w') as file:
                    file.write(json_txt_result)
                '''
                items=response.json()
                for item in items: 
                    index+=1
                    if type(item) is dict:
                        print()
                        print(item)
                        print()
                        print(cyan(item["target_ref"],bold=True))      
                '''
            else:
                json_txt_result=response.text
                print('RESULT : ',red(response_txt,bold=True))
    else:
        result=0
        json_txt_result='ERROR  !!!! '
    # ===================================================================
    env.level=env.level[:-1]
    return result,json_txt_result
    

