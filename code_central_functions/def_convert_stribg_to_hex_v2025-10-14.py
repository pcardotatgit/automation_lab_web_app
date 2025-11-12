#  def_convert_stribg_to_hex***
def convert_stribg_to_hex(ip_address):
    '''
    MODIFIED : 2025-10-14T14:39:08.000Z
    description : convert ip address to hex
    
    how to call it :
    '''
    route="/convert_stribg_to_hex"
    env.level+='-'
    print('\n'+env.level,white('def convert_stribg_to_hex() in app.py  : >\n',bold=True))
    loguer(env.level+' def convert_stribg_to_hex() in app.py  : > ')
    # ===================================================================    
    #resultat=codecs.encode(b"ip_address", "hex")
    res = ip_address.encode("utf-8")
    resultat=codecs.encode(res, "hex")
    print('ip : ',resultat)
    ip_string=resultat.decode("utf-8")
    print('ip string : ',ip_string)
    # ===================================================================
    loguer(env.level+' def END OF convert_stribg_to_hex() in app.py  : > ')
    env.level=env.level[:-1]
    return ip_string
    

