#  def_create_rte_for_db_update_entry_function***
def create_rte_for_db_update_entry_function(name):
    '''
    MODIFIED : 2025-09-30T15:23:41.000Z

    description : create route for db update entry
    
    how to call it :
    '''
    route="/create_rte_for_db_update_entry_function"
    env.level+='-'
    print('\n'+env.level,white('def create_rte_for_db_update_entry_function() in app.py : >\n',bold=True))
    loguer(env.level+' def create_rte_for_db_update_entry_function() in app.py : >')
    # ===================================================================    
    db=name
    db_name=name.replace('./zbases/','')
    db_name=db_name.replace('.db','')
    name=name+'_db_update_entry'
    filename='./code_app_routes/route_def_'+name+'.py'
    filename2='/route_def_'+name+'.py'
    description='Flask Route for the '+name+' Database Update an entry'
    print()
    print(' filename :\n',yellow(filename,bold=True))
    print()
    print(' filename2 :\n',yellow(filename2,bold=True))
    print()
    print(magenta('--> CALL  A SUB FUNCTION :',bold=True))
    # check if file already exits
    with open('./code_architecture/app_routes.txt') as file:
        text_content2=file.read()    
    fichier_route = Path('./code_app_routes/route_def_'+name+'.py')    
    if fichier_route.is_file() or filename in text_content2:
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
        route="/"+db+"_db_update_entry"
        title="FLASK APP GENERATOR"
        with open('./sqlite_databases_code/'+db+'/db_details.txt') as file:
            db_details_dict=json.loads(file.read())
        print('db_details_dict : \n',yellow(db_details_dict,bold=True))       
        
        text_content='''#  def_'''+db+'''_db_update_entry***
@app.route('/'''+db+'''_db_update_entry', methods=['GET'])
def '''+db+'''_db_update_entry():
    \'\'\'
    '''+description+'''
    \'\'\'
    route="/'''+db+'''_db_update_entry"
    env.level+=\'-\'
    print(\'\\n\'+env.level,white(\'route '''+db+'''_db_update_entry() in ***app.py*** : >\\n\',bold=True))
    loguer(env.level+\' route '''+db+'''_db_update_entry() in ***app.py*** : >\')
    if not session.get(\'logged_in\'):
        return render_template(\'login.html\')
    else:
        row=request.args.get("row")
        print("\\nrow : ",row)'''
        len_columns=len(db_details_dict['columns'])-1
        i=0
        for col in db_details_dict['columns']:
            print(col)
            if i<len_columns:
                text_content=text_content+'''\n        '''+col+'''=request.args.get(\''''+col+'''\')\n        print('\\n'''+col+''' : \','''+col+''')'''  
        text_content=text_content+'''
        with open(\'./sqlite_databases_code/'''+db+'''/db_details.txt\') as file:
            db_details_dict=json.loads(file.read())
        print(\'db_details_dict : \\n\',yellow(db_details_dict,bold=True))        
        db_name = "'''+db+'''.db"
        table_name = db_details_dict["table_name"]
        where_clause='`index` = '+row
        sql_fields=[\'index\',\''''
        i=0
        for col in db_details_dict['columns']:
            print(col)
            if i<len_columns:
                text_content=text_content+col+"','"
            else:
                text_content=text_content+col+"']"
            i+=1
        text_content=text_content+'''\n        sql_data_list=[int(row),'''
        i=0
        for col in db_details_dict['columns']:
            print(col)
            if i<len_columns:
                text_content=text_content+col+","
            else:
                text_content=text_content+col+"]"
            i+=1        
        
        text_content=text_content+'''
        result=sqlite_db_update_entry(db_name,table_name,where_clause,sql_fields,sql_data_list)        
        message1="OK done"
        image="../static/images/ok.png" 
        message2="entry had been updated"
        message3="/'''+db+'''_dashboard"
        message4="'''+db+''' Dashboard"
        PAGE_DESTINATION="operation_done"
        page_name="operation_done.html"
        loguer(env.level+\' route END OF example_name() in ***app.py*** : >\')
        # ===================================================================
        env.level=env.level[:-1]
        return render_template(\'main_index.html\',route=route,USERNAME=session[\'user\'],PAGE_DESTINATION=PAGE_DESTINATION,message1=message1,message2=message2,message3=message3,message4=message4,image=image,page_name=page_name)
 
'''        
        filename='./code_app_routes/route_def_'+db+'_db_update_entry.py'
        with open(filename,"w") as fichier:
            fichier.write(text_content)     
        with open('./code_architecture/app_routes.txt',"a+") as fichier:
            filename2=filename2.replace('/','')
            fichier.write(filename2+'\n')  
        result=1
    
    # ===================================================================
    loguer(env.level+' def END OF create_rte_for_db_update_entry_function() in app.py : >')    
    env.level=env.level[:-1]
    return result
    
