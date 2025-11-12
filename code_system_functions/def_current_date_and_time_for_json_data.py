# def_current_date_and_time_for_json_data***
def current_date_and_time_for_json_data():  
    env.level+='-'
    print()
    print(env.level,white('def current_date_and_time_for_json_data() : >',bold=True))
    loguer(env.level+' def current_date_and_time_for_json_data() : >')
    print() 
    '''
        current time + nb days in the YYYYmmddHMSformat
    '''
    current_time = datetime.utcnow()
    timestampStr = current_time.strftime("%Y-%m-%dT%H:%M:%S.000Z")  
    env.level=env.level[:-1]    
    return(timestampStr)
    

