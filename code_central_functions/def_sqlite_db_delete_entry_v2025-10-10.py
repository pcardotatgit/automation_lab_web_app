#  def_sqlite_db_delete_entry***
def sqlite_db_delete_entry(db_name,row):
    '''
    MODIFIED : 2025-10-01T16:57:57.000Z

    description : delete a row from the sqllite Database
    
    how to call it : result = sqlite_db_delete_entry(db_name,row)
    '''
    route="/sqlite_db_delete_entry"
    env.level+='-'
    print('\n'+env.level,white('def sqlite_db_delete_entry() in app.py  : >\n',bold=True))
    loguer(env.level+' def sqlite_db_delete_entry() in app.py  : > ')
    # ===================================================================    
    print()
    print('db_name :',db_name)     
    with open('./sqlite_databases_code/'+db_name+'/db_details.txt') as file:
        db_details_dict=json.loads(file.read())
    print('db_details_dict : \n',yellow(db_details_dict,bold=True)) 
    database = os.getcwd()+'/z_bases/'+db_name+'.db'
    database=database.replace("\\","/")
    table=db_details_dict['table_name']
    print('database is :',database) 
    print('table is :',table)   
    print('row to delete is :',row)     
    sql=f"DELETE FROM {table} where `index` = "+row
    print('\nsql request :',yellow(sql,bold=True))
    con = sqlite3.connect(database)       
    try:
        cur = con.cursor()
        cur.execute(sql)
        con.commit()
        print(green('OK DONE ENTRY DELETED',bold=True))
        loguer(env.level+' def END OF sqlite_db_delete_entry() in app.py  : > ')
        env.level=env.level[:-1]        
        return 1
    except:
        print(red('Error',bold=True))
        loguer(env.level+' def END OF sqlite_db_delete_entry() in app.py  : > ')
        env.level=env.level[:-1]                
        return 0


