#  def_reset_every_databases***
def reset_every_databases():
    '''
    MODIFIED : 2025-11-11T08:06:18.000Z

    description : reset every databases
    
    how to call it : result = reset_every_databases()
    '''
    route="/reset_every_databases"
    env.level+='-'
    print('\n'+env.level,white('def reset_every_databases() in app.py : >\n',bold=True))
    loguer(env.level+' def reset_every_databases() in app.py : >')
    # ===================================================================    
    action_type = 'replace'
    # WORKFLOWS
    print(red('RESET VARIABLES',bold=True))
    with open('./sqlite_databases_code/workflows/db_details.txt') as file:
        db_details_dict=json.loads(file.read())
    print('db_details_dict : \n',yellow(db_details_dict,bold=True))
    database = os.getcwd()+'/z_bases/workflows.db'
    database=database.replace("\\","/")
    print('database is :',database)
    print('table is :', db_details_dict["table_name"])
    conn=create_connection(database) # open connection to database
    if conn:
        # connection to database is OK
        c=conn.cursor()
        print(f'- Deleting table : {db_details_dict["table_name"]} =>')
        sql_request="drop table "+db_details_dict["table_name"]
        c.execute(sql_request)
        conn.commit()
        print('-- OK DONE : Deleted table : '+db_details_dict["table_name"])
        create_db_and_table(db_details_dict["db_name"],db_details_dict["table_name"])
        print(f'-- OK table {db_details_dict["table_name"]} reseted')     
    db_name='workflows'
    with open('./sqlite_databases_code/'+db_name+'/db_details.txt') as file:
        db_details_dict=json.loads(file.read())
    print('db_details_dict : \n',yellow(db_details_dict,bold=True))
    database = os.getcwd()+'/z_bases/'+db_name+'.db'
    database=database.replace("\\","/")
    print('database is :',database)
    print('table is :',db_details_dict['table_name'])
    lines=[]
    file='./DB_backups/workflows_init_20251109.csv'
    with open (file) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        lines = list(reader)
        if action_type=="replace":
            conn=create_connection(database) # open connection to database
            if conn:
                # connection to database is OK
                c=conn.cursor()
                print(f'- Deleting table : {db_details_dict["table_name"]} =>')
                sql_request="drop table "+db_details_dict["table_name"]
                c.execute(sql_request)
                conn.commit()
                print('-- OK DONE : Deleted table : '+db_details_dict["table_name"])
                create_db_and_table(db_details_dict["db_name"],db_details_dict["table_name"])
                print(f'-- OK table {db_details_dict["table_name"]} reseted')                  
            indexA=0
        else:
            indexA=sqlite_db_get_last_index(db_name)+1
        conn=create_connection(database) # open connection to database
        for row in lines:
            if conn:
                # connection to database is OK
                c=conn.cursor()
                # let's go to every lines one by one and let's extract url, targeted brand
                len_columns=len(db_details_dict['columns'])-1
                sqlite_data=[indexA]
                for cel in row:
                    sqlite_data.append(cel)
                print('\nsqlite_data :',cyan(sqlite_data,bold=True))
                sql_add=f"INSERT OR IGNORE into {db_details_dict['table_name']} (`index`,"
                i=0
                for col in db_details_dict['columns']:
                    print(col)
                    if i<len_columns:
                        sql_add=sql_add+col+","
                    else:
                        sql_add=sql_add+col+")"
                    i+=1
                sql_add=sql_add+' VALUES (?,'
                i=0
                for col in db_details_dict['columns']:
                    print(col)
                    if i<len_columns:
                        sql_add=sql_add+"?,"
                    else:
                        sql_add=sql_add+'?)'
                    i+=1
                #sql_add="INSERT OR IGNORE into truc (`index`,premier,deuxieme,troisieme,quatrieme) VALUES (?,?,?,?,?)"
                print('\nsql_add :',cyan(sql_add,bold=True))
            c.execute(sql_add, sqlite_data)
            print(green("==> OK Done : demo data ingested",bold=True))
            indexA+=1
            conn.commit()

    #VARIABLES
    print(red('RESET VARIABLES',bold=True))
    with open('./sqlite_databases_code/variables/db_details.txt') as file:
        db_details_dict=json.loads(file.read())
    print('db_details_dict : \n',yellow(db_details_dict,bold=True))
    file=open('./sqlite_databases_code/variables/init/variables.csv','w')
    ligne_out=''
    len_columns=len(db_details_dict['columns'])-1
    i=0        
    for col in db_details_dict['columns']:
        if i<len_columns:
            ligne_out=ligne_out+col+','
        else:
            ligne_out=ligne_out+col
        i+=1
    file.write(ligne_out+'\n')
    for i in range (0,10):
        ligne_out='name'+str(i)+','+'environment_name'+str(i)+','+'value'+str(i)+','+'description'+str(i)+','+'comment'+str(i)+','+'used_by'+str(i)           
        file.write(ligne_out+'\n')
    file.close()  
    create_db_and_table(db_details_dict['db_name'],db_details_dict['table_name'])
    
    db_name = "variables"
    print("\ndb_name : ",db_name)
    print("\naction_type : ",action_type)        

    result=1
    if result==1:
        with open('./sqlite_databases_code/variables/db_details.txt') as file:
            db_details_dict=json.loads(file.read())
        print('db_details_dict : \n',yellow(db_details_dict,bold=True))
        database = os.getcwd()+'/z_bases/'+db_name+'.db'
        database=database.replace("\\","/")
        print('database is :',database)
        print('table is :',db_details_dict['table_name'])
        lines=[]
        file='./DB_backups/variables_ok_20251109.csv'
        with open (file) as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            lines = list(reader)
            if action_type=="replace":
                conn=create_connection(database) # open connection to database
                if conn:
                    # connection to database is OK
                    c=conn.cursor()
                    print(f'- Deleting table : {db_details_dict["table_name"]} =>')
                    sql_request="drop table "+db_details_dict["table_name"]
                    c.execute(sql_request)
                    conn.commit()
                    print('-- OK DONE : Deleted table : '+db_details_dict["table_name"])
                    create_db_and_table(db_details_dict["db_name"],db_details_dict["table_name"])
                    print(f'-- OK table {db_details_dict["table_name"]} reseted')                  
                indexA=0
            else:
                indexA=sqlite_db_get_last_index(db_name)+1
            conn=create_connection(database) # open connection to database
            for row in lines:
                if conn:
                    # connection to database is OK
                    c=conn.cursor()
                    # let's go to every lines one by one and let's extract url, targeted brand
                    len_columns=len(db_details_dict['columns'])-1
                    sqlite_data=[indexA]
                    for cel in row:
                        sqlite_data.append(cel)
                    print('\nsqlite_data :',cyan(sqlite_data,bold=True))
                    sql_add=f"INSERT OR IGNORE into {db_details_dict['table_name']} (`index`,"
                    i=0
                    for col in db_details_dict['columns']:
                        print(col)
                        if i<len_columns:
                            sql_add=sql_add+col+","
                        else:
                            sql_add=sql_add+col+")"
                        i+=1
                    sql_add=sql_add+' VALUES (?,'
                    i=0
                    for col in db_details_dict['columns']:
                        print(col)
                        if i<len_columns:
                            sql_add=sql_add+"?,"
                        else:
                            sql_add=sql_add+'?)'
                        i+=1
                    #sql_add="INSERT OR IGNORE into truc (`index`,premier,deuxieme,troisieme,quatrieme) VALUES (?,?,?,?,?)"
                    print('\nsql_add :',cyan(sql_add,bold=True))
                c.execute(sql_add, sqlite_data)
                print(green("==> OK Done : demo data ingested",bold=True))
                indexA+=1
                conn.commit()  
    # FUNCTIONS
    with open('./sqlite_databases_code/functions/db_details.txt') as file:
        db_details_dict=json.loads(file.read())
    print('db_details_dict : \n',yellow(db_details_dict,bold=True))
    file=open('./sqlite_databases_code/functions/init/functions.csv','w')
    ligne_out=''
    len_columns=len(db_details_dict['columns'])-1
    i=0        
    for col in db_details_dict['columns']:
        if i<len_columns:
            ligne_out=ligne_out+col+','
        else:
            ligne_out=ligne_out+col
        i+=1
    file.write(ligne_out+'\n')
    for i in range (0,10):
        ligne_out='name'+str(i)+','+'environment_name'+str(i)+','+'description'+str(i)+','+'called_function'+str(i)+','+'input_variables'+str(i)+','+'output_variables'+str(i)+','+'comment'+str(i)           
        file.write(ligne_out+'\n')
    file.close()  
    create_db_and_table(db_details_dict['db_name'],db_details_dict['table_name'])
    
    db_name = "functions"
    print("\ndb_name : ",db_name)
    print("\naction_type : ",action_type)        

    result=1
    if result==1:
        with open('./sqlite_databases_code/functions/db_details.txt') as file:
            db_details_dict=json.loads(file.read())
        print('db_details_dict : \n',yellow(db_details_dict,bold=True))
        database = os.getcwd()+'/z_bases/'+db_name+'.db'
        database=database.replace("\\","/")
        print('database is :',database)
        print('table is :',db_details_dict['table_name'])
        lines=[]
        file='./DB_backups/functions_ok_20251109.csv'
        with open (file) as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            lines = list(reader)
            if action_type=="replace":
                conn=create_connection(database) # open connection to database
                if conn:
                    # connection to database is OK
                    c=conn.cursor()
                    print(f'- Deleting table : {db_details_dict["table_name"]} =>')
                    sql_request="drop table "+db_details_dict["table_name"]
                    c.execute(sql_request)
                    conn.commit()
                    print('-- OK DONE : Deleted table : '+db_details_dict["table_name"])
                    create_db_and_table(db_details_dict["db_name"],db_details_dict["table_name"])
                    print(f'-- OK table {db_details_dict["table_name"]} reseted')                  
                indexA=0
            else:
                indexA=sqlite_db_get_last_index(db_name)+1
            conn=create_connection(database) # open connection to database
            for row in lines:
                if conn:
                    # connection to database is OK
                    c=conn.cursor()
                    # let's go to every lines one by one and let's extract url, targeted brand
                    len_columns=len(db_details_dict['columns'])-1
                    sqlite_data=[indexA]
                    for cel in row:
                        sqlite_data.append(cel)
                    print('\nsqlite_data :',cyan(sqlite_data,bold=True))
                    sql_add=f"INSERT OR IGNORE into {db_details_dict['table_name']} (`index`,"
                    i=0
                    for col in db_details_dict['columns']:
                        print(col)
                        if i<len_columns:
                            sql_add=sql_add+col+","
                        else:
                            sql_add=sql_add+col+")"
                        i+=1
                    sql_add=sql_add+' VALUES (?,'
                    i=0
                    for col in db_details_dict['columns']:
                        print(col)
                        if i<len_columns:
                            sql_add=sql_add+"?,"
                        else:
                            sql_add=sql_add+'?)'
                        i+=1
                    #sql_add="INSERT OR IGNORE into truc (`index`,premier,deuxieme,troisieme,quatrieme) VALUES (?,?,?,?,?)"
                    print('\nsql_add :',cyan(sql_add,bold=True))
                c.execute(sql_add, sqlite_data)
                print(green("==> OK Done : demo data ingested",bold=True))
                indexA+=1
                conn.commit()  
    # ACCOUNT KEYS
    with open('./sqlite_databases_code/account_keys/db_details.txt') as file:
        db_details_dict=json.loads(file.read())
    print('db_details_dict : \n',yellow(db_details_dict,bold=True))
    file=open('./sqlite_databases_code/account_keys/init/account_keys.csv','w')
    ligne_out=''
    len_columns=len(db_details_dict['columns'])-1
    i=0        
    for col in db_details_dict['columns']:
        if i<len_columns:
            ligne_out=ligne_out+col+','
        else:
            ligne_out=ligne_out+col
        i+=1
    file.write(ligne_out+'\n')
    for i in range (0,10):
        ligne_out='name'+str(i)+','+'type'+str(i)+','+'username'+str(i)+','+'password'+str(i)+','+'key'+str(i)+','+'comment'+str(i)           
        file.write(ligne_out+'\n')
    file.close()  
    create_db_and_table(db_details_dict['db_name'],db_details_dict['table_name'])
    
    db_name = "account_keys"
    print("\ndb_name : ",db_name)
    print("\naction_type : ",action_type)        
    result=1
    if result==1:
        with open('./sqlite_databases_code/account_keys/db_details.txt') as file:
            db_details_dict=json.loads(file.read())
        print('db_details_dict : \n',yellow(db_details_dict,bold=True))
        database = os.getcwd()+'/z_bases/'+db_name+'.db'
        database=database.replace("\\","/")
        print('database is :',database)
        print('table is :',db_details_dict['table_name'])
        lines=[]
        file='./DB_backups/account_keys_ok_20251109.csv'
        with open (file) as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            lines = list(reader)
            if action_type=="replace":
                conn=create_connection(database) # open connection to database
                if conn:
                    # connection to database is OK
                    c=conn.cursor()
                    print(f'- Deleting table : {db_details_dict["table_name"]} =>')
                    sql_request="drop table "+db_details_dict["table_name"]
                    c.execute(sql_request)
                    conn.commit()
                    print('-- OK DONE : Deleted table : '+db_details_dict["table_name"])
                    create_db_and_table(db_details_dict["db_name"],db_details_dict["table_name"])
                    print(f'-- OK table {db_details_dict["table_name"]} reseted')                  
                indexA=0
            else:
                indexA=sqlite_db_get_last_index(db_name)+1
            conn=create_connection(database) # open connection to database
            for row in lines:
                if conn:
                    # connection to database is OK
                    c=conn.cursor()
                    # let's go to every lines one by one and let's extract url, targeted brand
                    len_columns=len(db_details_dict['columns'])-1
                    sqlite_data=[indexA]
                    for cel in row:
                        sqlite_data.append(cel)
                    print('\nsqlite_data :',cyan(sqlite_data,bold=True))
                    sql_add=f"INSERT OR IGNORE into {db_details_dict['table_name']} (`index`,"
                    i=0
                    for col in db_details_dict['columns']:
                        print(col)
                        if i<len_columns:
                            sql_add=sql_add+col+","
                        else:
                            sql_add=sql_add+col+")"
                        i+=1
                    sql_add=sql_add+' VALUES (?,'
                    i=0
                    for col in db_details_dict['columns']:
                        print(col)
                        if i<len_columns:
                            sql_add=sql_add+"?,"
                        else:
                            sql_add=sql_add+'?)'
                        i+=1
                    #sql_add="INSERT OR IGNORE into truc (`index`,premier,deuxieme,troisieme,quatrieme) VALUES (?,?,?,?,?)"
                    print('\nsql_add :',cyan(sql_add,bold=True))
                c.execute(sql_add, sqlite_data)
                print(green("==> OK Done : demo data ingested",bold=True))
                indexA+=1
                conn.commit()
    # API_CALLS
    with open('./sqlite_databases_code/api_calls/db_details.txt') as file:
        db_details_dict=json.loads(file.read())
    print('db_details_dict : \n',yellow(db_details_dict,bold=True))
    file=open('./sqlite_databases_code/api_calls/init/api_calls.csv','w')
    ligne_out=''
    len_columns=len(db_details_dict['columns'])-1
    i=0        
    for col in db_details_dict['columns']:
        if i<len_columns:
            ligne_out=ligne_out+col+','
        else:
            ligne_out=ligne_out+col
        i+=1
    file.write(ligne_out+'\n')
    for i in range (0,10):
        ligne_out='name'+str(i)+','+'fqdn'+str(i)+','+'relative_url'+str(i)+','+'documentation'+str(i)+','+'method'+str(i)+','+'description'+str(i)+','+'payload'+str(i)+','+'header'+str(i)+','+'body'+str(i)+','+'query_params'+str(i)+','+'custom_variables'+str(i)+','+'authentication_profile'+str(i)+','+'inputs_variables'+str(i)+','+'output_variables'+str(i)           
        file.write(ligne_out+'\n')
    file.close()  
    create_db_and_table(db_details_dict['db_name'],db_details_dict['table_name'])
    
    db_name = "api_calls"
    print("\ndb_name : ",db_name)
    print("\naction_type : ",action_type)        

    result=1
    if result==1:
        with open('./sqlite_databases_code/'+db_name+'/db_details.txt') as file:
            db_details_dict=json.loads(file.read())
        print('db_details_dict : \n',yellow(db_details_dict,bold=True))
        database = os.getcwd()+'/z_bases/'+db_name+'.db'
        database=database.replace("\\","/")
        print('database is :',database)
        print('table is :',db_details_dict['table_name'])
        lines=[]
        file='./DB_backups/api_calls_ok_20251109.csv'
        with open (file) as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            lines = list(reader)
            if action_type=="replace":
                conn=create_connection(database) # open connection to database
                if conn:
                    # connection to database is OK
                    c=conn.cursor()
                    print(f'- Deleting table : {db_details_dict["table_name"]} =>')
                    sql_request="drop table "+db_details_dict["table_name"]
                    c.execute(sql_request)
                    conn.commit()
                    print('-- OK DONE : Deleted table : '+db_details_dict["table_name"])
                    create_db_and_table(db_details_dict["db_name"],db_details_dict["table_name"])
                    print(f'-- OK table {db_details_dict["table_name"]} reseted')                  
                indexA=0
            else:
                indexA=sqlite_db_get_last_index(db_name)+1
            conn=create_connection(database) # open connection to database
            for row in lines:
                if conn:
                    # connection to database is OK
                    c=conn.cursor()
                    # let's go to every lines one by one and let's extract url, targeted brand
                    len_columns=len(db_details_dict['columns'])-1
                    sqlite_data=[indexA]
                    for cel in row:
                        sqlite_data.append(cel)
                    print('\nsqlite_data :',cyan(sqlite_data,bold=True))
                    sql_add=f"INSERT OR IGNORE into {db_details_dict['table_name']} (`index`,"
                    i=0
                    for col in db_details_dict['columns']:
                        print(col)
                        if i<len_columns:
                            sql_add=sql_add+col+","
                        else:
                            sql_add=sql_add+col+")"
                        i+=1
                    sql_add=sql_add+' VALUES (?,'
                    i=0
                    for col in db_details_dict['columns']:
                        print(col)
                        if i<len_columns:
                            sql_add=sql_add+"?,"
                        else:
                            sql_add=sql_add+'?)'
                        i+=1
                    #sql_add="INSERT OR IGNORE into truc (`index`,premier,deuxieme,troisieme,quatrieme) VALUES (?,?,?,?,?)"
                    print('\nsql_add :',cyan(sql_add,bold=True))
                c.execute(sql_add, sqlite_data)
                print(green("==> OK Done : demo data ingested",bold=True))
                indexA+=1
                conn.commit()    
    
    result=1
    # ===================================================================
    loguer(env.level+' def END OF reset_every_databases() in app.py : >')    
    env.level=env.level[:-1]
    return result
    
