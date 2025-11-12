#  def_workflows_db_update_entry***
@app.route('/workflows_db_update_entry', methods=['GET'])
def workflows_db_update_entry():
    '''
    version 20251105
    Flask Route for the workflows_db_update_entry Database Update an entry
    '''
    route="/workflows_db_update_entry"
    env.level+='-'
    print('\n'+env.level,white('route workflows_db_update_entry() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route workflows_db_update_entry() in ***app.py*** : >')
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        row=request.args.get("row")
        print("\nrow : ",row)
        workflow_name=request.args.get('workflow_name')
        print('\nworkflow_name : ',workflow_name)        
        step=request.args.get('step')
        print('\nstep : ',step)
        if "**" not in step:
            # NEW STEP
            int_step=int(step.split(' ')[1])
            #renumber_steps_minus_one(int_step)
            #renumber_steps(int_step)
        else:
            step=step.replace("**","")
        step_custom=request.args.get('step_custom')
        print('\nstep_custom : ',step_custom)   
        if step_custom!="":
            step=step_custom
        step_prefix=request.args.get('step_prefix')
        print('\nstep_prefix : ',step_prefix)        
        step_name=request.args.get('step_name')
        if step_prefix!='':
            step_name=step_prefix+' <=> '+step_name
        print('\nstep_name : ',step_name)
        custom_input=request.args.get('custom_input')
        print('\ncustom_input : ',custom_input)
        input=request.args.get('input')
        if custom_input!='':
            input=custom_input  
        if input=='':
            input="None"
        print('\ninput : ',input)        
        custom_output=request.args.get('custom_output') 
        print('\ncustom_output : ',custom_output)
        output=request.args.get('output')
        if custom_output!='':
            output=custom_output        
        if output=='':
            output="None"            
        print('\noutput : ',output)
        comment=request.args.get('comment')
        print('\ncomment : ',comment)
        with open('./sqlite_databases_code/workflows/db_details.txt') as file:
            db_details_dict=json.loads(file.read())
        print('db_details_dict : \n',yellow(db_details_dict,bold=True))        
        db_name = "workflows.db"
        table_name = db_details_dict["table_name"]
        where_clause='`index` = '+row
        sql_fields=['index','workflow_name','step','step_name','input','output','comment']
        sql_data_list=[int(row),workflow_name,step,step_name,input,output,comment]
        result=sqlite_db_update_entry(db_name,table_name,where_clause,sql_fields,sql_data_list)        
        message1="OK done"
        image="../static/images/ok.png" 
        message2="entry had been updated"
        message3="/workflows_dashboard"
        message4="workflows Dashboard"
        PAGE_DESTINATION="operation_done"
        page_name="operation_done.html"
        loguer(env.level+' route END OF example_name() in ***app.py*** : >')
        # ===================================================================
        env.level=env.level[:-1]
        return render_template('main_index.html',route=route,USERNAME=session['user'],PAGE_DESTINATION=PAGE_DESTINATION,message1=message1,message2=message2,message3=message3,message4=message4,image=image,page_name=page_name)
 
