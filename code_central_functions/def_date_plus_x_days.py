#  def_date_plus_x_days***
def date_plus_x_days(nb):
    '''
    MODIFIED : 2025-06-27T16:22:59.000Z

    description : Calculate date from today + x Days
    '''
    route="/date_plus_x_days"
    env.level+='-'
    print()
    print(env.level,white('def date_plus_x_days() in app.py : >',bold=True))     
    current_time = datetime.utcnow()
    start_time = current_time + timedelta(days=nb)
    timestampStr = start_time.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    env.level=env.level[:-1]
    return(timestampStr) 
    