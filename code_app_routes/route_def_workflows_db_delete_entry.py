#  def_workflows_db_delete_entry***
@app.route('/workflows_db_delete_entry', methods=['GET'])
def workflows_db_delete_entry():
    '''
    Flask Route for the workflows_db_delete_entry Database delete entry
    '''
    route="/workflows_db_delete_entry"
    env.level+='-'
    print('\n'+env.level,white('route workflows_db_delete_entry() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route workflows_db_delete_entry() in ***app.py*** : >')
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        row=request.args.get("row")
        print("\nrow : ",row)        
        # GET variable from calling web page
        step=request.args.get("step")
        print("\nstep : ",step)
        database="workflows"
        print("\ndatabase : ",database)
        table="workflows"
        print("\ntable : ",table)
        where_clause=f'where `index` = "{row}"'
        entry_list=sqlite_db_select_entry(database,table,where_clause)
        print("\nentry_list : \n",entry_list)
        row=str(entry_list[0][0])
        workflow_name=entry_list[0][1]
        step=entry_list[0][2]
        step_name=entry_list[0][3]          
        input=entry_list[0][4]
        output=entry_list[0][5]
        comment=entry_list[0][6]          
        result=renumber_steps_delete(step)       
        result=sqlite_db_delete_entry('workflows',row)            
        db_name = "workflows.db"
        table_name = "workflows"
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