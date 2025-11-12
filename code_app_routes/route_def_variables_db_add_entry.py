#  def_variables_db_add_entry***
@app.route('/variables_db_add_entry', methods=['GET'])
def variables_db_add_entry():
    '''
    Flask Route for the variables_db_add_entry Database Update an entry
    '''
    route="/variables_db_add_entry"
    env.level+='-'
    print('\n'+env.level,white('route variables_db_add_entry() in ***app.py*** : >\n',bold=True))
    loguer(env.level+' route variables_db_add_entry() in ***app.py*** : >')
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        db_name = "variables.db"
        column_list=['name','environment_name','value','description','comment','used_by']
        print('\ncolumn_list :',cyan(column_list,bold=True))
        index=sqlite_db_get_last_index('variables')
        index+=1        
        print('index : ',index)
        PAGE_DESTINATION="z_sqlite_db_add_entry"
        page_name="z_sqlite_db_add_entry.html"
        db_name=db_name.split('.')[0]
        loguer(env.level+' route END OF example_name() in ***app.py*** : >')
        # ===================================================================
        env.level=env.level[:-1]
        return render_template('main_index.html',route=route,USERNAME=session['user'],PAGE_DESTINATION=PAGE_DESTINATION,page_name=page_name,column_list=column_list,index=index,db_name=db_name)
 
