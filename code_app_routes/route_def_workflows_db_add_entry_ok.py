#  def_workflows_db_add_entry_ok***
@app.route('/workflows_db_add_entry_ok', methods=['GET'])
def workflows_db_add_entry_ok():
    '''
        version : 20251103
        Flask Route for the workflows_db_add_entry Database Update an entry
    '''
    route="/workflows_db_add_entry_ok"
    env.level+='-'
    print('\n'+env.level,white('route workflows_db_add_entry_ok() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route workflows_db_add_entry_ok() in ***app.py*** : >')
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        workflow_name=request.args.get("workflow_name")
        print("\nworkflow_name: ",workflow_name)
        step=request.args.get("step")
        print("\nstep: ",step)        
        if 'Step' not in step:
            if step=='1':
                step='Step 01'
            elif step=='2':
                step='Step 02'    
            elif step=='3':
                step='Step 03' 
            elif step=='4':
                step='Step 04' 
            elif step=='5':
                step='Step 05' 
            elif step=='6':
                step='Step 06' 
            elif step=='7':
                step='Step 07' 
            elif step=='8':
                step='Step 08'     
            elif step=='9':
                step='Step 09'             
            else:
                step='Step '+step
        else:
            insert_in_position=step.split(' ')[1]
            insert_in_position=int(insert_in_position)
            result=renumber_steps(insert_in_position)
        print("\nstep: ",step)
        step_prefix=request.args.get('step_prefix')
        print('\nstep_prefix : ',step_prefix)        
        step_name=request.args.get('step_name')
        if step_prefix!='':
            step_name=step_prefix+' <=> '+step_name
        print("\nstep_name: ",step_name)
        custom_input=request.args.get('custom_input')
        print('\ncustom_input : ',custom_input)        
        input=request.args.get("input")
        if custom_input!='':
            input=custom_input          
        if input=='':
            input="None" 
        print("\ninput: ",input)

        custom_output=request.args.get('custom_output') 
        print('\ncustom_output : ',custom_output)        
        output=request.args.get("output")
        if custom_output!='':
            output=custom_output         
        if output=='':
            output="None" 
        print("\noutput: ",output)
        comment=request.args.get("comment")
        print("\ncomment: ",comment)
        # ##############################
        db_name="workflows"
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
        sqlite_data=(new_index,workflow_name,step,step_name,input,output,comment)
        sql_add=f"INSERT OR IGNORE into {table} (`index`,workflow_name,step,step_name,input,output,comment) VALUES (?,?,?,?,?,?,?)"
        print('sqlite_data :',sqlite_data)     
        print('sql_add :',sql_add)          
        con = sqlite3.connect(database)       
        try:
            cur = con.cursor()
            cur.execute(sql_add,sqlite_data)
            con.commit()
            print(green('OK DONE ENTRY ADDED',bold=True))
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
        except:
            print(red('Error',bold=True))
            image="../static/images/nok.png" 
            message1="Error"
            message2="An error occured"
            message3=f"/{db_name}_dashboard"
            message4=f"{db_name}_dasbhoard"        
            PAGE_DESTINATION="operation_done"
            page_name="operation_done.html"            
            env.level=env.level[:-1]        
            return render_template('main_index.html',route=route,USERNAME=session['user'],PAGE_DESTINATION=PAGE_DESTINATION,message1=message1,message2=message2,message3=message3,message4=message4,image=image,page_name=page_name)
        