#  def_date_time_for_file_name***
def date_time_for_file_name():
    '''
    MODIFIED : 2025-07-18T14:41:19.000Z

    description : generate date and time suffixe to be added to file names when we save file : format YYYYmmddHMS 
    '''
    route="/date_time_for_file_name"
    env.level+='-'
    print()
    print(env.level,white('def date_time_for_file_name() in app.py : >',bold=True))
    loguer(env.level+' def date_time_for_file_name() in app.py : >')
    print()
    # ===================================================================    
    current_time = datetime.utcnow()
    timestampStr = current_time.strftime("%Y%m%d_%H%M%S")  
    # ===================================================================
    env.level=env.level[:-1]
    return(timestampStr)
    