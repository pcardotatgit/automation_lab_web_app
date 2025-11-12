#  def_replace_variables***
def replace_variables(chaine,config_dict):
    '''
    MODIFIED : 2025-07-18T14:43:59.000Z

    description : replace a variable string which start whith $ by the corresponding config variable which has the same name
    '''
    route="/replace_variables(chaine,config_dict)"
    env.level+='-'
    print()
    print(env.level,white('def replace_variables() in app.py  : >\n',bold=True))
    loguer(env.level+' def replace_variables() in app.py  : > ')
    print()
    global api_key
    global orgID
    global host
    global network_id
    global profil_name
    # ===================================================================    

    for k,v in config_dict.items():
          if v:
              chaine=chaine.replace('$'+k,v)
    print()
    print('chaine :',yellow(chaine,bold=True))
    print()   
    # ===================================================================
    env.level=env.level[:-1]
    return chaine
    

