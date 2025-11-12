# def_current_date_and_time***
def current_date_and_time():  
    env.level+='-'
    print()
    print(env.level,white('def current_date_and_time() : >',bold=True))
    loguer(env.level+' def current_date_and_time() : >')
    print() 
    '''
        current time + nb days in the YYYYmmddHMSformat
    '''
    current_time = datetime.utcnow()
    timestampStr = current_time.strftime("%Y%m%d%H%M%S")
    env.level=env.level[:-1]
    return(timestampStr)


