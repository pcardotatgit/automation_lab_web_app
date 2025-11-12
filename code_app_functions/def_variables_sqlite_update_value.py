#  def_variables_sqlite_update_value***
def variables_sqlite_update_value(name,value):
    '''
    MODIFIED : 2025-11-05

    description : Update the value of the selected variable name in variables DB
    
    how to call it : result = variables_sqlite_update_value(name,value)
        name : name to search an update in the rows
        value : new value
    '''
    route="/variables_sqlite_update_value"
    env.level+='-'
    print('\n'+env.level,white('def variables_sqlite_update_value() in app.py : >\n',bold=True))
    loguer(env.level+' def variables_sqlite_update_value() in app.py : >')
    global client_id
    global client_password
    global host
    global host_for_token
    global profil_name
    # ===================================================================    
    database="variables.db"
    #database = './z_bases/'+database+'.db'
    result=0
    value=value.replace("'"," ")
    print('database is :',database) 
    print(cyan(f'\n new value : {value} for variable : {name} \n',bold=True))
    #print('\n value = ',red(value,bold=True))   
    with sqlite3.connect('./z_bases/'+database) as conn:
        cursor=conn.cursor()
        sql_request = f"UPDATE 'variables' SET value = '{value}' where name = '{name}'"      
        print('sql_request :',cyan(sql_request,bold=True))
        cursor.execute(sql_request)
        result=1
    # ===================================================================
    loguer(env.level+' def END OF variables_sqlite_update_value() in app.py : >')    
    env.level=env.level[:-1]
    return result
    
