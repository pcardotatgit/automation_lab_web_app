#  def_sqlite_db_get_last_index***
def sqlite_db_get_last_index(db_name):
    '''
    MODIFIED : 2025-10-02T08:49:29.000Z
    description : retrieve highest index value of entries into a database
    
    how to call it : last_index=sqlite_db_get_last_index(db_name)
    
        db_name : database name ( without .db extension )
    '''
    route="/sqlite_db_get_last_index"
    env.level+='-'
    print('\n'+env.level,white('def sqlite_db_get_last_index() in app.py  : >\n',bold=True))
    loguer(env.level+' def sqlite_db_get_last_index() in app.py  : > ')
    # ===================================================================    
    with open('./sqlite_databases_code/'+db_name+'/db_details.txt') as file:
        db_details_dict=json.loads(file.read())
    print('db_details_dict : \n',yellow(db_details_dict,bold=True))
    database = os.getcwd()+'/z_bases/machin.db'
    database=database.replace("\\","/")
    print('database is :',database)
    if '.db' not in db_name:
        db_name = db_name+".db"
    table_name = db_details_dict["table_name"]
    print('table_name is :',table_name)    
    index=0
    with sqlite3.connect(database) as conn:
        cursor=conn.cursor()
        sql_request = f"SELECT * from {table_name}"
        print('\nsql_request : ',sql_request)
        try:
            cursor.execute(sql_request)
            for resultat in cursor:
                #print(resultat)
                if resultat[0]> index:
                    index=resultat[0]
        except:
            sys.exit("couldn't read database")
    # ===================================================================
    loguer(env.level+' def END OF sqlite_db_get_last_index() in app.py  : > ')
    env.level=env.level[:-1]
    return index
    

