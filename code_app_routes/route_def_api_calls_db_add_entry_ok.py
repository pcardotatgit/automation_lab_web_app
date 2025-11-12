#  def_api_calls_db_add_entry_ok***
@app.route('/api_calls_db_add_entry_ok', methods=['GET'])
def api_calls_db_add_entry_ok():
    '''
    Flask Route for the api_calls_db_add_entry Database Update an entry
    '''
    route="/api_calls_db_add_entry_ok"
    env.level+='-'
    print('\n'+env.level,white('route api_calls_db_add_entry_ok() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route api_calls_db_add_entry_ok() in ***app.py*** : >')
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        name=request.args.get("name")
        print("\nname: ",name)
        fqdn=request.args.get("fqdn")
        print("\nfqdn: ",fqdn)
        relative_url=request.args.get("relative_url")
        print("\nrelative_url: ",relative_url)
        documentation=request.args.get("documentation")
        print("\ndocumentation: ",documentation)
        method=request.args.get("method")
        print("\nmethod: ",method)
        description=request.args.get("description")
        print("\ndescription: ",description)
        payload=request.args.get("payload")
        print("\npayload: ",payload)
        header=request.args.get("header")
        print("\nheader: ",header)
        body=request.args.get("body")
        print("\nbody: ",body)
        query_params=request.args.get("query_params")
        print("\nquery_params: ",query_params)
        custom_variables=request.args.get("custom_variables")
        print("\ncustom_variables: ",custom_variables)
        authentication_profile=request.args.get("authentication_profile")
        print("\nauthentication_profile: ",authentication_profile)
        inputs_variables=request.args.get("inputs_variables")
        print("\ninputs_variables: ",inputs_variables)
        output_variables=request.args.get("output_variables")
        print("\noutput_variables: ",output_variables)

        db_name=request.args.get("db_name")
        print('db_name :',db_name)     
        with open('./sqlite_databases_code/'+db_name+'/db_details.txt') as file:
            db_details_dict=json.loads(file.read())
        print('db_details_dict : \n',yellow(db_details_dict,bold=True)) 
        database = os.getcwd()+'/z_bases/'+db_name+'.db'
        database=database.replace("\\","/")
        table=db_details_dict['table_name']
        print('database is :',database) 
        print('table is :',table)          
        # Get last index value in SQLITE DB
        new_index=sqlite_db_get_last_index(db_name)+1        
        print('new_index is :',new_index)  
        sqlite_data=(new_index,name,fqdn,relative_url,documentation,method,description,payload,header,body,query_params,custom_variables,authentication_profile,inputs_variables,output_variables)
        sql_add=f"INSERT OR IGNORE into {table} (`index`,name,fqdn,relative_url,documentation,method,description,payload,header,body,query_params,custom_variables,authentication_profile,inputs_variables,output_variables) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        print('sqlite_data :',sqlite_data)     
        print('sql_add :',sql_add)          
        con = sqlite3.connect(database)       
        try:
            cur = con.cursor()
            cur.execute(sql_add,sqlite_data)
            con.commit()
            print(green('OK DONE ENTRY DELETED',bold=True))
            image="../static/images/ok.png" 
            message1="Entry Added"
            message2="Entry was added to DB"
            message3=f"/{db_name}_dashboard"
            message4=f"{db_name}_dasbhoard"        
            PAGE_DESTINATION="operation_done"
            page_name="operation_done.html"            
            loguer(env.level+' route END OF machin_db_add_entry_ok() in ***app.py*** : >')    
            env.level=env.level[:-1]        
            return render_template('main_index.html',route=route,USERNAME=session['user'],PAGE_DESTINATION=PAGE_DESTINATION,message1=message1,message2=message2,message3=message3,message4=message4,image=image,page_name=page_name) 
        except:
            print(red('Error',bold=True))
            image="../static/images/nok.png" 
            message1="Error"
            message2="An error occured"
            message3=f"/{db_name}_dashboard"
            message4=f"{db_name}_dasbhoard"        
            PAGE_DESTINATION="operation_done"
            page_name="operation_done.html"            
            loguer(env.level+' route END OF machin_db_add_entry_ok() in ***app.py*** : >')    
            env.level=env.level[:-1]        
            return render_template('main_index.html',route=route,USERNAME=session['user'],PAGE_DESTINATION=PAGE_DESTINATION,message1=message1,message2=message2,message3=message3,message4=message4,image=image,page_name=page_name)

