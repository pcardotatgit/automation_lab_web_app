#  def_create_db_and_table***
def create_db_and_table(db_name,table):
    '''
    MODIFIED : 2025-09-23T16:08:36.000Z
    description : create database and one table
    
    how to call it : create_db_and_table(db_name,table)
    '''
    route="/create_db_and_table"
    env.level+='-'
    print('\n'+env.level,white('def create_db_and_table() in app.py : >\n',bold=True))
    loguer(env.level+' def create_db_and_table() in app.py : >')
    # ===================================================================    
    print("\ndb_name : ",db_name)   
    print("table_name : ",table) 
    with open('./sqlite_databases_code/'+db_name+'/db_details.txt') as file:
        db_details_dict=json.loads(file.read())
    print('\ndb_details_dict : \n',yellow(db_details_dict,bold=True))    
    len_columns=len(db_details_dict['columns'])-1  
    #with sqlite3.connect(':memory:') as conn:
    with sqlite3.connect('./z_bases/'+db_name+'.db') as conn:
        c=conn.cursor()
        print(f"--- table : {table} creation")
        sql_create='CREATE TABLE IF NOT EXISTS '+table +'(`index` int PRIMARY KEY,'
        i=0
        for col in db_details_dict['columns']:
            if i<len_columns:
                sql_create=sql_create+col+' text ,'
            else:
                sql_create=sql_create+col+' text)'
            i+=1
        print('sql_create : \n',cyan(sql_create,bold=True))
        c.execute(sql_create)
        print(green(f"--- OK {table} table created",bold=True))
    # ===================================================================
    #loguer(env.level+' def END OF create_db_and_table() in app.py : >')    
    env.level=env.level[:-1]
    return() 
    
