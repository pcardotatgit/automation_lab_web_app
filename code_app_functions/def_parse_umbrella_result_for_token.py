#  def_parse_umbrella_result_for_token***
def parse_umbrella_result_for_token(result):
    '''
    MODIFIED : 2025-11-05T14:33:53.000Z

    description : parse the result of the Umbrella API V2 Token request and return the token
    
    how to call it :
    '''
    route="/parse_umbrella_result_for_token"
    env.level+='-'
    print('\n'+env.level,white('def parse_umbrella_result_for_token() in app.py : >\n',bold=True))
    loguer(env.level+' def parse_umbrella_result_for_token() in app.py : >')
    # ===================================================================    
    if 'access_token' in result:
        json_data=json.loads(result)
        token=json_data['access_token']
    else:
        token='ERROR ! no token in result'
    # ===================================================================
    loguer(env.level+' def END OF parse_umbrella_result_for_token() in app.py : >')    
    env.level=env.level[:-1]
    return token
    
