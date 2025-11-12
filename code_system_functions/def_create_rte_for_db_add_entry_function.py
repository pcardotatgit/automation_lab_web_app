#  def_create_rte_for_db_add_entry_function***
def create_rte_for_db_add_entry_function(name):
    '''
    MODIFIED : 2025-10-09

    description : create route for db add a new entry into database
    
    how to call it : create_rte_for_db_add_entry_function(name)
        name : de name
    ''' 
    route="/create_rte_for_db_add_entry_function"
    env.level+='-'
    print('\n'+env.level,white('def create_rte_for_db_add_entry_function() in app.py : >\n',bold=True))
    loguer(env.level+' def create_rte_for_db_add_entry_function() in app.py : >')
    # ===================================================================    
    db=name
    db_name=name.replace('./zbases/','')
    db_name=db_name.replace('.db','')
    name=name+'_db_add_entry'
    filename='./code_app_routes/route_def_'+name+'.py'
    filename2='/route_def_'+name+'.py'
    description='Flask Route for the '+name+' Database Update an entry'
    print()
    print(' filename :\n',yellow(filename,bold=True))
    print(' filename2 :\n',yellow(filename2,bold=True))
    print()
    print(magenta('--> CALL  A SUB FUNCTION :',bold=True))
    # check if file already exits
    with open('./code_architecture/app_routes.txt') as file:
        text_content2=file.read()    
    fichier_route = Path('./code_app_routes/route_def_'+name+'.py')    
    if fichier_route.is_file() or filename in text_content2:
        print(red('ERROR !!',bold=True))
        print(filename+' already exists ! Choose another name')
        message1="ALREADY EXIST"
        image="../static/images/nok.png" 
        message2="Choose another name"
        message3="/home"
        message4="Back Home"        
        PAGE_DESTINATION="operation_done"
        page_name="z_operation_done.html"
        loguer(env.level+' route END OF example_name() in ***app.py*** : >')
        # ===================================================================
        env.level=env.level[:-1]
        return 0
    else:
        print(yellow(f'     {filename} does NOT exists. Let s create it',bold=True))
        route="/"+db+"_db_add_entry"
        title="FLASK APP GENERATOR"
        with open('./sqlite_databases_code/'+db+'/db_details.txt') as file:
            db_details_dict=json.loads(file.read())
        print('db_details_dict : \n',yellow(db_details_dict,bold=True))       
        # STEP 1 create the formular
        text_content='''#  def_'''+db+'''_db_add_entry***
@app.route('/'''+db+'''_db_add_entry', methods=['GET'])
def '''+db+'''_db_add_entry():
    \'\'\'
    '''+description+'''
    \'\'\'
    route="/'''+db+'''_db_add_entry"
    env.level+=\'-\'
    print(\'\\n\'+env.level,white(\'route '''+db+'''_db_add_entry() in ***app.py*** : >\\n\',bold=True))
    loguer(env.level+\' route '''+db+'''_db_add_entry() in ***app.py*** : >\')
    if not session.get(\'logged_in\'):
        return render_template(\'login.html\')
    else:
        db_name = "'''+db+'''.db"
        column_list=[\''''
        len_columns=len(db_details_dict['columns'])-1
        i=0
        for col in db_details_dict['columns']:
            print(col)
            if i<len_columns:
                text_content=text_content+col+"','"
            else:
                text_content=text_content+col
            i=i+1
        text_content=text_content+'''\']
        print(\'\\ncolumn_list :\',cyan(column_list,bold=True))
        index=sqlite_db_get_last_index(\''''+db+'''\')
        index+=1        
        print(\'index : \',index)
        PAGE_DESTINATION="z_sqlite_db_add_entry"
        page_name="z_sqlite_db_add_entry.html"
        db_name=db_name.split(\'.\')[0]
        loguer(env.level+\' route END OF example_name() in ***app.py*** : >\')
        # ===================================================================
        env.level=env.level[:-1]
        return render_template(\'main_index.html\',route=route,USERNAME=session[\'user\'],PAGE_DESTINATION=PAGE_DESTINATION,page_name=page_name,column_list=column_list,index=index,db_name=db_name)
 
'''        
        filename='./code_app_routes/route_def_'+db+'_db_add_entry.py'
        with open(filename,"w") as fichier:
            fichier.write(text_content)     
        with open('./code_architecture/app_routes.txt',"a+") as fichier:
            filename2=filename2.replace('/','')
            fichier.write(filename2+'\n')  
        # STEP 2 create the add entry in sqlite data base route           
        text_content='''#  def_'''+db+'''_db_add_entry_ok***
@app.route('/'''+db+'''_db_add_entry_ok', methods=['GET'])
def '''+db+'''_db_add_entry_ok():
    \'\'\'
    '''+description+'''
    \'\'\'
    route="/'''+db+'''_db_add_entry_ok"
    env.level+=\'-\'
    print(\'\\n\'+env.level,white(\'route '''+db+'''_db_add_entry_ok() in ***app.py*** : >\\n\',bold=True))
    loguer(env.level+\' route '''+db+'''_db_add_entry_ok() in ***app.py*** : >\')
    if not session.get(\'logged_in\'):
        return render_template(\'login.html\')
    else:\n'''
        for col in db_details_dict['columns']:
            print(col)
            text_content=text_content+'        '+col+'=request.args.get("'+col+'")\n        print("\\n'+col+': ",'+col+')\n'
        text_content=text_content+'''
        db_name=request.args.get("db_name")
        print(\'db_name :\',db_name)     
        with open(\'./sqlite_databases_code/\'+db_name+\'/db_details.txt\') as file:
            db_details_dict=json.loads(file.read())
        print(\'db_details_dict : \\n\',yellow(db_details_dict,bold=True)) 
        database = os.getcwd()+\'/z_bases/\'+db_name+\'.db\'
        database=database.replace("\\\\","/")
        table=db_details_dict[\'table_name\']
        print(\'database is :\',database) 
        print(\'table is :\',table)          
        # Get last index value in SQLITE DB
        new_index=sqlite_db_get_last_index(db_name)+1        
        print(\'new_index is :\',new_index)  
        sqlite_data=(new_index,'''
        len_columns=len(db_details_dict['columns'])-1
        i=0
        for col in db_details_dict['columns']:
            print(col)
            if i<len_columns:
                text_content=text_content+col+","
            else:
                text_content=text_content+col+")"
            i+=1        
        text_content=text_content+'''
        sql_add=f"INSERT OR IGNORE into {table} (`index`,'''
        i=0
        for col in db_details_dict['columns']:
            print(col)
            if i<len_columns:
                text_content=text_content+col+","
            else:
                text_content=text_content+col+")"
            i+=1           
        text_content=text_content+' VALUES (?,'
        i=0
        for col in db_details_dict['columns']:
            print(col)
            if i<len_columns:
                text_content=text_content+"?,"
            else:
                text_content=text_content+'?)"'
            i+=1         
        text_content=text_content+'''
        print(\'sqlite_data :\',sqlite_data)     
        print(\'sql_add :\',sql_add)          
        con = sqlite3.connect(database)       
        try:
            cur = con.cursor()
            cur.execute(sql_add,sqlite_data)
            con.commit()
            print(green(\'OK DONE ENTRY DELETED\',bold=True))
            image="../static/images/ok.png" 
            message1="Entry Added"
            message2="Entry was added to DB"
            message3=f"/{db_name}_dashboard"
            message4=f"{db_name}_dasbhoard"        
            PAGE_DESTINATION="operation_done"
            page_name="operation_done.html"            
            loguer(env.level+\' route END OF machin_db_add_entry_ok() in ***app.py*** : >\')    
            env.level=env.level[:-1]        
            return render_template(\'main_index.html\',route=route,USERNAME=session[\'user\'],PAGE_DESTINATION=PAGE_DESTINATION,message1=message1,message2=message2,message3=message3,message4=message4,image=image,page_name=page_name) 
        except:
            print(red(\'Error\',bold=True))
            image="../static/images/nok.png" 
            message1="Error"
            message2="An error occured"
            message3=f"/{db_name}_dashboard"
            message4=f"{db_name}_dasbhoard"        
            PAGE_DESTINATION="operation_done"
            page_name="operation_done.html"            
            loguer(env.level+\' route END OF machin_db_add_entry_ok() in ***app.py*** : >\')    
            env.level=env.level[:-1]        
            return render_template(\'main_index.html\',route=route,USERNAME=session[\'user\'],PAGE_DESTINATION=PAGE_DESTINATION,message1=message1,message2=message2,message3=message3,message4=message4,image=image,page_name=page_name)

'''        
        filename='./code_app_routes/route_def_'+db+'_db_add_entry_ok.py'
        with open(filename,"w") as fichier:
            fichier.write(text_content)     
        filename2='route_def_'+db+'_db_add_entry_ok.py'    
        with open('./code_architecture/app_routes.txt',"a+") as fichier:
            filename2=filename2.replace('/','')
            fichier.write(filename2+'\n')              
        result=1
    
    # ===================================================================
    loguer(env.level+' def END OF create_rte_for_db_add_entry_function() in app.py : >')    
    env.level=env.level[:-1]
    return result
    
