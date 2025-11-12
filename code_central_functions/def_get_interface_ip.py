#  def_get_interface_ip***
def get_interface_ip(interface):
    '''
    MODIFIED : 2025-08-03T16:30:42.000Z

    description : Get IP address for a given network interface
    
    how to call it :
    '''
    env.level+='-'
    print('\n'+env.level,white('def get_interface_ip() in app.py : >\n',bold=True))
    loguer(env.level+' def get_interface_ip() in app.py : >')
    if not interface or not isinstance(interface, str):
        return None
    if not re.match(r'^[a-zA-Z0-9]+$', interface):
        return None  # Only allow alphanumeric interface names
    try:
        command = ["ip", "addr", "show", interface]
        output = subprocess.check_output(command, timeout=10).decode()

        ip_pattern = r'inet\s+(\d+\.\d+\.\d+\.\d+)'
        match = re.search(ip_pattern, output)
        
        if match:
            ip_address = match.group(1)
            loguer(env.level+'OK DONE SUCCESS - def get_interface_ip() in app.py : >')
            env.level=env.level[:-1]        
            return ip_address
        else:
            loguer(env.level+'OK DONE ERROR - def get_interface_ip() in app.py : >')      
            env.level=env.level[:-1]        
            return None
    except subprocess.TimeoutExpired:
        loguer(env.level+'TIMEOUT - get_interface_ip()')
        return None
    except subprocess.CalledProcessError:
        loguer(env.level+'COMMAND_ERROR - get_interface_ip()')
        return None
    except Exception as e:
        loguer(env.level+f'UNEXPECTED_ERROR - get_interface_ip(): {e}')
        return None
      