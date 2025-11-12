#  def_update_variables_from_json_inputs***
def update_variables_from_json_inputs(inputs):
    '''
    MODIFIED : 2025-11-06T15:19:39.000Z

    description : Update Variable from a JSON Input definition
    
    how to call it :
    '''
    route="/update_variables_from_json_inputs"
    env.level+='-'
    print('\n'+env.level,white('def update_variables_from_json_inputs() in app.py : >\n',bold=True))
    loguer(env.level+' def update_variables_from_json_inputs() in app.py : >')
    # ===================================================================    
    json_dict=json.loads(inputs)
    print('json_dict : ',cyan(json_dict,bold=True))
    for item,v in json_dict.items():
        print(item)
        if '$' in v:    
            word=v.replace('$','')
            print(f'\n OK We replace this name : {word} by its value in Database\n')            
            v=replace_this_variable_by_its_value(word)
        print(v)        
        print("========================")
        variables_sqlite_update_value(item,v)
    # ===================================================================
    env.level=env.level[:-1]
    return 1
    
