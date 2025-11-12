#  def_select_profile_function***
def select_profile_function(authentication_profile):
    '''
    MODIFIED : 2025-10-26T17:23:59.000Z

    description : retrieve API credentials from profile
    
    how to call it :
    '''
    route="/select_profile_function"
    env.level+='-'
    print('\n'+env.level,white('def select_profile_function() in app.py : >\n',bold=True))
    loguer(env.level+' def select_profile_function() in app.py : >')
    global client_id
    global client_password
    global host
    global host_for_token
    global profil_name
    # ===================================================================    
    database="account_keys"
    print("\ndatabase : ",database)
    table="account_keys"
    print("\ntable : ",table)
    where_clause=f'where `name` = "{authentication_profile}"'
    entry_list=sqlite_db_select_entry(database,table,where_clause)
    print("\nentry_list : \n",entry_list)    
    type=entry_list[0][2]
    if type=='basic':
        client_id=entry_list[0][3]
        client_password=entry_list[0][4]
        api_key="no_key"
    elif type=='api_key':
        client_id=""
        client_password=""   
        api_key=entry_list[0][4]   
    elif type=='token':
        client_id=""
        client_password=""   
        api_key=entry_list[0][4]           
    else:
        client_id=""
        client_password=""   
        api_key=entry_list[0][4]                
    # ===================================================================
    env.level=env.level[:-1]
    return client_id,client_password,api_key
    
