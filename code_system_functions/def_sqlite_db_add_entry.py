#  def_sqlite_db_add_entry***
def sqlite_db_add_entry(database,sql_request,sql_data_list):
    '''
    TO DEBUG !!
    MODIFIED : 2025-10-09T15:09:17.000Z
    description : add a new entry in sqlite database
    
    how to call it : result=sqlite_db_add_entry(database,sql_request,sql_data_list)
    '''
    route="/sqlite_db_add_entry"
    env.level+='-'
    print('\n'+env.level,white('def sqlite_db_add_entry() in app.py : >\n',bold=True))
    loguer(env.level+' def sqlite_db_add_entry() in app.py : >')
    # ===================================================================    
    print('database :',database)
    print('sql_request :',sql_request)     
    print('sql_data_list :',sql_data_list)
    con = sqlite3.connect(database)
    try:
        cur = con.cursor()
        cur.execute(sql_add,sqlite_data)
        con.commit()
        print(green('OK DONE ENTRY ADDED INTEO DATABASE',bold=True))
        loguer(env.level+' route END OF machin_db_add_entry_ok() in ***app.py*** : >')
        env.level=env.level[:-1]
        return 1
    except:
        print(red('Error : could not add entry into database',bold=True))
        loguer(env.level+' route END OF machin_db_add_entry_ok() in ***app.py*** : >')
        env.level=env.level[:-1]
        return 0
