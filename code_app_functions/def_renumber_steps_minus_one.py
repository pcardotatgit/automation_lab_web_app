#  def_renumber_steps_minus_one***
def renumber_steps_minus_one(step):
    '''
    MODIFIED : 2025-11-01T18:18:23.000Z

    description : renumber steps from step number given as input
    
    how to call it :
    '''
    route="/renumber_steps_minus_one"
    env.level+='-'
    print('\n'+env.level,white('def renumber_steps_minus_one() in app.py : >\n',bold=True))
    loguer(env.level+' def renumber_steps_minus_one() in app.py : >')
    if not session.get('logged_in'):
        return render_template('login.html')
    else:      
        print('step :',step,type(step))  
        sys.exit()
        db_name = "workflows.db"
        column_list=['workflow_name','step','step_name','input','output','comment']
        print('\ncolumn_list :',cyan(column_list,bold=True))
        # step list
        table_name = "workflows"
        engine = sqlalchemy.create_engine("sqlite:///z_bases/%s" % db_name, execution_options={"sqlite_raw_colnames": True})
        df = pd.read_sql_table(table_name, engine)
        out_df = df[['index','workflow_name','step','step_name','input','output','comment']]
        df = DataFrame(out_df)
        #print (df)
        res = df.values.tolist()
        steps_dict={}
        step_index=0
        if step!=1:        
            for item in res:
                print(item)    
                row_step_number=item[2].split(' ')[1]
                row_step_number=int(row_step_number)
                if row_step_number<=step:
                    if row_step_number>0:
                        row_step_number=row_step_number-1
                    if row_step_number==1:
                        new_step_number='Step 01'
                    elif row_step_number==2:
                        new_step_number='Step 02'    
                    elif row_step_number==3:
                        new_step_number='Step 03' 
                    elif row_step_number==4:
                        new_step_number='Step 04' 
                    elif row_step_number==5:
                        new_step_number='Step 05' 
                    elif row_step_number==6:
                        new_step_number='Step 06' 
                    elif row_step_number==7:
                        new_step_number='Step 07' 
                    elif row_step_number==8:
                        new_step_number='Step 08'     
                    elif row_step_number==9:
                        new_step_number='Step 09'             
                    else:        
                        new_step_number='Step '+str(row_step_number)            
                    steps_dict[step_index]={
                        'new_step':new_step_number,
                        'index':str(item[0])
                    }
                step_index+=1
        else:
            for item in res:
                print(item)    
                row_step_number=item[2].split(' ')[1]
                row_step_number=int(row_step_number)
                if row_step_number>=step:
                    row_step_number=row_step_number+1
                    if row_step_number==1:
                        new_step_number='Step 01'
                    elif row_step_number==2:
                        new_step_number='Step 02'    
                    elif row_step_number==3:
                        new_step_number='Step 03' 
                    elif row_step_number==4:
                        new_step_number='Step 04' 
                    elif row_step_number==5:
                        new_step_number='Step 05' 
                    elif row_step_number==6:
                        new_step_number='Step 06' 
                    elif row_step_number==7:
                        new_step_number='Step 07' 
                    elif row_step_number==8:
                        new_step_number='Step 08'     
                    elif row_step_number==9:
                        new_step_number='Step 09'             
                    else:        
                        new_step_number='Step '+str(row_step_number)            
                    steps_dict[step_index]={
                        'new_step':new_step_number,
                        'index':str(item[0])
                    }       
                step_index+=1                    
        print('STEPS TO UPDATE : ',cyan(steps_dict,bold=True))
        for item in steps_dict.items():
            print(" item : ",item)
            #print(" item['index'] : ",item[1]['index'])
            #print("item['new_step'] : ",item[1]['new_step'])
            result=workflow_sqlite_update_step(item[1]['index'],item[1]['new_step'])            
        result=1
        # ===================================================================
        env.level=env.level[:-1]
        return result
    
