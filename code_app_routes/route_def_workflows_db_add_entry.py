#  def_workflows_db_add_entry***
@app.route('/workflows_db_add_entry', methods=['GET'])
def workflows_db_add_entry():
    '''
    Flask Route for the workflows_db_add_entry Database Update an entry
    '''
    route="/workflows_db_add_entry"
    env.level+='-'
    print('\n'+env.level,white('route workflows_db_add_entry() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route workflows_db_add_entry() in ***app.py*** : >')
    if not session.get('logged_in'):
        return render_template('login.html')
    else:        
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
        # calculate next step
        next_step=nb_step+1
        if next_step==1:
            str_next_step='Step 01'
        elif next_step==2:
            str_next_step='Step 02'    
        elif next_step==3:
            str_next_step='Step 03' 
        elif next_step==4:
            str_next_step='Step 04' 
        elif next_step==5:
            str_next_step='Step 05' 
        elif next_step==6:
            str_next_step='Step 06' 
        elif next_step==7:
            str_next_step='Step 07' 
        elif next_step==8:
            str_next_step='Step 08'     
        elif next_step==9:
            str_next_step='Step 09'             
        else:
            str_next_step='Step '+str(next_step)        
        # API Calls
        db_name = "api_calls.db"
        table_name = "api_calls"
        engine = sqlalchemy.create_engine("sqlite:///z_bases/%s" % db_name, execution_options={"sqlite_raw_colnames": True})
        df = pd.read_sql_table(table_name, engine)
        out_df = df[['index','name','fqdn','relative_url','documentation','method','description','payload','header','body','query_params','custom_variables','authentication_profile','inputs_variables','output_variables']]
        #save result to csv file
        #out_df.to_csv(r'./result/api_calls.csv')
        df = DataFrame(out_df)
        #print (df)
        #save result to csv file
        #out_df.to_csv(r'./result/workflows.csv')
        df = DataFrame(out_df)
        #print (df)
        res = df.values.tolist()
        function_dict={}
        for item in res:
            print(item)    
            function_dict[item[1]]={
                'title':item[1],
            }                
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
        
        # Variables
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
        print('\nsorted_variables_list:\n',cyan(sorted_variables_list,bold=True))     
        for step in sorted_variables_list:
            for item,valeur in variables_dict.items():
                if item==step[1] and valeur['title']== step[0]:
                    sorted_variables_dict[item] = variables_dict[item]
                    break
            
        PAGE_DESTINATION="z_sqlite_db_add_entry_custom"
        page_name="z_sqlite_db_add_entry_custom.html"
        db_name="workflows"
        loguer(env.level+' route END OF example_name() in ***app.py*** : >')
        # ===================================================================
        env.level=env.level[:-1]
        return render_template('main_index.html',route=route,USERNAME=session['user'],PAGE_DESTINATION=PAGE_DESTINATION,page_name=page_name,column_list=column_list,index=index,db_name=db_name,steps_dict=sorted_dict,function_dict=function_dict,variables_dict=sorted_variables_dict,str_next_step=str_next_step,next_step=next_step)
 
