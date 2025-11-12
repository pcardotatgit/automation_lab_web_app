#  def_send_api_call_for_oauth_token***
def send_api_call_for_oauth_token(base_url,relative_url,client_id,client_password,headers,body_payload):
    '''
    MODIFIED : 2025-11-05T18:45:25.000Z

    description : Send API call for asking for a token based on Oauth2
    
    how to call it : result,response_txt=send_api_call_for_oauth_token(base_url,relative_url,client_id,client_password,headers,body_payload)
    '''
    route="/end_api_call_for_oauth_token"
    env.level+='-'
    print('\n'+env.level,white('def end_api_call_for_oauth_token() in app.py : >\n',bold=True))
    loguer(env.level+' def end_api_call_for_oauth_token() in app.py : >')
    # ===================================================================    
    print('\nbase_url :',cyan(base_url,bold=True))   
    print('\nrelative_url :',cyan(relative_url,bold=True))
    print('\nmethod :',cyan('POST',bold=True))     
    print('\nbody_payload :',cyan(body_payload,bold=True)) 
    print('\nheaders :',cyan(headers,bold=True))      
    if headers!='':
        if '$' in headers:
            headers=replace_variables(headers,config_dict) 
    else:
        headers=''    
    api_url = f"{base_url}{relative_url}"          
    print(magenta('\n--> API CALL :',bold=True))
    print('\napi_url : ',yellow(api_url,bold=True))    
    response = requests.post(api_url, headers=headers, auth=(client_id, client_password), data=body_payload)
    print('response code:',yellow(response,bold=True))
    print('response :',yellow(response.content,bold=True))
    print()     
    if response.status_code==401:
        print()
        print(red('INVALID API KEY >',bold=True))
        print()      
        # renew the token
        # access_token=get_ctr_token(host_for_token,client_id,client_password)
        # response = requests.request(method, api_url, headers=headers, data = payload)
        result=0
        json_txt_result=''
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
    # ===================================================================
    env.level=env.level[:-1]
    return result,json_txt_result
    