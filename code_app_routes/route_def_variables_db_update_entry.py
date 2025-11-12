#  def_variables_db_update_entry***
@app.route('/variables_db_update_entry', methods=['GET'])
def variables_db_update_entry():
    '''
    Flask Route for the variables_db_update_entry Database Update an entry
    '''
    route="/variables_db_update_entry"
    env.level+='-'
    print('\n'+env.level,white('route variables_db_update_entry() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route variables_db_update_entry() in ***app.py*** : >')
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        row=request.args.get("row")
        print("\nrow : ",row)
        name=request.args.get('name')
        print('\nname : ',name)
        environment_name=request.args.get('environment_name')
        print('\nenvironment_name : ',environment_name)
        value=request.args.get('value')
        print('\nvalue : ',value)
        description=request.args.get('description')
        print('\ndescription : ',description)
        comment=request.args.get('comment')
        print('\ncomment : ',comment)
        used_by=request.args.get('used_by')
        print('\nused_by : ',used_by)
        with open('./sqlite_databases_code/variables/db_details.txt') as file:
            db_details_dict=json.loads(file.read())
        print('db_details_dict : \n',yellow(db_details_dict,bold=True))        
        db_name = "variables.db"
        table_name = db_details_dict["table_name"]
        where_clause='`index` = '+row
        sql_fields=['index','name','environment_name','value','description','comment','used_by']
        sql_data_list=[int(row),name,environment_name,value,description,comment,used_by]
        result=sqlite_db_update_entry(db_name,table_name,where_clause,sql_fields,sql_data_list)        
        message1="OK done"
        image="../static/images/ok.png" 
        message2="entry had been updated"
        message3="/variables_dashboard"
        message4="variables Dashboard"
        PAGE_DESTINATION="operation_done"
        page_name="operation_done.html"
        loguer(env.level+' route END OF example_name() in ***app.py*** : >')
        # ===================================================================
        env.level=env.level[:-1]
        return render_template('main_index.html',route=route,USERNAME=session['user'],PAGE_DESTINATION=PAGE_DESTINATION,message1=message1,message2=message2,message3=message3,message4=message4,image=image,page_name=page_name)
 
