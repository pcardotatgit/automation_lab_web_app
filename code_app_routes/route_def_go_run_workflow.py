#  def_go_run_workflow***
@app.route('/go_run_workflow', methods=['GET'])
def go_run_workflow():
    '''
    Created : 2025-10-31T14:00:17.000Z

    description : go to step execution formular
    '''
    route="/go_run_workflow"
    env.level+='-'
    print('\n'+env.level,white('route go_run_workflow() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route go_run_workflow() in ***app.py*** : >')
    global client_id
    global client_password
    global host
    global host_for_token
    global profil_name
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        with open('./result/step.txt') as file:
            step=file.read()
        print("\nRead step  : ",step)            
        current_index=step.split(' ')[1]
        next_step=int(current_index)+1
        if next_step==1:
            str_next_step='Step 01'
        elif next_step==2:
            str_next_step='Step 02'    
        elif next_step==3:
            str_next_step='Step 03' 
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
        database="workflows"
        print("\ndatabase : ",database)
        table="workflows"
        print("\ntable : ",table)
        where_clause=f'where step = "{step}"'
        entry_list=sqlite_db_select_entry(database,table,where_clause)
        print("\nentry_list : \n",entry_list)        
        if entry_list!=[]:
            row=entry_list[0][0]
            workflow_name=entry_list[0][1]
            step=entry_list[0][2]
            step_name=entry_list[0][3]
            if ' <=> ' in step_name:
                step_name_list=step_name.split(' <=> ')
                step_prefix=step_name_list [0]
                step_name=step_name_list [1]
            else:
                step_prefix=""
                step_name=step_name           
            input=entry_list[0][4]
            output=entry_list[0][5]
            comment=entry_list[0][6]
       
            PAGE_DESTINATION="z_go_run_workflow_step"
            page_name="z_go_run_workflow_step.html"
            loguer(env.level+' route END OF db_row_details_workflows() in ***app.py*** : >')
            # ===================================================================
            env.level=env.level[:-1]
            return render_template('main_index.html',route=route,USERNAME=session['user'],PAGE_DESTINATION=PAGE_DESTINATION,row=row,page_name=page_name,db_name=database,workflow_name=workflow_name,step=step,step_prefix=step_prefix,step_name=step_name,input=input,output=output,comment=comment,next_step=str_next_step)
        else:
            image="../static/images/ok.png"
            message1="End Of workflow"
            message2="Workflow completed"
            message3="/challenge_result"
            message4="Check Results"
            PAGE_DESTINATION="operation_done"
            page_name="operation_done.html"
            env.level=env.level[:-1]
            return render_template('main_index.html',route=route,USERNAME=session['user'],PAGE_DESTINATION=PAGE_DESTINATION,message1=message1,message2=message2,message3=message3,message4=message4,image=image,page_name=page_name)
 