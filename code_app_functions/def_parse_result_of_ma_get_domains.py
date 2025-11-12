#  def_parse_result_of_ma_get_domains***
def parse_result_of_ma_get_domains(result):
    '''
    MODIFIED : 2025-11-05T16:40:37.000Z

    description : parse the result of Malware Analytics API call and return domain name and domain IP address
    
    how to call it :
    '''
    route="/parse_result_of_ma_get_domains"
    env.level+='-'
    print('\n'+env.level,white('def parse_result_of_ma_get_domains() in app.py : >\n',bold=True))
    loguer(env.level+' def parse_result_of_ma_get_domains() in app.py : >')
    # ===================================================================    
    json_result=json.loads(result)
    for item in json_result.items():
        if 'data' in item[0]:
            #print("\nitem : ",cyan(item,bold=True))
            #print("\ntype",cyan(type(item),bold=True))   
            domain=item[1]["items"][0]["domain"]
            domain_ip=item[1]["items"][0]["data"]["answers"][0]
            print("\ndomain :",red(domain,bold=True))
            print("\ndomain_ip :",red(domain_ip,bold=True))            
    # ===================================================================
    loguer(env.level+' def END OF parse_result_of_ma_get_domains() in app.py : >')    
    env.level=env.level[:-1]
    return domain,domain_ip
    
