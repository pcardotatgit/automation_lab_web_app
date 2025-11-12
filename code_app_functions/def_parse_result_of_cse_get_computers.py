#  def_parse_result_of_cse_get_computers***
def parse_result_of_cse_get_computers(api_call_result,hostname):
    '''
    MODIFIED : 2025-11-01T13:14:17.000Z

    description : Parse the result of the CSE Get Computers API call and output the GUID of the selected hostname
    
    how to call it :
    '''
    route="/parse_result_of_cse_get_computers"
    env.level+='-'
    print('\n'+env.level,white('def parse_result_of_cse_get_computers() in app.py : >\n',bold=True))
    loguer(env.level+' def parse_result_of_cse_get_computers() in app.py : >')
    # ===================================================================    
    print('\n api_call_result  : \n',cyan(api_call_result,bold=True))
    print('\nhostname  : ',cyan(hostname,bold=True))
    json_input_data=json.loads(api_call_result)
    computer_list_items = json_input_data["data"]
    print('\n computer_list_items  : ',cyan(computer_list_items,bold=True))    
    print(type(computer_list_items))
    print(len(computer_list_items))
    guid="xxxxxxxx"
    for item in computer_list_items:
        if item["hostname"]==hostname:
            print('\n',yellow(item["hostname"],bold=True))
            print(yellow(item["connector_guid"],bold=True))
            guid=item["connector_guid"]
    # ===================================================================  
    env.level=env.level[:-1]
    return guid
