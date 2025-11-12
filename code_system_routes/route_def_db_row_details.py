#  def_db_row_details***
@app.route('/db_row_details', methods=['GET'])
def db_row_details():
    '''
    Created : 2025-10-26
    description : 
    '''
    route="/db_row_details"
    env.level+='-'
    print('\n'+env.level,white('route db_row_details() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route db_row_details() in ***app.py*** : >')
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
        items={}
        i=0
        for obj in entry_list[0]:
            if i<len(column_list):
                items[i]={'name':column_list[i],'value':entry_list[0][i+1]}
            i+=1
        print('items : ',cyan(items,bold=True))
        PAGE_DESTINATION="z_db_display_entry_details"
        page_name="z_db_display_entry_details.html"
        loguer(env.level+' route END OF db_row_details() in ***app.py*** : >')
        # ===================================================================
        env.level=env.level[:-1]
        return render_template('main_index.html',route=route,USERNAME=session['user'],PAGE_DESTINATION=PAGE_DESTINATION,page_name=page_name,items=items,db_name=database,row=row)
        
