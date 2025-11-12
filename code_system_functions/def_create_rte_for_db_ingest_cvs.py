#  def_create_rte_for_db_ingest_cvs***
def create_rte_for_db_ingest_cvs(name):
    '''
    MODIFIED : 2025-10-09T19:46:56.000Z

    description : create route for csv file ingestion in Database
    
    how to call it : create_rte_for_db_ingest_cvs(db_name)
    '''
    route="/create_rte_for_db_ingest_cvs"
    env.level+='-'
    print('\n'+env.level,white('def create_rte_for_db_ingest_cvs() in app.py : >\n',bold=True))
    loguer(env.level+' def create_rte_for_db_ingest_cvs() in app.py : >')
    # ===================================================================    
    db=name
    db_name=name.replace('./zbases/','')
    db_name=db_name.replace('.db','')
    name=name+'_db_ingest_csv'
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
        route="/"+db+"_db_ingest_csv"
        title="FLASK APP GENERATOR"
        with open('./sqlite_databases_code/'+db+'/db_details.txt') as file:
            db_details_dict=json.loads(file.read())
        print('db_details_dict : \n',yellow(db_details_dict,bold=True))       
        
        text_content='''#  def_'''+db+'''_db_ingest_csv***
@app.route('/'''+db+'''_db_ingest_csv', methods=['GET'])
def '''+db+'''_db_ingest_csv():
    \'\'\'
    '''+description+'''
    \'\'\'
    route="/'''+db+'''_db_ingest_csv"
    env.level+=\'-\'
    print(\'\\n\'+env.level,white(\'route '''+db+'''_db_ingest_csv() in ***app.py*** : >\\n\',bold=True))
    loguer(env.level+\' route '''+db+'''_db_ingest_csv() in ***app.py*** : >\')
    if not session.get(\'logged_in\'):
        return render_template(\'login.html\')
    else:
        db_name="'''+db+'''"
        message1="Message 1 :"
        image="../static/images/toolbox.png"
        message2="Message 2 :"
        message3="/Message 3"
        message4="Message 4 in button"
        PAGE_DESTINATION="z_sqlite_ingest_csv"
        page_name="z_sqlite_ingest_csv.html"
        loguer(env.level+\' route END OF '''+db+'''_db_ingest_csv() in ***app.py*** : >\')
        # ===================================================================
        env.level=env.level[:-1]
        return render_template(\'main_index.html\',route=route,USERNAME=session[\'user\'],PAGE_DESTINATION=PAGE_DESTINATION,message1=message1,message2=message2,message3=message3,message4=message4,image=image,page_name=page_name,db_name=db_name) 
'''        
        filename='./code_app_routes/route_def_'+db+'_db_ingest_csv.py'
        with open(filename,"w") as fichier:
            fichier.write(text_content)     
        with open('./code_architecture/app_routes.txt',"a+") as fichier:
            filename2=filename2.replace('/','')
            fichier.write(filename2+'\n')  
        result=1
    # ===================================================================
    loguer(env.level+' def END OF create_rte_for_db_ingest_cvs() in app.py : >')    
    env.level=env.level[:-1]
    return result
    
