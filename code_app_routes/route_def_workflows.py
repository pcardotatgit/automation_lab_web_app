#  def_workflows***
@app.route('/workflows', methods=['GET'])
def workflows():
    '''
    Created : 2025-10-29T16:28:37.000Z

    description : display workflow creation dashboard
    '''
    route="/workflows"
    env.level+='-'
    print('\n'+env.level,white('route workflows() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route workflows() in ***app.py*** : >')
    global client_id
    global client_password
    global host
    global host_for_token
    global profil_name
    if not session.get('logged_in'):
        return render_template('login.html')
    else:     
        keyword='' # select every entries in DB
        with open('./sqlite_databases_code/workflows/db_details.txt') as file:
            db_details_dict=json.loads(file.read())
        print('db_details_dict : \n',yellow(db_details_dict,bold=True))
        database = os.getcwd()+'/z_bases/workflows.db'
        database=database.replace("\\","/")
        print('database is :',database)
        # sqlite:///:memory: (or, sqlite://)
        # sqlite:///relative/path/to/file.db
        # sqlite:////absolute/path/to/file.db
        db_name = "workflows.db"
        table_name = db_details_dict["table_name"]
        engine = sqlalchemy.create_engine("sqlite:///z_bases/%s" % db_name, execution_options={"sqlite_raw_colnames": True})
        df = pd.read_sql_table(table_name, engine)
        out_df = df[['index','workflow_name','step','step_name','input','output','comment']]
        #save result to csv file
        #out_df.to_csv(r'./result/workflows.csv')
        df = DataFrame(out_df)
        #print (df)
        select_options=''
        res = df.values.tolist()
        step_dict={}
        for item in res:
            print(item)    
            step_dict[item[2]]={
                'title':item[2],
                'description':item[3]
            }         
        print('step_dict : ' ,yellow(step_dict,bold=True))
        # sort detection by steps
        sorted_dict = {}
        step_list=[]
        for item,value in step_dict.items():
            print('item:\n',yellow(item,bold=True))   
            print('value:\n',yellow(value,bold=True))
            step_list.append([value['title'],item])
        sorted_step_list = sorted(step_list, key=operator.itemgetter(0),reverse=False)     
        print()
        print('sorted step_list:\n',cyan(sorted_step_list,bold=True))   
        print()     
        for step in sorted_step_list:
            for item,valeur in step_dict.items():
                if item==step[1] and valeur['title']== step[0]:
                    sorted_dict[item] = step_dict[item]
                    break    
        
        print('=========================================')
        columns="workflow_name,step,step_name,input,output,comment"    
        message1="Message 1 :"
        image="../static/images/toolbox.png" 
        message2="Message 2 :"
        message3="/Message 3"
        message4="Message 4 in button"
        PAGE_DESTINATION="z_workflows"
        page_name="z_workflows.html"
        loguer(env.level+' route END OF workflows() in ***app.py*** : >')
        # ===================================================================
        env.level=env.level[:-1]
        return render_template('main_index.html',route=route,USERNAME=session['user'],PAGE_DESTINATION=PAGE_DESTINATION,page_name=page_name,step_dict=sorted_dict)
        
