#  def_workflows_solution***
@app.route('/workflows_solution', methods=['GET'])
def workflows_solution():
    '''
    Created : 2025-11-10T08:50:38.000Z

    description : install example of workflow solution
    '''
    route="/workflows_solution"
    env.level+='-'
    print('\n'+env.level,white('route workflows_solution() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route workflows_solution() in ***app.py*** : >')
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        action_type = 'replace'
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
        file='./DB_backups/workflows_full_solution_ok_20251109.csv'
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
            
        message1="Ok Done"
        image="../static/images/ok.png" 
        message2="Example of workflow soluton installed"
        message3="/workflows"
        message4="Worflows"
        PAGE_DESTINATION="operation_done"
        page_name="operation_done.html"
        loguer(env.level+' route END OF workflows_solution() in ***app.py*** : >')
        # ===================================================================
        env.level=env.level[:-1]
        return render_template('main_index.html',route=route,USERNAME=session['user'],PAGE_DESTINATION=PAGE_DESTINATION,message1=message1,message2=message2,message3=message3,message4=message4,image=image,page_name=page_name)
        
