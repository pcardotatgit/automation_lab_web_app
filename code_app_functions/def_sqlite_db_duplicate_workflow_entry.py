#  def_sqlite_db_duplicate_workflow_entry***
def sqlite_db_duplicate_workflow_entry(db_name,row):
    '''
    MODIFIED : 2025-10-29

    description : duplicate selected row from the sqllite Database
    
    how to call it : result = sqlite_db_duplicate_workflow_entry(db_name,row)
    '''
    route="/sqlite_db_duplicate_workflow_entry"
    env.level+='-'
    print('\n'+env.level,white('def sqlite_db_duplicate_workflow_entry() in app.py : >\n',bold=True))
    loguer(env.level+' def sqlite_db_duplicate_workflow_entry() in app.py : >')
    # ===================================================================    
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        db_name=request.args.get("db_name")
        print('db_name :',db_name)     
        row=request.args.get("row")
        print('db_name :',row)              
        with open('./sqlite_databases_code/'+db_name+'/db_details.txt') as file:
            db_details_dict=json.loads(file.read())
        print('db_details_dict : \n',yellow(db_details_dict,bold=True)) 
        column_list=db_details_dict['columns']
        database = os.getcwd()+'/z_bases/'+db_name+'.db'
        database=database.replace("\\","/")
        table=db_details_dict['table_name']
        print('database is :',database) 
        print('table is :',table)          
        # read entry in data base
        where_clause='where `index` = '+row
        entry_list=sqlite_db_select_entry(db_name,table,where_clause)
        print("\nentry_list : \n",entry_list)   
        # calculate new step
        where_clause=''
        full_list=sqlite_db_select_entry(db_name,table,where_clause)
        #print("\nfull_list : \n",full_list) 
        last_step=''
        for item in full_list:
            #print(item[2])
            if item[2]>last_step:
                last_step=item[2]
        print("\nLast step is : \n",last_step) 
        step_index=int(last_step.split(' ')[1])
        step_index+=1
        if step_index=='1':
            step_index='01'
        elif step_index=='2':
            step_index='02'    
        elif step_index=='3':
            step_index='03' 
        elif step_index=='4':
            step_index='04' 
        elif step_index=='5':
            step_index='05' 
        elif step_index=='6':
            step_index='06' 
        elif step_index=='7':
            step_index='07' 
        elif step_index=='8':
            step_index='08'     
        elif step_index=='9':
            step_index='09'             
        else:
            step_index=str(step_index)
                
        new_step_index='Step '+str(step_index)
        print('New step index : ',cyan(new_step_index,bold=True))
        items={}
        i=0
        for obj in entry_list[0]:
            if i<len(column_list):
                if i==1:
                    items[i]={'name':column_list[i],'value':new_step_index}
                else:
                    items[i]={'name':column_list[i],'value':entry_list[0][i+1]}
            i+=1
        print('items : ',cyan(items,bold=True))        
        # Get last index value in SQLITE DB
        new_index=sqlite_db_get_last_index(db_name)+1        
        print('new_index is :',str(new_index)+'\n')         
        sqlite_data=[new_index]      
        i=0
        for obj in items.items():
            print('obj :',cyan(obj,bold=True))
            sqlite_data.append(obj[1]['value'])  
        sql_add=f"INSERT OR IGNORE into {table} (`index`,"
        i=0
        for obj in items.items():
            print('obj :',cyan(obj,bold=True))
            if i<len(column_list)-1:
                sql_add=sql_add+obj[1]['name']+','
            else:
                sql_add=sql_add+obj[1]['name']+') VALUES (?,'
            i+=1       
        i=0
        for obj in items:
            if i<len(column_list)-1:
                sql_add=sql_add+'?,'
            else:
                sql_add=sql_add+'?)'
            i+=1             
        print('sqlite_data :',sqlite_data)     
        print('sql_add :',sql_add)    
        con = sqlite3.connect(database)       
        try:
            cur = con.cursor()
            cur.execute(sql_add,sqlite_data)
            con.commit()
            print(green('OK DONE ENTRY DUPLICATED',bold=True))
            image="../static/images/ok.png" 
            message1="Entry Duplicated"
            message2="Entry was duplicated"
            message3=f"/{db_name}_dashboard"
            message4=f"{db_name}_dasbhoard"        
            PAGE_DESTINATION="operation_done"
            page_name="operation_done.html"            
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
            env.level=env.level[:-1]        
            return render_template('main_index.html',route=route,USERNAME=session['user'],PAGE_DESTINATION=PAGE_DESTINATION,message1=message1,message2=message2,message3=message3,message4=message4,image=image,page_name=page_name)


