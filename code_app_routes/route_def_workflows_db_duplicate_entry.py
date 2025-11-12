#  def_workflows_db_duplicate_entry***
@app.route('/workflows_db_duplicate_entry', methods=['GET'])
def workflows_db_duplicate_entry():
    '''
    Flask Route for the workflows_db_duplicate_entry Database delete entry
    '''
    route="/workflows_db_duplicate_entry"
    env.level+='-'
    print('\n'+env.level,white('route workflows_db_duplicate_entry() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route workflows_db_duplicate_entry() in ***app.py*** : >')
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        row=request.args.get("row")
        print("\nrow : ",row)        
        result=sqlite_db_duplicate_workflow_entry('workflows',row)         
        last_step=''
        db_name = "workflows"
        table="workflows"
        print('database is :',db_name) 
        print('table is :',table)          
        # read entry in data base
        where_clause=''
        full_list=sqlite_db_select_entry(db_name,table,where_clause)    
        for item in full_list:
            #print(item[2])
            if item[2]>last_step:
                last_step=item[2]
        print("\nLast step is : \n",last_step)         
        message1="OK done - Entry DUPLICATED"
        image="../static/images/ok.png" 
        message2="entry had been duplicated"
        message3="/workflows_step_details?step="+last_step
        message4="Edit New Step"
        PAGE_DESTINATION="operation_done"
        page_name="operation_done.html"
        loguer(env.level+' route END OF example_name() in ***app.py*** : >')
        # ===================================================================
        env.level=env.level[:-1]
        return render_template('main_index.html',route=route,USERNAME=session['user'],PAGE_DESTINATION=PAGE_DESTINATION,message1=message1,message2=message2,message3=message3,message4=message4,image=image,page_name=page_name)
 
