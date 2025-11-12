#  def_get_sha256_from_cse_event***
def get_sha256_from_cse_event(events_in_host):
    '''
    MODIFIED : 2025-11-05T10:43:08.000Z

    description : Extract malicious sha256 value from last events list in computer
    
    how to call it :
    '''
    route="/get_sha256_from_cse_event"
    env.level+='-'
    print('\n'+env.level,white('def get_sha256_from_cse_event() in app.py : >\n',bold=True))
    loguer(env.level+' def get_sha256_from_cse_event() in app.py : >')
    # ===================================================================    
    event_dict=json.loads(events_in_host)
    filename=''
    sha256=''
    for event in event_dict.items():
        #print("\nevent : ",red(event,bold=True))
        filename=event[1]["file"]["file_name"]
        sha256=event[1]["file"]["identity"]["sha256"]
    print("\nfilename : ",cyan(filename,bold=True)) 
    print("\nsha256 : ",cyan(sha256,bold=True))
    # ===================================================================
    loguer(env.level+' def END OF get_sha256_from_cse_event() in app.py : >')    
    env.level=env.level[:-1]
    return sha256,filename
    
