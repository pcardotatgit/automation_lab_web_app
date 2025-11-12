#  def_db_row_details_workflows***
@app.route('/db_row_details_workflows', methods=['GET'])
def db_row_details_workflows():
    '''
    Created : 2025-10-26
    description : 
    '''
    route="/db_row_details_workflows"
    env.level+='-'
    print('\n'+env.level,white('route db_row_details_workflows() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route db_row_details_workflows() in ***app.py*** : >')
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        # GET variable from calling web page
        row=request.args.get("row")
        print("\nrow : ",row)
        database=request.args.get("database")
        print("\ndatabase : ",database)
        table=request.args.get("table")
        print("\ntable : ",table)
        columns=request.args.get("columns")
        print("\ncolumns : ",columns)
        column_list=columns.split(',')
        where_clause='where `index` = '+row
        entry_list=sqlite_db_select_entry(database,table,where_clause)
        print("\nentry_list : \n",entry_list)
        workflow_name=entry_list[0][1]
        step=entry_list[0][2]
        step_name=entry_list[0][3]
        input=entry_list[0][4]
        output=entry_list[0][5]
        comment=entry_list[0][6]
        PAGE_DESTINATION="z_db_display_entry_details_workflows"
        page_name="z_db_display_entry_details_workflows.html"
        loguer(env.level+' route END OF db_row_details_workflows() in ***app.py*** : >')
        # ===================================================================
        env.level=env.level[:-1]
        return render_template('main_index.html',route=route,USERNAME=session['user'],PAGE_DESTINATION=PAGE_DESTINATION,page_name=page_name,db_name=database,row=row,workflow_name=workflow_name,step=step,step_name=step_name,input=input,output=output,comment=comment)
        
