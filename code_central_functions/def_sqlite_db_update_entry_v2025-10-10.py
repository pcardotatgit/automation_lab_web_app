#  def_sqlite_db_update_entry***
def sqlite_db_update_entry(database,table,where_clause,sql_fields,sql_data_list):
    '''
    MODIFIED : 2025-10-01
    description : Update a row into the sqllite Database
    
    how to call it :     resultats = sqlite_db_update_entry(database,table,where_clause,sql_fields,sql_data_list) 
        database : DB name
        table : table name
        where_clause : where clause for selecting a row ex : where index = 2
        sql_fields : columns field list
        sql_data_list : data list of new data to ingest into the row
    '''
    route="/sqlite_db_update_entry"
    env.level+='-'
    print('\n'+env.level,white('def sqlite_db_update_entry() in app.py  : >\n',bold=True))
    loguer(env.level+' def sqlite_db_update_entry() in app.py  : > ')
    # ===================================================================    
    if '.db' not in database:
        database = os.getcwd()+'/z_bases/'+database+'.db'
    else:
        database = os.getcwd()+'/z_bases/'+database
    database=database.replace("\\","/")
    #database = './z_bases/'+database+'.db'
    print('database is :',database)    
    with sqlite3.connect(database) as conn:
        cursor=conn.cursor()
        print('sql_data_list :',cyan(sql_data_list,bold=True))             
        sql_data=('')
        sql_data=sql_data_list
        sql_request = f"UPDATE {table} SET "
        i=0
        len_sql_data_list=len(sql_data_list)
        for item in sql_fields:
            if i<len_sql_data_list-1:
                if i==0:
                    sql_request =sql_request +"`"+item +"` = "+str(sql_data_list[i])+" , "
                else:
                    sql_request =sql_request + item +" = '"+sql_data_list[i]+"' , "
            else:
                sql_request =sql_request + item +" = '"+sql_data_list[i]+"'"
            i+=1
        if where_clause!='':
            if 'where' not in sql_request:
                sql_request=sql_request+' where '+where_clause
            else:
                sql_request=sql_request+' '+where_clause           
        print('sql_request :',cyan(sql_request,bold=True))
        cursor.execute(sql_request)
        result=1
    # ===================================================================
    loguer(env.level+' def END OF sqlite_db_update_entry() in app.py  : > ')
    env.level=env.level[:-1]
    return(result) 
   
