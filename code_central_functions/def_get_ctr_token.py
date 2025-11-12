#  def_get_ctr_token***
def get_ctr_token(host_for_token,ctr_client_id,ctr_client_password):
    '''
    MODIFIED : 2025-06-04T13:11:36.000Z

    description : asking for an API Token to XDR
    '''
    route="/get_ctr_token"
    env.level+='-'
    print()
    print(env.level,white('def get_ctr_token() in app.py : >',bold=True))
    loguer(env.level+' def get_ctr_token() in app.py : >')
    print()
    print(yellow('Asking for new CTR token',bold=True))
    url = f'{host_for_token}/iroh/oauth2/token'
    #url = 'https://visibility.eu.amp.cisco.com/iroh/oauth2/token'
    print()
    print(url)
    print()    
    headers = {'Content-Type':'application/x-www-form-urlencoded', 'Accept':'application/json'}
    payload = {'grant_type':'client_credentials'}
    print()
    print('ctr_client_id : ',green(ctr_client_id,bold=True))
    print('ctr_client_password : ',green(ctr_client_password,bold=True))
    response = requests.post(url, headers=headers, auth=(ctr_client_id, ctr_client_password), data=payload)
    #print(response.json())
    reponse_list=response.text.split('","')
    token=reponse_list[0].split('":"')
    print(green(token[1],bold=True))
    fa = open("ctr_token.txt", "w")
    fa.write(token[1])
    fa.close()
    return (token[1])  
