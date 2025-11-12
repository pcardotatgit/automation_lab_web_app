#  def_parse_result_of_dns_activity***
def parse_result_of_dns_activity(result,domain):
    '''
    MODIFIED : 2025-11-05T17:14:38.000Z

    description : parse the result of the Umbrella get dns activity and return the list of IP addresses of host which connect to the domain
    
    how to call it :
    '''
    route="/parse_result_of_dns_activity"
    env.level+='-'
    print('\n'+env.level,white('def parse_result_of_dns_activity() in app.py : >\n',bold=True))
    loguer(env.level+' def parse_result_of_dns_activity() in app.py : >')
    # ===================================================================    
    ip_list=[]
    json_result=json.loads(result)['data']
    for item in json_result:
        #print("\nitem : ",cyan(item['domain'],bold=True))
        #print("\ntype",cyan(type(item),bold=True))   
        if item['domain']== domain:
            #print(red(item['internalip'],bold=True))
            #print('==================')
            ip_list.append(item['internalip'])
    print("\nip_list",red(ip_list,bold=True))
    # ===================================================================
    loguer(env.level+' def END OF parse_result_of_dns_activity() in app.py : >')    
    env.level=env.level[:-1]
    return ip_list
    
