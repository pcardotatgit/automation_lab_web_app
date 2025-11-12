#  def_workflows_step_details***
@app.route('/workflows_step_details', methods=['GET'])
def workflows_step_details():
    '''
    Created : 2025-11-03

    description : display formular for editing selected step details
    '''
    route="/workflows_step_details"
    env.level+='-'
    print('\n'+env.level,white('route workflows_step_details() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route workflows_step_details() in ***app.py*** : >')
    global client_id
    global client_password
    global host
    global host_for_token
    global profil_name
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        # GET variable from calling web page
        step=request.args.get("step")
        step0=step
        print("\nstep : ",step)
        with open('./result/step.txt','w') as file:
            file.write(step)        
        database="workflows"
        print("\ndatabase : ",database)
        table="workflows"
        print("\ntable : ",table)
        where_clause=f'where step = "{step}"'
        entry_list=sqlite_db_select_entry(database,table,where_clause)
        print("\nentry_list : \n",entry_list)
        row=entry_list[0][0]
        workflow_name=entry_list[0][1]
        #step=entry_list[0][2]
        step_name=entry_list[0][3]
        if ' <=> ' in step_name:
            step_name_list=step_name.split(' <=> ')
            step_prefix=step_name_list [0]
            step_name=step_name_list [1]
        else:
            step_prefix=""
            step_name=step_name           
        input=entry_list[0][4]
        if input=='':
            input='None'
        output=entry_list[0][5]
        if output=='':
            output='None'        
        comment=entry_list[0][6]
        # api calls
        db_name = "api_calls.db"
        table_name = "api_calls"
        engine = sqlalchemy.create_engine("sqlite:///z_bases/%s" % db_name, execution_options={"sqlite_raw_colnames": True})
        df = pd.read_sql_table(table_name, engine)
        out_df = df[['index','name','fqdn','relative_url','documentation','method','description','payload','header','body','query_params','custom_variables','authentication_profile','inputs_variables','output_variables']]
        #save result to csv file
        out_df.to_csv(r'./result/api_calls.csv')
        df = DataFrame(out_df)
        #print (df)
        #save result to csv file
        #out_df.to_csv(r'./result/workflows.csv')
        df = DataFrame(out_df)
        #print (df)
        select_options=''
        res = df.values.tolist()
        function_dict={}
        for item in res:
            print(item)    
            function_dict[item[1]]={
                'title':item[1],
            }     
        # functions
        # Functions
        db_name = "functions.db"
        table_name = "functions"
        engine = sqlalchemy.create_engine("sqlite:///z_bases/%s" % db_name, execution_options={"sqlite_raw_colnames": True})
        df = pd.read_sql_table(table_name, engine)
        out_df = df[['index','name','environment_name','description','called_function','input_variables','output_variables','comment']]
        df = DataFrame(out_df)
        #print (df)
        res = df.values.tolist()
        for item in res:
            print(item)    
            function_dict[item[1]]={
                'title':item[1],
            }         
        # variables        
        db_name = "variables.db"
        table_name = "variables"
        engine = sqlalchemy.create_engine("sqlite:///z_bases/%s" % db_name, execution_options={"sqlite_raw_colnames": True})
        df = pd.read_sql_table(table_name, engine)
        out_df = df[['index','name','environment_name','value','description','comment','used_by']]
        df = DataFrame(out_df)
        #print (df)
        res = df.values.tolist()
        variables_dict={}
        for item in res:
            print(item)    
            variables_dict[item[1]]={
                'title':item[1],
            }      
        sorted_variables_dict = {}
        variables_list=[]
        for item,value in variables_dict.items():
            print('item:\n',yellow(item,bold=True))   
            print('value:\n',yellow(value,bold=True))
            variables_list.append([value['title'],item])
        sorted_variables_list = sorted(variables_list, key=operator.itemgetter(0),reverse=False)     
        print()
        print('sorted_variables_list:\n',cyan(sorted_variables_list,bold=True))   
        print()     
        for step in sorted_variables_list:
            for item,valeur in variables_dict.items():
                if item==step[1] and valeur['title']== step[0]:
                    sorted_variables_dict[item] = variables_dict[item]
                    break            
        # STEPs
        db_name = "workflows.db"
        column_list=['workflow_name','step','step_name','input','output','comment']
        print('\ncolumn_list :',cyan(column_list,bold=True))
        index=sqlite_db_get_last_index('workflows')
        index+=1        
        print('index : ',index)
        # step list
        step_list_dict={}
        table_name = "workflows"
        engine = sqlalchemy.create_engine("sqlite:///z_bases/%s" % db_name, execution_options={"sqlite_raw_colnames": True})
        df = pd.read_sql_table(table_name, engine)
        out_df = df[['index','workflow_name','step','step_name','input','output','comment']]
        df = DataFrame(out_df)
        #print (df)
        res = df.values.tolist()
        steps_dict={}
        nb_step=0
        for item in res:
            print(item)    
            steps_dict[item[2]]={
                'title':item[2],
                'index':item[0]
            }  
            nb_step+=1
        print('steps_dict : ' ,yellow(steps_dict,bold=True))
        # sort detection by steps
        sorted_dict = {}
        step_list=[]
        for item,value in steps_dict.items():
            print('item:\n',yellow(item,bold=True))   
            print('value:\n',yellow(value,bold=True))
            step_list.append([value['title'],item])
        sorted_step_list = sorted(step_list, key=operator.itemgetter(0),reverse=False)     
        print()
        print('sorted step_list:\n',cyan(sorted_step_list,bold=True))   
        print()     
        for step in sorted_step_list:
            for item,valeur in steps_dict.items():
                if item==step[1] and valeur['title']== step[0]:
                    sorted_dict[item] = steps_dict[item]
                    break           
        
        # ######################################
        PAGE_DESTINATION="z_db_display_entry_details_workflows"
        page_name="z_db_display_entry_details_workflows.html"
        loguer(env.level+' route END OF db_row_details_workflows() in ***app.py*** : >')
        # ===================================================================
        env.level=env.level[:-1]
        return render_template('main_index.html',route=route,USERNAME=session['user'],PAGE_DESTINATION=PAGE_DESTINATION,row=row,page_name=page_name,db_name=database,workflow_name=workflow_name,step=step0,step_prefix=step_prefix,step_name=step_name,sorted_step_dict=sorted_dict,input=input,output=output,comment=comment,function_dict=function_dict,variables_dict=sorted_variables_dict)
        
