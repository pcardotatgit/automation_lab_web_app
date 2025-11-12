#  def_example_name***
def example_name(args):
    '''
    ***description***
    
    how to call it :
    '''
    route="/example_name"
    env.level+='-'
    print('\n'+env.level,white('def example_name() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' def example_name() in ***app.py*** : >')
    global client_id
    global client_password
    global host
    global host_for_token
    global profil_name
    # ===================================================================    
    '''
    put your custom code here
    '''
    # ===================================================================
    loguer(env.level+' def END OF example_name() in ***app.py*** : >')    
    env.level=env.level[:-1]
    return result
    
