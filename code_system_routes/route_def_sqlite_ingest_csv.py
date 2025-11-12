#  def_sqlite_ingest_csv***
@app.route('/sqlite_ingest_csv', methods=['GET','POST'])
def sqlite_ingest_csv():
    '''
    Created : 2025-10-10
    description : download a csv file and store it into ./tmp
    '''
    route="/sqlite_ingest_csv"
    env.level+='-'
    print('\n'+env.level,white('route sqlite_ingest_csv() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route sqlite_ingest_csv() in ***app.py*** : >')
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        result=0
        db_name = request.form['db_name']
        print("\ndb_name : ",db_name)
        action_type = request.form['action_type']
        print("\naction_type : ",action_type)        
        # download the CSV file
        if request.method == 'POST':
            if 'file' not in request.files:
                return redirect(request.url)
            file = request.files['file']
            if file.filename == '':
                return redirect(request.url)
            if file:
                filename = file.filename
                print('filename : ',filename+'\n')
                filename='csv_file.csv'
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                result=1
        # Prepare the resulting Next Web Page
        
        if result==1:
            with open('./sqlite_databases_code/'+db_name+'/db_details.txt') as file:
                db_details_dict=json.loads(file.read())
            print('db_details_dict : \n',yellow(db_details_dict,bold=True))
            database = os.getcwd()+'/z_bases/'+db_name+'.db'
            database=database.replace("\\","/")
            print('database is :',database)
            print('table is :',db_details_dict['table_name'])
            lines=[]
            file='./temp/csv_file.csv'
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
            image="../static/images/ok.png"
            message1="Database Updated"
            message2="CSV file is in [ ./temp ]"
            message3=f"/{db_name}_dashboard"
            message4=f"{db_name}_dashboard"
        else:
            image="../static/images/nok.png"
            message1="ERROR"
            message2="File Not downloaded"
            message3="/"
            message4="Home"
        PAGE_DESTINATION="z_sqlite_ingest_csv_result"
        page_name="z_sqlite_ingest_csv_result.html"
        loguer(env.level+' route END OF sqlite_ingest_csv() in ***app.py*** : >')
        # ===================================================================
        env.level=env.level[:-1]
        return render_template('main_index.html',route=route,USERNAME=session['user'],PAGE_DESTINATION=PAGE_DESTINATION,message1=message1,message2=message2,message3=message3,message4=message4,image=image,page_name=page_name)
        
