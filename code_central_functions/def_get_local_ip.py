#  def_get_local_ip***
def get_local_ip(interface: str) -> str:
    '''
    MODIFIED : 2025-08-05T06:55:31.000Z

    description : get local ip address  thru socket
    
    how to call it :
    '''
    env.level+='-'
    print('\n'+env.level,white('def get_local_ip() in app.py : >\n',bold=True))
    loguer(env.level+' def get_local_ip() in app.py : >')
    try:
        # Use socket to get local IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        loguer(env.level+' def END WITH SUCCESS OF get_local_ip() in app.py : >')    
        env.level=env.level[:-1]        
        return local_ip
    except Exception:
        loguer(env.level+' def END WITH ERROR OF get_local_ip() in app.py : >')    
        env.level=env.level[:-1]      
        return '0.0.0.0'
