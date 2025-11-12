#  def_sqlite_db_select_entry***
def sqlite_db_select_entry(database,table,where_clause):
    '''
    MODIFIED : 2025-09-26T08:40:02.000Z
    description : Search an entry in the selected SQLITE database
    
    how to call it :     resultats = sqlite_db_select_entry(database,table,where_clause) 
    '''
    route="/sqlite_db_select_entry"
    env.level+='-'
    print('\n'+env.level,white('def sqlite_db_select_entry() in app.py : >\n',bold=True))
    loguer(env.level+' def sqlite_db_select_entry() in app.py : >')
    # ===================================================================    
    database = os.getcwd()+'/z_bases/'+database+'.db'
    database=database.replace("\\","/")
    #database = './z_bases/'+database+'.db'
    print('database is :',database)    
    liste=[]
    columns=[]
    with sqlite3.connect(database) as conn:
        cursor=conn.cursor()           
        sql_request = f"SELECT * from {table} {where_clause}"
        print('\nsql_request : ',cyan(sql_request+'\n',bold=True))
        try:
            cursor.execute(sql_request)
            for resultat in cursor:
                print('entry found : ',resultat)
                liste.append(resultat)
        except:
            print(red('Error reading database',bold=True))
            sys.exit("couldn't read database")
    # ===================================================================
    print(' Result liste in sqlite_db_select_entry() : ',cyan(liste,bold=True))
    loguer(env.level+' def END OF sqlite_db_select_entry() in app.py : >')    
    env.level=env.level[:-1]
    return(liste) 
   