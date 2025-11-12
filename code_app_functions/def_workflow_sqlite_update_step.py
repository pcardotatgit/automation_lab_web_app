#  def_workflow_sqlite_update_step***
def workflow_sqlite_update_step(index,new_step):
    '''
    MODIFIED : 2025-11-01T16:03:53.000Z

    description : update step field of row in workflow database
    
    how to call it :
    '''
    route="/workflow_sqlite_update_step"
    env.level+='-'
    print('\n'+env.level,white('def workflow_sqlite_update_step() in app.py : >\n',bold=True))
    loguer(env.level+' def workflow_sqlite_update_step() in app.py : >')
    global client_id
    global client_password
    global host
    global host_for_token
    global profil_name
    # ===================================================================    
    database="workflows.db"
    #database = './z_bases/'+database+'.db'
    result=0
    print('database is :',database) 
    #print('\n value = ',red(value,bold=True))   
    with sqlite3.connect('./z_bases/'+database) as conn:
        cursor=conn.cursor()
        sql_request = f"UPDATE 'workflows' SET step = '{new_step}' where `index` = {index}"      
        print('sql_request :',cyan(sql_request,bold=True))
        cursor.execute(sql_request)
        result=1
    # ===================================================================
    loguer(env.level+' def END OF workflow_sqlite_update_step() in app.py : >')    
    env.level=env.level[:-1]
    return result
    
