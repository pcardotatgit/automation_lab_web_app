#  def_set_observable_type_to_domain***
def set_observable_type_to_domain():
    '''
    MODIFIED : 2025-11-06T14:57:08.000Z

    description : set_observable_type_variable_to_domain
    
    how to call it :
    '''
    route="/set_observable_type_to_domain"
    env.level+='-'
    print('\n'+env.level,white('def set_observable_type_to_domain() in app.py : >\n',bold=True))
    loguer(env.level+' def set_observable_type_to_domain() in app.py : >')
    # ===================================================================    
    variables_sqlite_update_value('observable_type','domain')
    # ===================================================================
    env.level=env.level[:-1]
    return 1
    
