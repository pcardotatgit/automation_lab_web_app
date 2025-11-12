#  def_check_ip_addresses***
def check_ip_addresses(interface_name: str) -> tuple[str, str]:
    '''
    MODIFIED : 2025-08-04

    description : get public IP address from jsonip.com
    
    how to call it : ip_address,ip=check_ip_addresses(interface)  interface = interface name ex: wlan0
    '''
    env.level+='-'
    print('\n'+env.level,white('def check_ip_addresses() in app.py : >\n',bold=True))
    loguer(env.level+' def check_ip_addresses() in app.py : >')
    # ===================================================================    
    loguer(env.level+'- var DEBUG : ???')
    loguer(env.level+'-- var Get Inferface IP  ???')        
    ip_address = get_interface_ip(interface_name)
    loguer(env.level+'-- var Get Inferface IP = OK ???')     
    if ip_address:
        print(f"IP address of {interface_name}: {ip_address}")
        loguer(env.level+'- var DEBUG : ???')
        loguer(env.level+'-- var query jsonip.com  ???')            
        r = requests.get(r'http://jsonip.com')
        loguer(env.level+'-- var query jsonip.com  = OK???')              
        public_ip= r.json()['ip']   
    else:
        loguer(env.level+'- var DEBUG : ???')
        loguer(env.level+'-- var No IP address found for inteface  ???')       
        print(f"No IP address found for {interface_name}")       
        public_ip='0.0.0.0'
        ip_address='0.0.0.0'
        
    try:
        # Get local IP
        ip_address = get_interface_ip(interface_name)
        
        if ip_address:
            print(f"\nIP address of {interface_name}: {ip_address}")
            
            # Get public IP with timeout
            try:
                loguer(env.level+'- var DEBUG : ???')
                loguer(env.level+'-- var query jsonip.com  ???')                  
                response = requests.get('https://jsonip.com', timeout=10)
                response.raise_for_status()
                public_ip = response.json()['ip']
                loguer(env.level+'-- var query jsonip.com  = SUCCESS ???')                   
            except (requests.RequestException, KeyError, ValueError) as e:
                print(f"Error getting public IP: {e}")
                public_ip = '0.0.0.0'
        else:
            print(f"\nNo IP address found for {interface_name}")
            loguer(env.level+'- var DEBUG : ???')
            loguer(env.level+'-- var query NO IP ADDRESS FOUND  ???')            
            public_ip = '0.0.0.0'
            ip_address = '0.0.0.0'
        env.level=env.level[:-1]  
        loguer(env.level+' def END w SUCCESS OF check_ip_addresses() in app.py : >')
        return ip_address, public_ip
        
    except Exception as e:
        loguer(env.level+'- var DEBUG : ???')
        loguer(env.level+'-- var Unexpected error  ???')    
        loguer(env.level+' def END w ERROR OF check_ip_addresses() in app.py : >')
        print(f"Unexpected error: {e}")
        env.level=env.level[:-1]        
        return '0.0.0.0', '0.0.0.0'          
