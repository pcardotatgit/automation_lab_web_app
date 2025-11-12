#  def_create_connection***
def create_connection(db_file):
    '''
    MODIFIED : 2025-09-23T16:05:16.000Z
    description : create create connection to database
    
    how to call it : conn=create_connection(database)
    '''
    route="/create_connection"
    env.level+='-'
    print('\n'+env.level,white('def create_connection() in app.py : >\n',bold=True))
    loguer(env.level+' def create_connection() in app.py : >')
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    env.level=env.level[:-1]
    return conn  
