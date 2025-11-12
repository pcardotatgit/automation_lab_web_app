#  def_convert_hex_to_string***
def convert_hex_to_string(hex_str):
    '''
    MODIFIED : 2025-10-14T14:45:14.000Z
    description : convert hex to an ip address
    
    how to call it :
    '''
    route="/convert_hex_to_string"
    env.level+='-'
    print('\n'+env.level,white('def convert_hex_to_string() in app.py  : >\n',bold=True))
    loguer(env.level+' def convert_hex_to_string() in app.py  : > ')
    # ===================================================================    
    res = ''.join([chr(int(hex_str[i:i+2], 16)) for i in range(0, len(hex_str), 2)])
    print('ip : ',res)
    #print(type(res))
    # ===================================================================
    loguer(env.level+' def END OF convert_hex_to_string() in app.py  : > ')
    env.level=env.level[:-1]
    return res
    

