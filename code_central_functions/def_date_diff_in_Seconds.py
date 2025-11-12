#  def_date_diff_in_Seconds***
def date_diff_in_Seconds(dt2, dt1):
    '''
    MODIFIED : 2025-08-03T16:52:34.000Z

    description : Get time difference in seconds between 2 times
    
    how to call it :
    '''
    route="/date_diff_in_Seconds"
    env.level+='-'
    print('\n'+env.level,white('def date_diff_in_Seconds() in app.py : >\n',bold=True))
    loguer(env.level+' def date_diff_in_Seconds() in app.py : >')
    # ===================================================================    
    # Calculate the time difference between dt2 and dt1
    timedelta = dt2 - dt1
    # ===================================================================
    loguer(env.level+' def END OF date_diff_in_Seconds() in app.py : >')    
    env.level=env.level[:-1]
    # Return the total time difference in seconds
    return timedelta.days * 24 * 3600 + timedelta.seconds
    
